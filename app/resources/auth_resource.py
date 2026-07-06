from flask import request
from flask_restful import Resource
from pydantic import ValidationError
from flask_jwt_extended import create_access_token, create_refresh_token
from app.services.user_service import user_service
from app.schemas.auth_schema import RegisterSchema, LoginSchema
from app.models.user_model import User
from app.utils.security import hash_password, verify_password, Crypto
from db import db


class LoginResource(Resource):
    
    def post(self):
        try:
            data = request.get_json()
            validate_data = LoginSchema.model_validate(data)
            
            user = user_service.find_by_email(validate_data.email)
            
            if user is None:
                return{
                    'error': 'User not found'
                }, 400
                
            password_validate = verify_password(user.password, validate_data.password)
            
            if not password_validate:
                return{
                    'error': 'Password incorrect'
                }, 401
            
            crypto = Crypto()
            hashed_id = crypto.encrypt(user.id)
            
            access_token = create_access_token(
                identity=hashed_id,
                additional_claims={
                    'name': user.name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'role_id': user.role_id
                }
            )
            
            refresh_token = create_refresh_token(identity=hashed_id)
            
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        
        except ValidationError as e:
            return{
                'error': e.errors()
            },400
        
        except Exception as e:
            return{
                "error": str(e)
            }, 500


class RegisterResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            
            validate_data = RegisterSchema.model_validate(data)
            
            user = User.query.filter_by(email=validate_data.email).first()

            user_exist = user_service.find_by_email(validate_data.email)
            
            if user_exist:
                return{
                    'error': 'The email address is already registered'
                }, 400
            
            created_user = User(
                    name=validate_data.name,
                    last_name=validate_data.last_name,
                    email=validate_data.email,
                    password=hash_password(validate_data.password),
                    role_id=validate_data.role_id
                )
            
            db.session.add(created_user)
            db.session.commit()
            
            return created_user.to_json(), 201

        except ValidationError as e:
            return {'error': e.errors()}, 400
        
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500

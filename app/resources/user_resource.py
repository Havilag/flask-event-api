from flask_restful import Resource
from app.models.user_model import User
from app.schemas.user_schema import UserSchema
from app.services.user_service import user_service
from flask import request
from pydantic import ValidationError
from db import db


class UserResource(Resource):
    
    def get(self):
        try:
            users: list[User] = User.query.all()
            
            users_list = [user.to_json() for user in users]
             
            return users_list, 200
         
        except Exception as e:
            return{
                'error': str(e)
            }, 400
    
    
    def post(self):
        try:
            data = request.get_json()
            validate_data = UserSchema.model_validate(data)
            
            create_user = user_service.create(validate_data)
            
            return create_user.to_json(), 201
    
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 400


class ManageUserResource(Resource):
    
    def get(self, user_id: int):
        
        try:
            
            user = user_service.get_by_id(user_id)
            
            if not user:
                return {
                    'error': 'User not found'
                }, 404
            
            return user.to_json(), 200
        
        except Exception as e:
            return {
                'error': str(e)
            }, 400
    
    def put(self,  user_id: int):
        
        try:
            user = user_service.get_by_id(user_id)
            
            if not user:
                return {
                    'error': 'User not found'
                }, 404
            
            data = request.get_json()
            validate_data = UserSchema.model_validate(data)
            
            updated_user = user_service.update(user, validate_data)
            
            return updated_user.to_json(), 200

        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
            
        except Exception as e:
            return {
                'error': str(e)
            }, 400
        
    
    def delete(self, user_id: int):
        try:
            user = user_service.get_by_id(user_id)
            
            if not user:
                return {
                    'error': 'User not found'
                }, 404
            
            user_service.delete(user)
            
            return {"message": "User deleted successfully"}, 200
        
        except Exception as e:
            return {
                'error': str(e)
            }, 400
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from app.services.user_service import user_service


class LoginResource(Resource):
    
    def post(self):
        try:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
            
            if not username or not password:
                return{
                    'error': 'Missing username or password'
                }, 400
                
            user = user_service.get_by_username(username)
            
            if not user or user.password != password:
                return{
                    'error': 'Invalid username or password'
                }, 401
            
            access_token = create_access_token(identity=str(user.id))
            
            return {
                "access_token": access_token,
                "message": "Login successful"
            }, 200
        
        except Exception as e:
            return{
                "error": str(e)
            }, 500
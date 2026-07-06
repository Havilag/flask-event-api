from flask_restful import Resource
from app.services.role_service import role_service
from app.schemas.role_schema import RoleSchema
from pydantic import ValidationError
from flask import request


class RoleResource(Resource):
    
    def get(self):
        try:
            roles = role_service.get_all()
            
            roles_list = [role.to_json() for role in roles] 

            return roles_list, 200
        
        except Exception as e:
            return {
                'error': str(e)
            }, 400
    
    def post(self):
        try:
            data = request.get_json()
            validate_data = RoleSchema.model_validate(data)
            
            create_role = role_service.create(validate_data)
            
            return create_role.to_json(), 201
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 400


class ManageRoleResource(Resource):
    
    def get(self, role_id: int):
        try:
            role = role_service.get_by_id(role_id)
            
            if not role:
                return {
                    'error': 'Role not found'
                }, 404
            
            return role.to_json(), 200
        
        except Exception as e:
            return {
                'error': str(e)
            }, 400
    
    def put(self, role_id: int):
        try:
            role = role_service.get_by_id(role_id)
            
            if not role:
                return {
                    'error': 'Role not found'
                }, 404
            
            data = request.get_json()
            validate_data = RoleSchema.model_validate(data)
            
            update_role = role_service.update(role, validate_data)
            
            return update_role.to_json(), 200
        
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 400
    
    def delete(self, role_id: int):
        try:
            role = role_service.get_by_id(role_id)
            
            if not role:
                return {
                    'error': 'Role not found'
                }, 404
            
            role_service.delete(role)
            
            return {"message": "Role deleted successfully"}, 200
            
        except Exception as e:
            return {
                'error': str(e)
            }, 400
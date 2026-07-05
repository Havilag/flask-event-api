from flask_restful import Resource
from app.services.role_service import role_service


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
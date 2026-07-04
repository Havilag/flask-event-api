from app.models.role_model import Role
from app.schemas.role_schema import RoleSchema
from db import db



class RoleService:
    
    def get_all(self):
        return Role.query.all()
    
    def get_by_id(self, id: int) -> Role | None:
        role = Role.query.filter_by(
            id=id
        ).first()
        
        return role

    
    def create(self, data: RoleSchema) -> Role:
        role = Role(
            name = data.name
        )
        
        db.session.add(role)
        db.session.commit()
        return role
    
    def update(self, role: Role, data: RoleSchema):
        role.name = data.name
        
        db.session.commit()
        return role
    
    def delete(self, role: Role) -> None:
        db.session.delete(role)
        db.session.commit()

role_service = RoleService()
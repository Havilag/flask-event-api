from app.models.user_model import User
from app.schemas.user_schema import UserSchema
from db import db


class UserService:
    
    def get_all(self):
        return User.query.filter_by(is_active=True).all()
        
    
    def get_by_id(self, id: int) -> User | None:
        user = User.query.filter_by(
            id=id,
            is_active=True
        ).first()
        
        return user
    
    
    
    def get_by_username(self, username: str) -> User | None:
        return User.query.filter_by(username=username).first()
    
    
        
    def create(self, data: UserSchema ) -> User:
        created_user = User(
            name = data.name,
            last_name = data.last_name,
            email = data.email,
            password = data.password,
            is_active=True,
            role_id = data.role_id,
        )
        
        db.session.add(created_user)
        db.session.commit()
        
        return created_user
    
    def update(self, user: User, data: UserSchema) -> User:
        user.name=data.name
        user.last_name = data.last_name
        user.email = data.email
        user.password = data.password
        
        return user

    def delete(self, user: User) -> None:
        user.is_active = False
        db.session.commit()

user_service = UserService()
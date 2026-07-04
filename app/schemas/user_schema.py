from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    password: str
    is_active: bool
    role_id: int
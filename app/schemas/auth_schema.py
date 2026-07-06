from pydantic import BaseModel, EmailStr, Field


class RegisterSchema(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    password: str
    role_id: int = Field(default=4)


class LoginSchema(BaseModel):
    email: EmailStr
    password: str
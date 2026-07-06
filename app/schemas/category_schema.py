from pydantic import BaseModel


class CategorySchema(BaseModel):
    name: str
    is_active: bool = True
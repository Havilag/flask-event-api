from app.models.category_model import Category
from app.schemas.category_schema import CategorySchema
from db import db


class CategoryService:
    
    def get_all(self):
        return Category.query.filter_by(is_active=True).all()
    
    def get_by_id(self, id: int) -> Category | None:
        category = Category.query.filter_by(
            id=id,
            is_active=True
        ).first()
        
        return category
    
    
    def create(self, data: CategorySchema) -> Category:
        category = Category(
            name = data.name,
            is_active = True
        )
        db.session.add(category)
        db.session.commit()
        
        return category
    
    
    def update(self, category: Category, data: CategorySchema):
        category.name = data.name
        
        db.session.commit()
        
        return category

    def delete(self, category: Category) -> None:
        category.is_active = False
        db.session.commit()
        
category_service = CategoryService()
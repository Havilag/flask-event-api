from flask_restful import Resource
from app.schemas.category_schema import CategorySchema
from app.services.category_service import category_service
from flask import request
from pydantic import ValidationError


class CategoryResource(Resource):
    
    def get(self):
        try:
        
            categories = category_service.get_all()
            category_list = [category.to_json() for category in categories]
            
            return category_list, 200
    
        except Exception as e:
            return{
                'error': str(e)
            }, 400
    
    def post(self):
        try:
            
            data = request.get_json()
            validate_data = CategorySchema.model_validate(data)
            
            create_category = category_service.create(validate_data)
            
            return create_category.to_json(), 201

        except ValidationError as e:
            return{
                'error':e.errors()
            }, 400
        
        except Exception as e:
            return{
                'error': str(e)
            }, 400
    

class ManageCategoryResource(Resource):
    
    def get(self, category_id: int):
        try:
            category = category_service.get_by_id(category_id)
            
            if not category:
                return {
                    'error': 'Category not found'
                }, 404
            
            return category.to_json(), 200
        
        except Exception as e:
            return {
                'error': str(e)
            }, 400
    
    def put(self, category_id: int):
        try:
            category = category_service.get_by_id(category_id)
            
            if not category:
                return {
                    'error': 'Category not found'
                }, 404
            
            data = request.get_json()
            validate_data = CategorySchema.model_validate(data)
            
            update_category = category_service.update(category, validate_data)
            
            return update_category.to_json(), 201
        
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
            
        except Exception as e:
            return {
                'error': str(e)
            }, 400
    
    def delete(self, category_id: int):
        try:
            category = category_service.get_by_id(category_id)
            
            if not category:
                return {
                    'error': 'Category not found'
                }, 404
            
            category_service.delete(category)
            
            return {"message": "Category deleted successfully"}, 200
        
        except Exception as e:
            return {
                'error': str(e)
            }, 400
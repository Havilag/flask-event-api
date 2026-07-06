from flask_restful import Resource
from app.schemas.event_schema import EventSchema
from app.services.event_service import event_service
from flask import request
from pydantic import ValidationError


class EventResource(Resource):
    
    def get(self):
        try:
            events = event_service.get_all()
            event_list = [event.to_json() for event in events]
            
            return event_list, 200
        
        except Exception as e:
            return {
                'error': str(e)
            }, 400
    
    def post(self):
        
        try:
            data = request.get_json()
            validate_data = EventSchema.model_validate(data)
            
            create_event = event_service.create(validate_data)
            
            return create_event.to_json(), 201
        
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 400
        

class ManageEventResource(Resource):
    
    def get(self, event_id: int):
        try:
            event = event_service.get_by_id(event_id)
            
            if not event:
                return {
                    'error': 'Event not found'
                }, 404
            
            return event.to_json(), 200
        
        except Exception as e:
            return {
                'error': str(e)
            }, 400
    
    def put(self, event_id: int):
        try:
            event = event_service.get_by_id(event_id)
            
            if not event:
                return {
                    'error': 'Event not found'
                }, 404
            
            data = request.get_json()
            validate_data = EventSchema.model_validate(data)
            
            event_update = event_service.update(event, validate_data)
            
            return event_update.to_json(), 200
        
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
            
        except Exception as e:
            return {
                'error': str(e)
            }, 400
    
    def delete(self, event_id: int):
        try:
            event = event_service.get_by_id(event_id)
            
            if not event:
                return {
                    'error': 'Event not found'
                }, 404
            
            event_service.delete(event)
            
            return {"message": "Event deleted successfully"}, 200
        
        except Exception as e:
            return {
                'error': str(e)
            }, 400
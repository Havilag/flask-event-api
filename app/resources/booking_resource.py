from flask_restful import Resource
from app.schemas.booking_schema import BookingSchema
from app.services.booking_service import booking_service
from app.services.event_service import event_service
from flask import request
from pydantic import ValidationError
from db import db


class BookingResource(Resource):
    
    def get(self):
        try:
            bookings = booking_service.get_all()
            
            booking_list = [booking.to_json() for booking in bookings]
            
            return booking_list, 200
        
        except Exception as e:
            return{
                'error': str(e)
            }, 400
    
    def post(self):
        try:
            data = request.get_json()
            validate_data = BookingSchema.model_validate(data)
            
            event = event_service.get_by_id(validate_data.event_id)
            
            if not event:
                raise Exception("The selected event does not exist")
            
            if event.available_tickets < validate_data.ticket_quantity:
                raise Exception(f"Insufficient stock. Only {event.available_tickets} tickets left")
            
            event.available_tickets -= validate_data.ticket_quantity
            
            create_booking = booking_service.create(
                user_id=validate_data.user_id,
                event_id=validate_data.event_id,
                ticket_quantity=validate_data.ticket_quantity,
                booking_date=validate_data.booking_date,
                total_amount=validate_data.total_amount,
                status=validate_data.status
            )
            
            db.session.commit()
            
            return create_booking.to_json(), 201
        
        except ValidationError as e:
            return{
                'error':e.errors()
            }, 400
        
        except Exception as e:
            db.session.rollback()
            return{
                'error': str(e)
            }, 400
    
    
class ManageBookingResource(Resource):
    
    def get(self, booking_id: int):
        try:
            booking = booking_service.get_by_id(booking_id)
            
            if not booking:
                return {
                    'error': 'Booking not found'
                }, 404
            
            return booking.to_json(), 200

        except Exception as e:
            return{
                'error': str(e)
            }, 400
    
    def put(self, booking_id: int):
        try:
            booking = booking_service.get_by_id(booking_id)
            
            if not booking:
                return {
                    'error': 'Booking not found'
                }, 404
            
            data = request.get_json()
            validate_data = BookingSchema.model_validate(data)
            
            update_booking = booking_service.update(booking, validate_data)
            db.session.commit()
            
            return update_booking.to_json(), 200
        
        except ValidationError as e:
            return{
                'error':e.errors()
            }, 400
        
        except Exception as e:
            db.session.rollback()
            return{
                'error': str(e)
            }, 400
    
    
    def delete(self, booking_id: int):
        try:
            booking = booking_service.get_by_id(booking_id)
            
            if not booking:
                return {
                    'error': 'Booking not found'
                }, 404
            
            event = event_service.get_by_id(booking.event_id)
            
            if event:
                event.available_tickets += booking.ticket_quantity
            
            booking_service.delete(booking)
            db.session.commit()
            
            return {"message": "Reservation successfully cancelled and tickets returned to stock"}, 200
        
        except Exception as e:
            db.session.rollback()
            return {
                'error': str(e)
            }, 400
    
    
            
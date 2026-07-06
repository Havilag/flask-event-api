from app.models.booking_model import Booking
from app.schemas.booking_schema import BookingSchema
from db import db


class BookingService:
    
    def get_all(self):
        return Booking.query.all()
    
    def get_by_id(self, id: int) -> Booking | None:
        booking = Booking.query.filter_by(
            id=id
        ).first()
        
        return booking
    
    def create(self, user_id: int, event_id: int, ticket_quantity: int, booking_date: str, total_amount: float, status: str) -> Booking:
        booking = Booking (
            booking_date = booking_date,
            ticket_quantity = ticket_quantity,
            total_amount = total_amount,
            status = status,
            user_id = user_id,
            event_id =event_id
        )
        
        db.session.add(booking)
        
        
        return booking
    
    def update(self, booking: Booking, data: BookingSchema):
        booking.booking_date = data.booking_date
        booking.ticket_quantity = data.ticket_quantity
        booking.total_amount = data.total_amount
        booking.status = data.status
        booking.user_id = data.user_id
        booking.event_id = data.event_id
        
        
        return booking
    
    def delete(self, booking:Booking) -> None:
        booking.status = 'cancelled'
        

booking_service = BookingService()
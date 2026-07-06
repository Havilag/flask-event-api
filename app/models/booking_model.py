from db import db
from sqlalchemy import Integer, String, Text, DECIMAL, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


class Booking(db.Model):
    __tablename__ = 'bookings'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True)
    booking_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    ticket_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    total_amount: Mapped[float] = mapped_column(DECIMAL(10,4), nullable=False)
    status: Mapped[str] = mapped_column(String(50), default='PENDING')
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    event_id: Mapped[int] = mapped_column(Integer, ForeignKey('events.id'), nullable=False)
    
    
    def to_json(self):
        return{
            'id': self.id,
            'booking_date': str(self.booking_date),
            'ticket_quantity': self.ticket_quantity,
            'total_amount': float(self.total_amount),
            'status': self.status,
            'user_id': self.user_id,
            'event_id': self.event_id
        }
    
    
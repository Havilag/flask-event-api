from sqlalchemy import Integer, String, Text, DECIMAL, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import db
from datetime import datetime

class Event(db.Model):
    __tablename__ = 'events'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    location:  Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[float] = mapped_column(DECIMAL(10,4), nullable=False)
    max_capacity: Mapped[int] = mapped_column(Integer, nullable=False)
    available_tickets: Mapped[int] = mapped_column(Integer, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey('categories.id'), nullable=False)
    
    
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'date': str(self.date),
            'location':  self.location,
            'price': float(self.price),
            'max_capacity': self.max_capacity,
            'available_tickets': self.available_tickets,
            'is_active': self.is_active,
            'category_id': self.category_id
            }
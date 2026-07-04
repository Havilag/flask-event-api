from app.models.event_model import Event
from app.schemas.event_schema import EventSchema
from db import db


class EventService:
    
    def get_all(self):
        return Event.query.filter_by(is_active=True).all()
    
    def get_by_id(self, id: int) -> Event | None:
        event = Event.query.filter_by(
            id=id,
            is_active=True
        ).first()
        
        return event

    def create(self, data:EventSchema) -> Event:
        event = Event(
            title = data.title,
            description = data.description,
            date = data.date,
            location = data.location,
            price = data.price,
            max_capacity = data.max_capacity,
            available_tickets = data.max_capacity,
            is_active = data.is_active,
            category_id = data.category_id
        )
        
        db.session.add(event)
        db.session.commit()
        return event

    def update(self, event: Event, data: EventSchema):
        event.title = data.title
        event.description = data.description
        event.date = data.date
        event.location = data.location
        event.price = data.price
        event.max_capacity = data.max_capacity
        event.available_tickets = data.available_tickets
        event.is_active = data.is_active
        event.category_id = data.category_id
        
        db.session.commit()
        return event
    
    def delete(self, event: Event) -> None:
        event.is_active = False
        db.session.commit()

event_service = EventService()
            
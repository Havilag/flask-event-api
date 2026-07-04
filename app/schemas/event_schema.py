from pydantic import BaseModel
from datetime import datetime

class EventSchema(BaseModel):
    title: str
    description: str
    date: datetime
    location: str
    price: int
    max_capacity: int
    available_tickets: int
    is_active: bool
    category_id: int
from pydantic import BaseModel
from datetime import datetime

class BookingSchema(BaseModel):
    booking_date: datetime
    ticket_quantity: int
    total_amount: float
    status: str
    user_id: int
    event_id: int
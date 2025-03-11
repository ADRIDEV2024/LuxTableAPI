from pydantic import BaseModel, Field
from datetime import datetime

class ReservationBase(BaseModel):
    user_id: int
    table_id: int
    reservation_time: datetime = Field(..., example="2024-06-01T19:00:00")

    @classmethod
    def validate_reservation_time(cls, value):
        if value < datetime.utcnow():
            raise ValueError("Reservation time must be in the future")
        return value

class ReservationCreate(ReservationBase):
    pass

class ReservationResponse(ReservationBase):
    id: int
    status: str

    class Config:
        from_attributes = True

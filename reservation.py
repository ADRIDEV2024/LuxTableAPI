from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    table_id = Column(Integer, ForeignKey("tables.id"), nullable=False)
    reservation_time = Column(DateTime, nullable=False)
    status = Column(String, default="pending")

    user = relationship("User", back_populates="reservations")
    table = relationship("Table", back_populates="reservations")
    
    __table_args__ = (Index("idx_reservations_time", "reservation_time"),)

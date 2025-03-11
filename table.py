from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base

class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, index=True)
    capacity = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)

    reservations = relationship("Reservation", back_populates="table")
    
    __table_args__ = (Index("idx_tables_available", "available"),)
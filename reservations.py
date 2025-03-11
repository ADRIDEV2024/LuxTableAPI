from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.reservation import ReservationCreate, ReservationResponse
from app.services.reservation_service import create_reservation, get_reservation, cancel_reservation
from app.core.database import get_db
from app.core.security import get_current_user

router = APIRouter(prefix="/reservations", tags=["Reservations"])

@router.post("/", response_model=ReservationResponse)
def make_reservation(reservation: ReservationCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return create_reservation(db, user, reservation)

@router.get("/{reservation_id}", response_model=ReservationResponse)
def get_reservation_details(reservation_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    reservation = get_reservation(db, user, reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation

@router.delete("/{reservation_id}")
def cancel_reservation_route(reservation_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return cancel_reservation(db, user, reservation_id)

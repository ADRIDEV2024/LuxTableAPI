from sqlalchemy.orm import Session
from app.models.reservation import Reservation
from app.schemas.reservation import ReservationCreate
from app.core.exceptions import ReservationNotFoundException
from app.websockets.notifications import notify_clients
from datetime import datetime

def create_reservation(db: Session, user, reservation_data: ReservationCreate):
    existing_reservation = db.query(Reservation).filter(
        Reservation.table_id == reservation_data.table_id,
        Reservation.reservation_time == reservation_data.reservation_time
    ).first()

    if existing_reservation:
        return {"error": "Table already reserved at this time"}

    reservation = Reservation(
        user_id=user["id"], 
        table_id=reservation_data.table_id, 
        reservation_time=reservation_data.reservation_time,
        status="confirmed"
    )
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    await notify_clients(f"New reservation: {reservation.id} for table {reservation.table_id}")
    return reservation

def get_reservation(db: Session, user, reservation_id: int):
    reservation = db.query(Reservation).filter(Reservation.id == reservation_id, Reservation.user_id == user["id"]).first()

    if not reservation:
        raise ReservationNotFoundException()
    return reservation

def get_user_reservations(db: Session, user_id: int):
    user_reservation = db.query(Reservation).filter(Reservation.user_id == user_id).all()

    if not user_reservation:
        raise ReservationNotFoundException()
    return user_reservation

def update_reservation(db: Session, user, reservation_id: int, new_time: datetime):
    reservation = get_reservation(db, user, reservation_id)
    if reservation:
        reservation.reservation_time = new_time
        db.commit()
        db.refresh(reservation)
        return reservation
    return {"error": "Reservation not found"}

def cancel_reservation(db: Session, user, reservation_id: int):
    reservation = get_reservation(db, user, reservation_id)
    if reservation:
        db.delete(reservation)
        db.commit()
        await notify_clients(f"Reservation {reservation.id} has been canceled")
        return {"message": "Reservation canceled"}
    return {"error": "Reservation not found"}


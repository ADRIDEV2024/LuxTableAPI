from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user, get_user_profile
from app.core.database import get_db
from app.core.security import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/me", response_model=UserResponse)
def get_profile(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_user_profile(db, user)

from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import verify_password
from app.core.exceptions import UnauthorizedAccessException
from app.schemas.user import UserResponse

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if user and verify_password(password, user.hashed_password):
        return user
    raise UnauthorizedAccessException()

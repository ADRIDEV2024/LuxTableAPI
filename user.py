from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, regex="^[A-Za-z ]+$")
    email: EmailStr = Field(..., example="user@example.com")

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=100, example="StrongPass123!")

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

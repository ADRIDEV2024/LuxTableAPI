from pydantic import BaseModel, Field

class TableBase(BaseModel):
    capacity: int = Field(..., ge=1, le=6, example=4)
    available: bool = Field(default=True)

class TableCreate(TableBase):
    pass

class TableResponse(TableBase):
    id: int

    class Config:
        from_attributes = True

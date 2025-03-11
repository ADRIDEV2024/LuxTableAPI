from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.table import TableCreate, TableResponse
from app.services.table_service import create_table, get_all_tables
from app.core.database import get_db

router = APIRouter(prefix="/tables", tags=["Tables"])

@router.post("/", response_model=TableResponse)
def add_table(table: TableCreate, db: Session = Depends(get_db)):
    return create_table(db, table)

@router.get("/", response_model=list[TableResponse])
def list_tables(db: Session = Depends(get_db)):
    return get_all_tables(db)

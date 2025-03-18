from sqlalchemy.orm import Session
from app.models.table import Table
from app.schemas.table import TableCreate
from app.core.exceptions import TableNotFoundException, TableUnavailableException

def create_table(db: Session, table_data: TableCreate):
    table = Table(capacity=table_data.capacity, available=table_data.available)
    db.add(table)
    db.commit()
    db.refresh(table)
    return table

def get_all_tables(db: Session):
    table = db.query(Table).all()
    if not table:
        raise TableNotFoundException()
    return table

def get_table_by_id(db: Session, table_id: int):
    table_by_id = db.query(Table).filter(Table.id == table_id).first()
    if not table_by_id:
        raise TableNotFoundException()
    return table_by_id

def update_table_availability(db: Session, table_id: int, available: bool):
    table = get_table_by_id(db, table_id)
    if table:
        table.available = available
        db.commit()
        db.refresh(table)
        return table
    return {"error": "Table not found"}

def get_available_tables(db: Session):
    available_table = db.query(Table).filter(Table.available == True).all()
    if not available_table:
        raise TableUnavailableException()
    return available_table

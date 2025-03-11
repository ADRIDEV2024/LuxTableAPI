from fastapi import HTTPException

class UserNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="User not found")

class ReservationNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Reservation not found")

class TableUnavailableException(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Table is already reserved at this time")
        
class TableNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Table not found")

class UnauthorizedAccessException(HTTPException):
    def __init__(self):
        super().__init__(status_code=403, detail="Unauthorized access")

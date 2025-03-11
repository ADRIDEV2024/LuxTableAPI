from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
import traceback

def global_error_handler(app: FastAPI):
    @app.middleware("http")
    async def error_handling_middleware(request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            traceback.print_exc()  # Para debugging
            return JSONResponse(
                status_code=500,
                content={"status": "error", "message": "Internal Server Error"}
            )

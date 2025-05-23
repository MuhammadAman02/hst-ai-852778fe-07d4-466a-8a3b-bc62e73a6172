from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from typing import Any, Dict, Optional

class AppError(Exception):
    """Base application exception class."""
    
    def __init__(
        self, 
        message: str, 
        status_code: int = 500, 
        details: Optional[Dict[str, Any]] = None
    ):
        self.message = message
        self.status_code = status_code
        self.details = details or {}
        super().__init__(self.message)

def register_exception_handlers(app: FastAPI) -> None:
    """
    Register exception handlers for the application.
    
    Args:
        app: The FastAPI application instance
    """
    
    @app.exception_handler(AppError)
    async def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
        """Handle application-specific errors."""
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": exc.__class__.__name__,
                "message": exc.message,
                "details": exc.details,
            },
        )
    
    @app.exception_handler(Exception)
    async def generic_error_handler(request: Request, exc: Exception) -> JSONResponse:
        """Handle any unhandled exceptions."""
        return JSONResponse(
            status_code=500,
            content={
                "error": "InternalServerError",
                "message": "An unexpected error occurred",
                "details": {"error_type": exc.__class__.__name__},
            },
        )
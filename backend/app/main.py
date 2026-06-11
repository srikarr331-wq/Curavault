"""FastAPI Application Entry Point"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config import get_settings

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    # Startup
    print(f"🚀 Starting {settings.app_name} v{settings.app_version}")
    print(f"📍 Environment: {settings.environment}")
    yield
    # Shutdown
    print(f"🛑 Shutting down {settings.app_name}")


app = FastAPI(
    title=settings.app_name,
    description="Patient-Owned Digital Healthcare Wallet",
    version=settings.app_version,
    lifespan=lifespan,
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=settings.cors_allow_credentials,
    allow_methods=settings.cors_allow_methods,
    allow_headers=settings.cors_allow_headers,
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": f"Welcome to {settings.app_name}",
        "version": settings.app_version,
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": settings.app_version,
    }


@app.get("/api/v1")
async def api_info():
    """API v1 information"""
    return {
        "api_version": "v1",
        "service": settings.app_name,
        "endpoints": {
            "auth": "/api/v1/auth",
            "reports": "/api/v1/reports",
            "prescriptions": "/api/v1/prescriptions",
            "profile": "/api/v1/profile",
            "doctor": "/api/v1/doctor",
            "admin": "/api/v1/admin",
        },
    }


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """Global exception handler"""
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error",
            "error_type": type(exc).__name__,
        },
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
    )

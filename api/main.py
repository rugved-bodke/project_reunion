from fastapi import FastAPI
from database.db import get_db_sync

def _get_app():
    app = FastAPI(
        title="Social Media Platform",
        description="A social media platform for users to share their thoughts and ideas.",
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )
    from api.routers import router as api_router

    app.include_router(api_router)


    @app.get("/check_db")
    async def check_db():
        return {"message": f"{next(get_db_sync())} ! Database is connected"}

    return app

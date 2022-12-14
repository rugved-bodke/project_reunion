from fastapi import APIRouter
from .users import router as users_router
from .posts import router as posts_router
from .comments import router as comments_router
from .likes import router as likes_router
from .follow import router as follows_router
from .authenticate import router as auth_router

router = APIRouter(prefix="/api", tags=["API's"])
router.include_router(users_router)
router.include_router(posts_router)
router.include_router(comments_router)
router.include_router(likes_router)
router.include_router(follows_router)
router.include_router(auth_router)

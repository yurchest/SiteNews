from fastapi import APIRouter
from . import news, auth

router = APIRouter(
    prefix='/api',
)
router.include_router(news.router)
router.include_router(auth.router)

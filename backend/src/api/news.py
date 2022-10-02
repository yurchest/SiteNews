from typing import List
from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)

from .. import models
from ..database import Session, get_session
from ..services.news import NewsService

router = APIRouter(
    prefix='/news',
    tags=['news']
)


@router.get('/', response_model=List[models.News])
async def get_news_all(
        service: NewsService = Depends(),
):
    return await service.get_list()


@router.get('/{news_id}', response_model=models.News)
async def get_news(
        news_id: int,
        service: NewsService = Depends(),
):
    return await service.get(news_id)


@router.post('/', response_model=models.News)
async def create_news(
        news_data: models.NewsCreate,
        service: NewsService = Depends(),
):
    return await service.create(news_data)


@router.delete('/{news_id}')
async def delete_news(
        news_id: int,
        service: NewsService = Depends(),
):
    await service.delete(news_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

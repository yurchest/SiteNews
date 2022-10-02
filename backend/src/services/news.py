from typing import List, Dict

from fastapi import Depends, HTTPException
from starlette import status
from .. import tables
from src.database import get_session, Session
from .. import models


class NewsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    async def _get(self, news_id: int) -> tables.News:
        news = (
            self.session
            .query(tables.News)
            .filter_by(id=news_id)
            .first()
        )
        if not news:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return news

    async def get_list(self) -> List[tables.News]:
        return self.session.query(tables.News).all()

    async def get(self, news_id: int) -> tables.News:
        return await self._get(news_id)

    async def create(self, news_data: models.NewsCreate) -> tables.News:
        news = tables.News(**news_data.dict())
        print(news)
        self.session.add(news)
        self.session.commit()
        return news

    async def create_many(self, news_data: List[models.NewsCreate | Dict]) -> List[tables.News]:
        news = [
            (tables.News(**post)) for post in news_data
        ]
        self.session.add_all(news)
        self.session.commit()
        return news

    async def delete(self, news_id: int):
        news = await self._get(news_id)
        self.session.delete(news)
        self.session.commit()



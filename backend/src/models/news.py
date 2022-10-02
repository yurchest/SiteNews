from pydantic import BaseModel
from datetime import datetime


class BaseNews(BaseModel):
    content: str
    url: str


class News(BaseNews):
    time_create: datetime
    time_update: datetime
    id: int

    class Config:
        orm_mode = True


class NewsCreate(BaseNews):
    pass


class NewsUpdate(BaseNews):
    pass

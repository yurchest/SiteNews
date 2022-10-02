from datetime import datetime
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, Depends
from fastapi_utils.tasks import repeat_every
from starlette.background import BackgroundTasks

from . import api
from .utils.parse_news import parse_and_update_db

app = FastAPI()


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def root():
    return ({'ABOBA': '228'})


@app.on_event("startup")
@repeat_every(seconds=30)
async def repeat_parse_news():
    await parse_and_update_db()


app.include_router(api.router)

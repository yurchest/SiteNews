from datetime import datetime

import requests
from bs4 import BeautifulSoup as bs

from src import tables
from src.database import Session


async def parse_and_update_db():
    service = Session()
    news_page = await parse_news('https://ria.ru/lenta/')
    news = []
    for post in news_page:
        if not service.query(tables.News).filter_by(url=post['url']).first():
            print("FOUND NEW POST   " + str(datetime.now()))
            news.append(tables.News(**post))
    service.add_all(news)
    service.commit()


async def parse_news(url):
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    news_content = soup.find_all('a', class_='list-item__title color-font-hover-only')
    result = []
    for news in news_content:
        href = news.get('href')
        content = news.text
        result.append({'content': news.text, 'url': news.get('href')})
    return result

from fastapi import APIRouter
from app.services.news_service import search_news

router = APIRouter()

@router.get("/news")
def news(keyword: str):
    return search_news(keyword)
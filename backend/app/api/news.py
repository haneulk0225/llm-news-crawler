from fastapi import APIRouter

router = APIRouter()

@router.get("/news")
def news(keyword: str):
    return {
        "keyword": keyword,
        "message": f"'{keyword}' 뉴스를 검색합니다."
    }
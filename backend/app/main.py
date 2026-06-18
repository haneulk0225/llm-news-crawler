from fastapi import FastAPI

app = FastAPI(
    title="AI News Agent",
    version="0.1.0"
)

@app.get("/")
def home():
        return {
            "message": "AI News Agent API Server"
        }

@app.get("/health")
def health():
    return {
        "status": "Ok",
        "version": "0.1.0"
    }

@app.get("/news")
def news(keyword: str):
    return {
        "keyword": keyword,
        "message": f"'{keyword} 뉴스를 검색합니다."
    }
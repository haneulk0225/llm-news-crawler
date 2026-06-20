from fastapi import FastAPI
from app.api.news import router as news_router

app = FastAPI(
    title="AI News Agent",
    version="0.1.0"
)

app.include_router(news_router)

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

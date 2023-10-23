from fastapi import FastAPI
from routers import stock_router


app = FastAPI()

app.include_router(stock_router, prefix="/stocks", tags=["stocks"])


@app.get("/")
def root():
    return {"message": "You hit the root path!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

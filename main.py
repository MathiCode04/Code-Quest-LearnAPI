from fastapi import FastAPI

app = FastAPI()


@app.get("/health", status_code=200)
async def root():
    return {
        "status": "ok",
        "message": "Code-Quest learning API is running successfully"
    }

@app.get("/daily-challange", status_code=200)
async def daily_challange():
    return {
        "status": "ok",
    }
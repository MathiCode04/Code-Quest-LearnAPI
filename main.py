from fastapi import FastAPI

from service.quest_picker import get_quest
app = FastAPI()


@app.get("/health", status_code=200)
async def root():
    return {
        "status": "ok",
        "message": "Code-Quest learning API is running successfully"
    }

@app.get("/daily-quest", status_code=200)
async def daily_quest():
    return get_quest()


from fastapi import FastAPI

from api.routers import penguin_avg
from .routers import penguin

app = FastAPI()

app.include_router(penguin.router)
app.include_router(penguin_avg.router)

@app.get("/")
def test():
    return {"message": "Test OK"}
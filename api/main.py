from fastapi import FastAPI
from .routers import penguin

app = FastAPI()

app.include_router(penguin.router)

@app.get("/")
def test():
    return {"message": "Test OK"}
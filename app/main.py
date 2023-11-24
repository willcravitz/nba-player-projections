from contextlib import asynccontextmanager
from fastapi import FastAPI

from .db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    
app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"message": "Hello World"}
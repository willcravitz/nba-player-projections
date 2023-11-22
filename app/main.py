from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    
app = FastAPI(lifespan=lifespan)
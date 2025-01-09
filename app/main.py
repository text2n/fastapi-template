from fastapi import  FastAPI

from .core.config import settings
from .routers import heros
from app.core.logger import logger

app = FastAPI()
app.include_router(heros.router)


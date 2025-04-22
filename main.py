from fastapi import FastAPI
from app.routes import freight_router

app = FastAPI()

app.include_router(freight_router)

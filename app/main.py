from fastapi import FastAPI
from app.routes import api

app = FastAPI(title="Inventory API")
app.include_router(api.router)

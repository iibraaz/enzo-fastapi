from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Enzo API", version="1.0")
app.include_router(router)
from fastapi import FastAPI
from app.routes import router
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

app = FastAPI(title="Enzo API", version="1.0")
app.include_router(router)
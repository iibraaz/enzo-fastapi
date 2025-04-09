from fastapi import APIRouter
from pydantic import BaseModel
from services.synthesizer import Synthesizer
from database.vector_store import VectorStore
from app.utils import generate_narration, embed_and_store

router = APIRouter()
vec = VectorStore()

class Question(BaseModel):
    question: str

class DataRow(BaseModel):
    data: dict

@router.post("/ask")
async def ask_endpoint(payload: Question):
    context = vec.search(payload.question, limit=3)
    response = Synthesizer.generate_response(question=payload.question, context=context)
    return {"answer": response.answer}

@router.post("/narrate")
async def narrate_endpoint(payload: DataRow):
    narration = await generate_narration(payload.data)
    await embed_and_store(narration, metadata={"source": "user_upload"})
    return {"narration": narration}
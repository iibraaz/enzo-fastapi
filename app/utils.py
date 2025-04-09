import openai
from uuid import uuid4
from database.vector_store import VectorStore

vec = VectorStore()

async def generate_narration(data: dict) -> str:
    prompt = f"Convert the following data into a human-readable summary:\n\n{data}"
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return res['choices'][0]['message']['content']

async def embed_and_store(text: str, metadata: dict):
    embedding = vec.get_embedding(text)
    vec.upsert_single({
        "id": str(uuid4()),
        "contents": text,
        "embedding": embedding,
        "metadata": metadata
    })
from fastapi import APIRouter, Request
# from .database import messages_collection
# from .redis_client import redis_client
from .rag_machine import get_qa_chain
from pathlib import Path

router = APIRouter()
pdf_path = Path(__file__).resolve().parent.parent / "sample_doc.pdf"
qa_chain = get_qa_chain(str(pdf_path))

@router.get("/ping")
async def ping():
    return {"message": "pong"}

@router.post("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        user_message = data.get("message")

        if not user_message:
            return {"error": "No message provided"}

        # messages_collection.insert_one({"sender": "user", "message": user_message})
        # redis_client.lpush("chat_history", user_message)
        # redis_client.ltrim("chat_history", 0, 9)
        
        ai_response = qa_chain.run(user_message)

        # messages_collection.insert_one({"sender": "ai", "message": ai_response})
        return {"response": ai_response}
    except Exception as e:
        return {"error": str(e)}

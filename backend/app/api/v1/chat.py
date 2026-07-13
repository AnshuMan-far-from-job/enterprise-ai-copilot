from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.llm_service import llm_service
from app.core.logger import logger

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        logger.info(f"Received message: {request.message}")
        
        user_id = "user_1"
        
        response = llm_service.generate_response(
            user_id,
            request.message
        )

        logger.info("Response generated successfully")
        
        return ChatResponse(
            response=response
        )
        
        
        
    except Exception as e:
        import traceback

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
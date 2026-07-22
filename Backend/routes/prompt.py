from fastapi import APIRouter, HTTPException
from models.prompt_model import PromptRequest
from models.response_model import PromptResponse
from services.prompt_detector import detect_prompt
from utils.logger import logger

router = APIRouter()

@router.post("/prompt", response_model=PromptResponse)
def check_prompt(request: PromptRequest):

    logger.info("Prompt analysis request received")

    if not request.text.strip():
        logger.warning("Empty or whitespace-only input received")
        raise HTTPException(
            status_code=400,
            detail="Input cannot be empty or only spaces."
        )

    result = detect_prompt(request.text)

    logger.info(
        f"Analysis completed | Risk: {result['risk']} | Confidence: {result['confidence']}"
    )

    return result
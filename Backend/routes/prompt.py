print("LOADED NEW PROMPT ROUTE")

from fastapi import APIRouter, HTTPException
from models.prompt_model import PromptRequest
from services.prompt_detector import detect_prompt
from utils.logger import logger

router = APIRouter()

@router.post("/prompt")
def check_prompt(request: PromptRequest):

    logger.info("Prompt analysis request received")

    if not request.text or not request.text.strip():
        logger.warning("Empty or whitespace-only input received")
        raise HTTPException(
            status_code=400,
            detail="Input cannot be empty or only spaces."
        )

    result = detect_prompt(request.text)

    logger.info(
        f"Analysis completed | Risk: {result.get('risk')} | Confidence: {result.get('confidence')}"
    )

    return result

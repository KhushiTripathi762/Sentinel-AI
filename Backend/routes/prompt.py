<<<<<<< HEAD
from fastapi import APIRouter, HTTPException
from models.prompt_model import PromptRequest
from models.response_model import PromptResponse
=======
print("LOADED NEW PROMPT ROUTE")

from fastapi import APIRouter, HTTPException
from models.prompt_model import PromptRequest
>>>>>>> frontend
from services.prompt_detector import detect_prompt
from utils.logger import logger

router = APIRouter()

<<<<<<< HEAD
@router.post("/prompt", response_model=PromptResponse)
=======
@router.post("/prompt")
>>>>>>> frontend
def check_prompt(request: PromptRequest):

    logger.info("Prompt analysis request received")

<<<<<<< HEAD
    if not request.text.strip():
=======
    if not request.text or not request.text.strip():
>>>>>>> frontend
        logger.warning("Empty or whitespace-only input received")
        raise HTTPException(
            status_code=400,
            detail="Input cannot be empty or only spaces."
        )

    result = detect_prompt(request.text)

    logger.info(
<<<<<<< HEAD
        f"Analysis completed | Risk: {result['risk']} | Confidence: {result['confidence']}"
    )

    return result
=======
        f"Analysis completed | Risk: {result.get('risk')} | Confidence: {result.get('confidence')}"
    )

    return result
>>>>>>> frontend

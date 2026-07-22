from fastapi import APIRouter, HTTPException
from models.prompt_model import PromptRequest
from models.response_model import PromptResponse
from services.prompt_detector import detect_prompt

router = APIRouter()

@router.post("/prompt", response_model=PromptResponse)
def check_prompt(request: PromptRequest):

    if not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Input cannot be empty or only spaces."
        )

    return detect_prompt(request.text)
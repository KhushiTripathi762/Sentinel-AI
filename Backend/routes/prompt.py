print("LOADED NEW PROMPT ROUTE")

from fastapi import APIRouter
from models.prompt_model import PromptRequest
from services.prompt_detector import detect_prompt

router = APIRouter()

@router.post("/prompt")
def check_prompt(request: PromptRequest):
    return detect_prompt(request.prompt)
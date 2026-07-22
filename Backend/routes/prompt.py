from fastapi import APIRouter
from models.prompt_model import PromptRequest
from models.response_model import PromptResponse
from services.prompt_detector import detect_prompt

print("LOADED NEW PROMPT ROUTE")

router = APIRouter()

@router.post("/prompt", response_model=PromptResponse)
def check_prompt(request: PromptRequest):
    return detect_prompt(request.prompt)
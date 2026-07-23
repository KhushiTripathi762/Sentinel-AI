from fastapi import APIRouter
from pydantic import BaseModel
from services.prompt_detector import detect_prompt

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/prompt")
def check_prompt(data: PromptRequest):
    return detect_prompt(data.prompt)
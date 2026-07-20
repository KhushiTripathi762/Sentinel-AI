from fastapi import APIRouter
from services.prompt_detector import detect_prompt

router = APIRouter()

@router.post("/prompt")
def check_prompt(text: str):
    return detect_prompt(text)
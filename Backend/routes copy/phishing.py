from fastapi import APIRouter
from services.phishing_detector import detect_phishing

router = APIRouter()

@router.post("/phishing")
def check_url(url: str):
    return detect_phishing(url)
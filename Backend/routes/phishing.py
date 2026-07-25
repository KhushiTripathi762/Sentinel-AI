from fastapi import APIRouter
from pydantic import BaseModel
from services.phishing_detector import detect_phishing

router = APIRouter()

class URLRequest(BaseModel):
    url: str

@router.post("/phishing")
def check_url(data: URLRequest):
    return detect_phishing(data.url)
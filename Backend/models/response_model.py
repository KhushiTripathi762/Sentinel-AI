from pydantic import BaseModel
from typing import List


class PromptResponse(BaseModel):
    attack_type: str
    risk: str
    confidence: int
    matched_patterns: List[str]
    recommendation: str
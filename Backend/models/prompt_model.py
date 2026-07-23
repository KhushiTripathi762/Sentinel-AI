from pydantic import BaseModel, Field
from config import settings

class PromptRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=settings.MIN_INPUT_LENGTH,
        max_length=settings.MAX_INPUT_LENGTH,
        description="Text to analyze for prompt injection"
    )
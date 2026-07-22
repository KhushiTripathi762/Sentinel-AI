from pydantic import BaseModel, Field

class PromptRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=5,
        max_length=5000,
        description="Text to analyze for prompt injection"
    )
from fastapi import FastAPI

from routes.prompt import router as prompt_router
from routes.phishing import router as phishing_router
from exceptions.handlers import register_exception_handlers

app = FastAPI(
    title="Sentinel AI",
    description="AI-powered security backend for Prompt Injection and Phishing Detection.",
    version="1.0.0"
)

register_exception_handlers(app)

# Register Prompt API
app.include_router(prompt_router)

# Register Phishing API
app.include_router(phishing_router)

@app.get("/")
def home():
    return {"message": "Sentinel AI Running 🚀"}
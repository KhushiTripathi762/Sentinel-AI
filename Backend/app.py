from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.prompt import router as prompt_router
from routes.phishing import router as phishing_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prompt_router)
app.include_router(phishing_router)

@app.get("/")
def home():
    return {"message": "Sentinel AI Running 🚀"}
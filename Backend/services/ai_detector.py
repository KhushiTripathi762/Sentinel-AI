import os
import requests

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/Shomi28/PromptShield"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def analyze_text(text):

    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": text},
        timeout=60
    )

    response.raise_for_status()

    result = response.json()

    # HF inference returns nested list
    if isinstance(result, list) and len(result) > 0:
        if isinstance(result[0], list):
            predictions = result[0]
        else:
            predictions = result

        best = max(predictions, key=lambda x: x["score"])

        return {
            "label": best["label"].lower(),
            "score": round(best["score"] * 100, 2)
        }

    raise Exception(f"Unexpected HF response: {result}")
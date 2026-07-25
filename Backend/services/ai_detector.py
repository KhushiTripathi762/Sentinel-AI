import os
import requests

API_URL = "https://api-inference.huggingface.co/models/Shomi28/PromptShield"


def analyze_text(text: str):
    hf_token = os.getenv("HF_TOKEN")

    if not hf_token:
        raise RuntimeError("HF_TOKEN environment variable is not configured.")

    headers = {
        "Authorization": f"Bearer {hf_token}"
    }

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": text},
            timeout=60,
        )
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to connect to Hugging Face: {e}")

    if response.status_code != 200:
        raise RuntimeError(
            f"Hugging Face API error {response.status_code}: {response.text}"
        )

    result = response.json()

    if (
        isinstance(result, list)
        and len(result) > 0
    ):
        predictions = result[0] if isinstance(result[0], list) else result

        if not predictions:
            raise RuntimeError("Empty prediction returned from Hugging Face.")

        best = max(predictions, key=lambda x: x.get("score", 0))

        return {
            "label": str(best.get("label", "unknown")).lower(),
            "score": round(float(best.get("score", 0)) * 100, 2),
        }

    raise RuntimeError(f"Unexpected Hugging Face response: {result}")
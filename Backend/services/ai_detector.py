from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Shomi28/PromptShield"
)


def analyze_text(text):
    result = classifier(text)[0]

    return {
        "label": result["label"].lower(),
        "score": round(result["score"] * 100, 2)
    }
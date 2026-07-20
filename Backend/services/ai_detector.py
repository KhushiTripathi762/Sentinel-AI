from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="facebook/roberta-hate-speech-dynabench-r4-target"
)

def analyze_text(text):
    result = classifier(text)

    return {
        "label": result[0]["label"],
        "score": round(result[0]["score"] * 100, 2)
    }
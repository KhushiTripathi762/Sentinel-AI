from transformers import pipeline

classifier = None


def get_classifier():
    global classifier

    if classifier is None:
        classifier = pipeline(
            "text-classification",
            model="Shomi28/PromptShield"
        )

    return classifier


def analyze_text(text):

    model = get_classifier()

    result = model(text)[0]

    return {
        "label": result["label"].lower(),
        "score": round(result["score"] * 100, 2)
    }
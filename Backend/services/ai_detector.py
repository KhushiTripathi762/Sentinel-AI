patterns = {
    "ignore previous instructions": 100,
    "ignore all previous instructions": 100,
    "forget previous instructions": 90,
    "system prompt": 85,
    "reveal system prompt": 90,
    "developer mode": 75,
    "jailbreak": 90,
    "bypass": 70,
    "ignore safety": 80,
    "disable safety": 90,
    "act as": 50,
    "pretend to be": 50,
}


def analyze_text(text: str):
    text = text.lower()

    score = 0

    for pattern, weight in patterns.items():
        if pattern in text:
            score = max(score, weight)

    if score >= 50:
        label = "injection"
    else:
        label = "safe"

    return {
        "label": label,
        "score": score
    }
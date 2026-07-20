patterns = {
    "ignore previous instructions": 40,
    "ignore all previous instructions": 40,
    "system prompt": 30,
    "reveal system prompt": 30,
    "developer mode": 20,
    "jailbreak": 25,
    "bypass": 20,
    "forget previous instructions": 35
}

def detect_prompt(text):

    text = text.lower()

    confidence = 0
    matches = []

    for pattern, weight in patterns.items():

        if pattern in text:
            confidence += weight
            matches.append(pattern)

    if confidence > 100:
        confidence = 100

    if confidence >= 70:
        risk = "High"

    elif confidence >= 30:
        risk = "Medium"

    else:
        risk = "Low"

    recommendation = "Allow"

    if risk == "Medium":
        recommendation = "Review"

    if risk == "High":
        recommendation = "Block"

    return {
        "attack_type": "Prompt Injection",
        "risk": risk,
        "confidence": confidence,
        "matched_patterns": matches,
        "recommendation": recommendation
    }
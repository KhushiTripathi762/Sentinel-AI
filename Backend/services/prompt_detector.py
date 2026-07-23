from services.ai_detector import analyze_text

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

    ai_result = analyze_text(text)
    ai_label = ai_result["label"]
    ai_score = ai_result["score"]

    confidence = 0
    matches = []

    # Rule-based detection
    for pattern, weight in patterns.items():
        if pattern in text:
            confidence += weight
            matches.append(pattern)

    if confidence > 100:
        confidence = 100

    # ---------- AI + Rule Logic ----------

    if ai_label == "injection":
        confidence = max(confidence, int(ai_score))

    elif ai_label == "safe" and confidence == 0:
        confidence = 0

    # -------------------------------------

    if confidence >= 70:
        risk = "High"
    elif confidence >= 30:
        risk = "Medium"
    else:
        risk = "Low"

    if risk == "High":
        recommendation = "Block"
    elif risk == "Medium":
        recommendation = "Review"
    else:
        recommendation = "Allow"

    return {
        "attack_type": "Prompt Injection",
        "risk": risk,
        "confidence": confidence,
        "matched_patterns": matches,
        "recommendation": recommendation,
        "ai_analysis": ai_result
    }
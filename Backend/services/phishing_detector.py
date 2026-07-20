import re

keywords = [
    "login",
    "verify",
    "bank",
    "secure",
    "account",
    "update",
    "password"
]

def detect_phishing(url):

    score = 0
    reasons = []

    url = url.lower()

    # 1. Suspicious keywords
    for keyword in keywords:
        if keyword in url:
            score += 20
            reasons.append(f"Keyword detected: {keyword}")

    # 2. IP Address
    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        score += 30
        reasons.append("Uses IP Address")

    # 3. Long URL
    if len(url) > 60:
        score += 15
        reasons.append("Very Long URL")

    # 4. Too many dots
    if url.count(".") >= 4:
        score += 20
        reasons.append("Too many subdomains")

    if score > 100:
        score = 100

    if score >= 70:
        risk = "High"

    elif score >= 30:
        risk = "Medium"

    else:
        risk = "Low"

    recommendation = "Allow"

    if risk == "Medium":
        recommendation = "Review"

    if risk == "High":
        recommendation = "Block"

    return {
        "attack_type": "Phishing URL",
        "risk": risk,
        "confidence": score,
        "reasons": reasons,
        "recommendation": recommendation
    }
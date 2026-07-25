import re

keywords = [
    "login",
    "verify",
    "bank",
    "secure",
    "security",
    "account",
    "update",
    "password",
    "paypal",
    "amazon",
    "google",
    "microsoft",
    "apple",
    "signin"
]

trusted_domains = [
    "google.com",
    "github.com",
    "paypal.com",
    "amazon.com",
    "microsoft.com",
    "apple.com"
]


def detect_phishing(url):

    score = 0
    reasons = []

    url = url.lower()

    # Trusted domains
    for domain in trusted_domains:
        if domain in url:
            return {
                "attack_type": "Phishing URL",
                "risk": "Low",
                "confidence": 0,
                "reasons": ["Trusted Domain"],
                "recommendation": "Allow"
            }

    # Suspicious keywords
    for keyword in keywords:
        if keyword in url:
            score += 15
            reasons.append(f"Keyword detected: {keyword}")

    # IP Address
    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        score += 35
        reasons.append("Uses IP Address")

    # Long URL
    if len(url) > 60:
        score += 15
        reasons.append("Very Long URL")

    # Too many dots
    if url.count(".") >= 4:
        score += 20
        reasons.append("Too many subdomains")

    # Hyphens (common in phishing)
    if url.count("-") >= 2:
        score += 25
        reasons.append("Multiple hyphens")

    # Suspicious TLDs
    if url.endswith((".xyz", ".top", ".click", ".live", ".shop")):
        score += 25
        reasons.append("Suspicious top-level domain")

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
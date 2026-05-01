def should_escalate(text, score, request_type):
    text = text.lower()

    # High-risk keywords (financial / security issues)
    high_risk = [
        "fraud", "unauthorized", "hacked", "stolen",
        "charge", "charged", "transaction", "payment"
    ]

    # Immediate escalation for sensitive issues
    if any(k in text for k in high_risk):
        return True

    # Escalate if similarity is too low (not confident)
    if score < 0.25:
        return True

    # Escalate invalid / irrelevant queries
    if request_type == "invalid":
        return True

    return False
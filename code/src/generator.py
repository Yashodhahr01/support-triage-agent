def generate_response(doc, status):
    # Escalated case → safe response
    if status == "escalated":
        return "Your request requires further review by our support team."

    # Clean and shorten the response (optional polish)
    if doc:
        response = doc.strip()
        # Return only first sentence for cleaner output
        return response.split(".")[0] + "."

    return "No relevant information found."


def generate_justification(score, escalated, request_type):
    if escalated:
        return f"Escalated (low confidence or potential risk, score={score:.2f})"

    return f"Matched support document (score={score:.2f})"

def _confidence_label(score):
    if score >= 0.6:
        return "high"
    elif score >= 0.4:
        return "medium"
    else:
        return "low"


def generate_justification(score, escalated, request_type):
    conf = _confidence_label(score)
    if escalated:
        return f"Escalated (confidence={conf}, score={score:.2f})"
    return f"Matched support document (confidence={conf}, score={score:.2f})"
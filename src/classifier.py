def classify_request(text):
    text = text.lower()

    # Product issues (login, account, payments, help)
    if any(k in text for k in [
        "login", "account", "password",
        "how", "help", "can i",
        "payment", "card", "charge", "transaction"
    ]):
        return "product_issue"

    # Bug-related issues
    elif any(k in text for k in ["error", "bug", "not working", "failed", "issue"]):
        return "bug"

    # Feature requests
    elif any(k in text for k in ["feature", "add", "improve", "request"]):
        return "feature_request"

    else:
        return "invalid"


def classify_product_area(text, company):
    text = text.lower()

    if any(k in text for k in ["payment", "card", "transaction", "charge"]):
        return "payments"
    elif any(k in text for k in ["login", "account", "password"]):
        return "account_access"
    elif any(k in text for k in ["test", "submission", "assessment"]):
        return "assessments"
    else:
        return "general"
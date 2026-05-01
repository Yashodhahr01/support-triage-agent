def preprocess(issue, subject):
    issue = str(issue) if issue else ""
    subject = str(subject) if subject else ""
    
    text = (subject + " " + issue).lower().strip()
    return text
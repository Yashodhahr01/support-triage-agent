import pandas as pd
from preprocess import preprocess
from classifier import classify_request, classify_product_area
from retriever import retrieve
from decision import should_escalate
from generator import generate_response, generate_justification

df = pd.read_csv("../data/support_tickets.csv")

results = []

for _, row in df.iterrows():
    text = preprocess(row["issue"], row["subject"])
    
    request_type = classify_request(text)
    product_area = classify_product_area(text, row["company"])
    
    doc, score = retrieve(text)
    
    escalate = should_escalate(text, score, request_type)
    
    status = "escalated" if escalate else "replied"
    
    response = generate_response(doc, status)
    justification = generate_justification(score, escalate, request_type)
    
    results.append({
        "status": status,
        "product_area": product_area,
        "response": response,
        "justification": justification,
        "request_type": request_type
    })

output_df = pd.DataFrame(results)
output_df.to_csv("../output/output.csv", index=False)

print("✅ Done! Output saved to output/output.csv")
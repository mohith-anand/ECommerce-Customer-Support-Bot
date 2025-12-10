import os
from dotenv import load_dotenv
from google import genai

# Load Gemini API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

# Detailed system instruction
SYSTEM_INSTRUCTION = """
You are an expert ecommerce customer support assistant.
Help customers with orders, products, FAQs, returns, refunds, shipping, payments.

Rules:
1. Use the retrieved context as reference only. You may answer naturally.
2. Provide concise, polite guidance.
3. If information is missing, you may still give general advice.
4. Tone: friendly, professional, helpful.
5. Escalate if complaint or negative sentiment detected.
"""

def generate_response(user_query, retrieved_docs=None):
    if retrieved_docs:
        context_text = ""
        for doc in retrieved_docs:
            context_text += f"[Source: {doc['id']}] {doc['text']}\n"
        full_prompt = f"{SYSTEM_INSTRUCTION}\n\nContext:\n{context_text}\nUser question: {user_query}\nAnswer:"
    else:
        full_prompt = f"{SYSTEM_INSTRUCTION}\n\nUser question: {user_query}\nAnswer:"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )
    return response.text
# src/llm.py (add this at the bottom)
# src/llm.py
def classify_intent_sentiment(user_input):
    """
    Dummy intent and sentiment classifier.
    Returns: intent, sentiment, escalate
    """
    # Example simple rules; replace with actual model/classifier later
    if "return" in user_input.lower() or "refund" in user_input.lower():
        return "return_request", "negative", True
    elif "order" in user_input.lower():
        return "order_status", "neutral", False
    elif "wrong" in user_input.lower() or "defect" in user_input.lower():
        return "complaint", "negative", True
    else:
        return "general_query", "neutral", False

# app.py
import streamlit as st
from src.llm import generate_response, classify_intent_sentiment
from src.rag import retrieve
st.set_page_config(page_title="Ecommerce Chatbot", page_icon="🛒", layout="wide")
# CSS for chat bubbles
st.markdown("""
<style>
/* Customer bubble */
.customer {
    background-color: #0D47A1;  /* dark blue */
    color: white;               
    padding: 8px 12px;
    border-radius: 12px;
    margin-bottom: 5px;
    width: fit-content;
    max-width: 70%;
    float: right;
    clear: both;
}
/* Bot bubble */
.bot {
    background-color: #E0E0E0;  /* light gray */
    color: black;               
    padding: 8px 12px;
    border-radius: 12px;
    margin-bottom: 5px;
    width: fit-content;
    max-width: 70%;
    float: left;
    clear: both;
}
/* Clear floats */
.clearfix::after {
    content: "";
    clear: both;
    display: table;
}
</style>
""", unsafe_allow_html=True)
# Sidebar toggle
user_mode = st.sidebar.radio("Select mode:", ["Customer", "Agent"])
# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
st.title("🛒 Ecommerce Customer Support Chatbot")
st.write("Type your message and get instant responses!")
with st.form("user_input_form", clear_on_submit=True):
    user_input = st.text_input("Type your message here...", "")
    submitted = st.form_submit_button("Send")
    
if submitted and user_input:
    # Retrieve documents
    retrieved_docs_raw = retrieve(user_input, k=3)
    structured_docs = [{"id": f"doc_{i+1}", "text": d} for i, d in enumerate(retrieved_docs_raw)]
    
    # LLM response
    llm_response = generate_response(user_input, structured_docs)
    
    # Intent, sentiment, escalation
    intent, sentiment, escalate = classify_intent_sentiment(user_input)
    
    # Append message
    st.session_state.messages.append({
        "user": user_input,
        "response": llm_response,
        "intent": intent,
        "sentiment": sentiment,
        "escalate": escalate,
        "docs": structured_docs
    })
# Display chat messages
for chat in st.session_state.messages:
    # Customer bubble
    st.markdown(f'<div class="customer clearfix">You: {chat["user"]}</div>', unsafe_allow_html=True)
    
    # Bot bubble
    st.markdown(f'<div class="bot clearfix">Bot: {chat["response"]}</div>', unsafe_allow_html=True)
    
    if user_mode == "Agent":
        # Agent section: Columns + Collapsible documents
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        col1.info(f"**Intent:** {chat['intent']}")
        
        # Color-coded sentiment
        sentiment_lower = chat['sentiment'].lower()
        if 'positive' in sentiment_lower:
            col2.success(f"**Sentiment:** {chat['sentiment']}")
        elif 'negative' in sentiment_lower:
            col2.error(f"**Sentiment:** {chat['sentiment']}")
        else:
            col2.info(f"**Sentiment:** {chat['sentiment']}")
        
        col3.info(f"**Escalate:** {chat['escalate']}")
        
        with st.expander("Retrieved Documents", expanded=False):
            for doc in chat['docs']:
                st.markdown(f"[Source: {doc.get('id', 'unknown')}] {doc.get('text', '')}")
    else:
        # Customer view: Simple escalation warning
        if chat['escalate']:
            st.warning("⚠️ This issue may require escalation. Our support team will follow up.")

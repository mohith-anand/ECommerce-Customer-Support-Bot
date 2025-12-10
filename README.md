# Ecommerce Customer Support Chatbot

An AI-powered customer support chatbot built using RAG (Retrieval-Augmented Generation) + LLM, designed to handle complex customer queries like order tracking, cancellations, returns, and defective products.

## 📋 Overview

This system provides accurate, context-aware responses and includes features to support both end-users and supervising agents. The project demonstrates real-world AI deployment for customer support, showing how LLMs can be augmented with a knowledge base for precise, explainable answers.

## ✨ Features

### Customer Mode
- Simple, visually appealing chat interface
- Handles real-time queries with relevant responses
- Escalation suggestions for critical or unresolved issues
  
![image alt](https://github.com/mohith-anand/ECommerce-Customer-Support-Bot/blob/e9caefde61e80ec5ce65ae532d772d28f11c349a/Demo1.png)

### Agent Mode (Supervisor Mode)
- Displays intent, sentiment, and escalation status for each query
- Shows retrieved documents that informed the AI response
- Helps human agents oversee, validate, and intervene when necessary
- Provides context awareness for accurate support handling
  
![image alt](https://github.com/mohith-anand/ECommerce-Customer-Support-Bot/blob/e9caefde61e80ec5ce65ae532d772d28f11c349a/Demo2.png)

### AI & Retrieval
- Uses a Retrieval-Augmented Generation (RAG) pipeline for precise answers
- Integrates LLM with knowledge base documents to ensure response accuracy
- Intent classification and sentiment analysis improve automated escalation and context understanding

## 🛠️ Tech Stack

- **Python** - Core programming language
- **Streamlit** - UI framework
- **FAISS** - Vector-based retrieval
- **LLM** - Generative responses
- **Pandas** - Data handling
- **GitHub** - Version control

## 📁 Project Structure

```
customer-support-bot/
├── app.py                         # Main Streamlit chatbot app
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
├── .gitignore                     # Git ignore rules
│
├── src/                           # Source modules
│   ├── llm.py                     # Gemini API integration
│   ├── rag.py                     # FAISS retrieval functions
│   └── utils.py                   # Helper utilities (file loading, text cleaning)
│
├── data/                          # Knowledge base documents
│   ├── faq.json                   # FAQ & common issues
│   ├── orders.json                # Order-related info
│   ├── products.json              # Product information
│   └── returns.json               # Return & refund policies
│
└── vectorstore/                   # FAISS indexes (auto-generated, git-ignored)
    ├── faiss_index.bin
    └── texts.npy
```

## 📦 Setup & Installation

> **⚠️ API Disclaimer:** This project uses third-party LLM APIs (e.g., Google Gemini API). You are responsible for your API usage and associated costs. Make sure to follow the API provider's terms and quotas.

### 1. Clone the repository

```bash
git clone https://github.com/mohith-anand/ECommerce-Customer-Support-Bot.git
cd customer-support-bot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Install required packages

```bash
pip install -r requirements.txt
```

### 5. Set up API credentials

- Add your API key (e.g., Google Gemini) to `src/llm.py` or as an environment variable
- Ensure your API plan has sufficient quota for testing

### 6. Run the app

```bash
streamlit run app.py
```

## 🚀 Usage

1. **Select mode** from the sidebar:
   - **Customer** – End-user friendly chat interface
   - **Agent** – Shows intent, sentiment, escalation, and retrieved docs

2. **Type your query** in the input box

3. **View the bot's response** instantly:
   - If escalation is required, the bot suggests further support
   - Agents can see additional context to verify or intervene if needed

## 📊 API & Dataset Information

- **LLM API:** Google Gemini (or any compatible LLM)
- **Retrieval Dataset:** Simulated order data, product info, and FAQ documents
- **Note:** This project demonstrates how AI can augment human customer support. All data used is synthetic or anonymized.



  **Built with ❤️ for better customer support automation**

# 🤖 Jarvis – Gemini AI Chatbot

**Author**: Mohd Rafey  
**Date**: 29 April 2025

Jarvis is an intelligent chatbot built using Google’s **Gemini 2.0 Flash** model. Designed as a virtual assistant, Jarvis can provide smart, AI-generated responses through natural language understanding. This version includes an introductory script where Jarvis introduces itself and credits its creator.

---

## 🧠 What Can Jarvis Do?

- Introduce itself with a custom personality
- Generate context-aware responses using Gemini AI
- Ideal for extending into a full-featured voice or text assistant

---

## 🛠 Technologies Used

| Tech              | Purpose                          |
|------------------|----------------------------------|
| `google-genai`   | Access Gemini AI content models  |
| `Python`         | Scripting and logic              |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/jarvis-gemini-chatbot.git
cd jarvis-gemini-chatbot
```

### 2. Install Dependencies

Make sure you have [Python 3.8+](https://www.python.org/downloads/) installed, then:

```bash
pip install -r requirements.txt
```

### 3. Set Your API Key

Edit the script and replace:

```python
client = genai.Client(api_key="your_api_here")
```

with your **Gemini API key** from [Google AI Studio](https://makersuite.google.com/app).

Alternatively, use environment variables for safety:

```python
import os
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
```

### 4. Run the Script

```bash
python main.py
```

---

## 🗣 Sample Prompt

The script uses the following prompt to instruct Jarvis:

> "You are a chatbot named Jarvis. Your purpose is to provide information. Start by introducing yourself to the user. Your creator's name is Rafey. He is a student at SKIT College Jaipur."

---


---

## 🔐 Security Note

✅ **DO NOT** hardcode sensitive credentials (like API keys) in public projects. Use `.env` files or environment variables.

---

## 📌 License

This project is open for educational and personal use. Feel free to modify and expand it!

---

## 🙋‍♂️ Creator Info

Built with ❤️ by **Mohd Rafey**, student at **SKIT College Jaipur**.

[GitHub](https://github.com/rafeyshamim) • [LinkedIn]([https://www.linkedin.com/](https://www.linkedin.com/in/rafey-shamim-87657b291/)) 


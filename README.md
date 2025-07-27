# 🔍 AI-Powered Resume Screening Tool

Welcome to the AI Resume Screener App — a smart, automated tool that helps recruiters and HR teams evaluate and rank resumes based on how well they match a given job description. Built with Python, NLP, spaCy, and Streamlit, this tool simplifies the hiring process by providing data-driven resume insights in seconds.

---

## 📌 Features

- 📂 Upload multiple PDF resumes at once
- 📝 Input any custom job description
- 🤖 Uses Natural Language Processing (NLP) to extract key info
- 🔎 Ranks resumes from best to least matched
- 🎯 Calculates match scores based on similarity and keyword relevance
- 🖼️ Visually appealing Streamlit dashboard with sidebar info
- ✅ Compatible with resumes containing varied structures

---

## 🚀 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **NLP Engine**: spaCy
- **Model**: `en_core_web_sm`
- **Resume Parsing**: PyPDF2 + custom entity extraction

---

## 📁 Folder Structure

```bash
├── app.py                 # Main Streamlit app
├── resume_parser.py       # PDF and NLP-based resume extractor
├── matcher.py             # JD vs resume similarity calculator
├── requirements.txt       # Dependencies for pip install
├── README.md

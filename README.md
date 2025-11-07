# 🩺 AI-Powered Healthcare Assistant

**Short description**: An end-to-end Healthcare AI system that provides disease information, symptom/treatment answers, sentiment analysis of patient feedback, and a simple chatbot — built with Hugging Face Transformers, FastAPI backend, and a Streamlit frontend.

---

## 🔎 Project overview

This repository contains a modular Healthcare Assistant showcasing several AI capabilities: clinical question answering (Bio/Clinical BERT), patient feedback sentiment analysis, disease risk prediction (tabular ML), medical image classification (CNN), patient clustering, and a simple RAG-style chatbot. The app is intended for educational/demo purposes — it provides information, not medical advice.

**Disclaimer:** This tool is for educational purposes only. It does **not** replace professional medical advice. Always consult a qualified healthcare provider for diagnosis or treatment.

---

## 🚀 Features

* 💬 **Chatbot (QA)** — Answers questions about diseases, symptoms, and treatments using a BERT QA model.
* 💬 **Structured Responses** — Replies formatted as: Disease / Symptoms / Causes / Treatments + safety note.
* 🧾 **Sentiment Analysis** — Classifies patient reviews as Positive / Neutral / Negative (BERT-based).
* ❤️ **Disease Risk Prediction** — Classic ML model (Random Forest) for heart disease prediction (example dataset included).
* 🖼️ **Imaging Module (optional)** — CNN-based chest X-ray classifier (if dataset available).
* 👥 **Patient Clustering** — Unsupervised segmentation for cohort analysis.
* 🧾 **Explainability** — SHAP support for model interpretability.
* 🧰 **Deployment-ready** — FastAPI backend + Streamlit frontend; optional ngrok for public tunneling; Docker-ready.

---

## 📁 Repository structure

```
healthcare-assistant/
├── app.py                  # Streamlit frontend (3-tab UI: Chatbot, Disease Info, About)
├── backend.py              # FastAPI backend that serves QA endpoint (/ask)
├── healthcare_chatbot.py   # Modular QA + helper functions (optional)
├── models/                 # Saved model artifacts (pkl, tf, or pt files)
├── data/                   # disease_info.txt, sample CSVs, medical_notes.txt
├── notebooks/              # Colab / Jupyter notebooks for experiments
├── requirements.txt        # Python packages
├── README.md               # This file
└── assets/                 # images/icons/screenshots
```

---

## 🧪 Datasets

* `data/heart.csv` — example heart disease dataset (UCI-style) for classification.
* `data/patient_reviews_sample.csv` — sample patient feedback for sentiment analysis.
* `data/medical_notes.txt` — sample medical notes for RAG or QA context

---

## 📞 Contact

**Anupriya R** — Data Science Learner
LinkedIn: [https://www.linkedin.com/in/anupriya-anupriya-391072257](https://www.linkedin.com/in/anupriya-anupriya-391072257

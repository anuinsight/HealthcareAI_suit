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

## ⚙️ Quick start (local)

**Prerequisites**: Python 3.9+ (3.10 recommended), pip

1. Clone the repo

```bash
git clone https://github.com/<your-username>/healthcare-assistant.git
cd healthcare-assistant
```

2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate    # macOS / Linux
venv\Scripts\activate     # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the FastAPI backend

```bash
uvicorn backend:app --reload
```

5. Run the Streamlit frontend (in a new terminal)

```bash
streamlit run app.py
```

6. Open [http://localhost:8501](http://localhost:8501) in your browser

---

## 📥 Quick start (Google Colab)

If you prefer Colab (no local install):

1. Open the provided Colab notebook (`notebooks/colab_demo.ipynb`).
2. Run cells to install dependencies, download sample datasets, and start Streamlit using `pyngrok` (remember to set your ngrok authtoken in Colab if you use ngrok).

---

## 🧪 Datasets

* `data/heart.csv` — example heart disease dataset (UCI-style) for classification.
* `data/patient_reviews_sample.csv` — sample patient feedback for sentiment analysis.
* `data/medical_notes.txt` — sample medical notes for RAG or QA context.

> **Note:** For real clinical data (MIMIC, PhysioNet), ensure you have proper access and follow HIPAA/GDPR and institutional rules.

---

## 🧰 Models & Notebooks

* `notebooks/heart_classification.ipynb` — EDA, preprocessing, Random Forest training, SHAP explainability.
* `notebooks/sentiment_finetune.ipynb` — demonstrate fine-tuning BERT on patient feedback.
* `notebooks/cxr_cnn.ipynb` — CNN training on chest X-rays (optional, uses GPU).

---

## 🔍 API (FastAPI)

Once backend is running (`uvicorn backend:app --reload`):

* **POST /ask** — body `{ "question": "..." }` → returns JSON `{ answer, confidence, note }`.

You can access Swagger UI at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🖥️ Streamlit Frontend

The frontend (`app.py`) has three tabs:

1. **Chatbot** — Enter questions and receive structured answers (calls backend `/ask`).
2. **Disease Info** — View a table of common diseases & treatments.
3. **About** — Project description, author, and disclaimer.

---

## 📦 Deployment

* **Local**: `uvicorn` + `streamlit` as above.
* **Colab**: use `pyngrok` to expose the Streamlit port (requires ngrok authtoken).
* **Production**: Dockerize using the provided `Dockerfile` and deploy to any cloud provider or Streamlit Cloud / Hugging Face Spaces.

---

## 🧾 Model Card (summary)

**Model:** `deepset/bert-base-cased-squad2` (QA), `nlptown/bert-base-multilingual-uncased-sentiment` (sentiment) or finetuned BioClinicalBERT.
**Intended Use:** Educational demo, clinical information retrieval.
**Limitations & Risks:** Not a diagnostic tool. May hallucinate; must be verified by clinicians.

---

## ✍️ Contribution

Contributions are welcome. Please open issues or PRs. Follow `CONTRIBUTING.md` for guidelines.

---

## 📜 License

Include a license file (e.g., MIT). This project template uses the MIT License by default.

---

## 📞 Contact

**Anupriya R** — Data Science Learner
LinkedIn: [https://www.linkedin.com/in/anupriya-anupriya-391072257](https://www.linkedin.com/in/anupriya-anupriya-391072257)

---

*Generated README — edit sections for your final dataset/model choices, links, and author details.*

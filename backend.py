from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load QA model
qa = pipeline("question-answering",
              model="deepset/bert-base-cased-squad2",
              tokenizer="deepset/bert-base-cased-squad2")

# Simple disease knowledge base
with open("data_info.txt", "r") as f:
    disease_context = f.read()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_question(query: Query):
    answer = qa(question=query.question, context=disease_context)
    return {
        "question": query.question,
        "answer": answer["answer"],
        "confidence": round(float(answer["score"]), 3),
        "note": "⚕️ Always consult a doctor before taking any action."
    }

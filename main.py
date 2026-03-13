from fastapi import FastAPI
import json

app = FastAPI()

with open("faq.json") as f:
    faq = json.load(f)

@app.get("/")
def home():
    return {"message": "AI FAQ Bot running"}

@app.get("/ask")
def ask(question: str):
    for key in faq:
        if key in question.lower():
            return {"answer": faq[key]}
    return {"answer": "Sorry, I don't know"}

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
import json

app = FastAPI()

templates = Jinja2Templates(directory="templates")

with open("faq.json") as f:
    faq = json.load(f)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/ask")
def ask(question: str):
    for key in faq:
        if key in question.lower():
            return {"answer": faq[key]}
    return {"answer": "Sorry, I don't know"}

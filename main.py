from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    try:
        with open("sinyal_log.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return templates.TemplateResponse("index.html", {
        "request": request,
        "data": data,
        "timestamp": timestamp
    })

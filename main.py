from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
from datetime import datetime
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def binance_access_test():
    try:
        r = requests.get("https://api.binance.com/api/v3/time", timeout=5)
        if "serverTime" in r.json():
            return "✅ Binance API erişimi açık."
        else:
            return "❌ Binance API engelli."
    except Exception as e:
        return f"⚠️ Hata oluştu: {str(e)}"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    try:
        with open("sinyal_log.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    binance_status = binance_access_test()

    return templates.TemplateResponse("index.html", {
        "request": request,
        "data": data,
        "timestamp": timestamp,
        "binance_status": binance_status
    })




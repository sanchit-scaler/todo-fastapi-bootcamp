from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    with open("db.json", "r") as f:
        db = json.load(f)
    return templates.TemplateResponse("todolist.html", {"request": request,"data": db})

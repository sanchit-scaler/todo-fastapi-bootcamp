from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    with open("db.json", "r") as f:
        db = json.load(f)
    return templates.TemplateResponse("todolist.html", {"request": request,"data": db})

@app.post("/add")
async def add_task(request: Request):
    data = await request.form()
    new_task = data["task"]
    with open("db.json", "r") as f:
        db = json.load(f)
    db[str(len(db) + 1)] = new_task
    with open("db.json", "w") as f:
        json.dump(db, f)
    # Use 303 status code for proper POST-to-GET redirect
    # This tells the browser to make a GET request to the redirect URL
    return RedirectResponse(url="/", status_code=303)
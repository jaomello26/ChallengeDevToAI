from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from modules.game_logic import start_game, process_player_input
from modules.database import set_ollama_host, create_tables
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
async def startup_event():
    set_ollama_host()
    create_tables()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    response = start_game()
    return templates.TemplateResponse("index.html", {"request": request, "response": response})

@app.post("/play", response_class=HTMLResponse)
async def play(request: Request, player_input: str = Form(...)):
    response = process_player_input(player_input)
    return templates.TemplateResponse("game.html", {"request": request, "response": response})

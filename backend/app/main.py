"""FastAPI application entry point."""
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import os

from .database import init_db

app = FastAPI()

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database
init_db()

# Setup templates directory
templates_path = os.path.join(os.path.dirname(__file__), "../../frontend/templates")
templates = Jinja2Templates(directory=templates_path)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serve the main HTML page."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/hello", response_class=HTMLResponse)
async def hello(text: str = Form(...)):
    """
    Hello endpoint that returns an H1 element.
    
    Accepts form data: text field
    Returns HTML fragment: <h1>Hello, {text}</h1>
    """
    return f"<h1 class='text-3xl font-bold text-blue-600 mt-4'>Hello, {text}</h1>"

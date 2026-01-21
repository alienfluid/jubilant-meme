# FastAPI + HTMX Web App

A simple web application with FastAPI backend and HTMX frontend, using SQLite for the database and `uv` for Python dependency management.

## Features

- FastAPI backend with RESTful API
- HTMX for dynamic frontend interactions
- Tailwind CSS for styling
- SQLite database (ready to swap with Supabase)
- Simple deployment configuration for Render

## Project Structure

```
test_project/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # FastAPI app entry point
│   │   ├── models.py        # SQLAlchemy models
│   │   └── database.py      # Database setup
│   └── pyproject.toml       # uv project dependencies
├── frontend/
│   └── templates/
│       └── index.html       # Main HTML page with HTMX
└── Procfile                 # Render deployment config
```

## Setup

### Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) installed

### Local Development

1. Install dependencies:
   ```bash
   cd backend
   uv sync
   ```

2. Run the development server:
   ```bash
   # Option 1: Use the run script (easiest)
   ./run.sh
   ```
   
   ```bash
   # Option 2: Run manually from project root
   uv run --directory backend uvicorn app.main:app --reload
   ```
   
   This runs the app from the `backend` directory, where the `app` package is available.

3. Open your browser and navigate to `http://localhost:8000`

## Deployment

### Render

1. Connect your repository to Render
2. Render will automatically detect the Python project
3. Set the build command: `curl -LsSf https://astral.sh/uv/install.sh | sh && uv sync`
4. The Procfile will handle the start command automatically

### Digital Ocean / Fly.io

For other platforms, you can use similar commands:
- Build: Install `uv` and run `uv sync`
- Start: `uv run uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT`

## API Endpoints

- `GET /` - Serves the main HTML page
- `POST /api/hello` - Accepts `{"text": "..."}` and returns `<h1>Hello, {text}</h1>`

## Future Enhancements

- Database models for persistent data storage
- Migration to Supabase when needed
- Additional API endpoints
- More frontend pages and interactions

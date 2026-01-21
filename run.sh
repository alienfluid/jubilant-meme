#!/bin/bash
# Run script for local development
cd "$(dirname "$0")"
uv run --directory backend uvicorn app.main:app --reload

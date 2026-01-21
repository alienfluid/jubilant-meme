#!/bin/bash
# Run script for local development
cd "$(dirname "$0")"
uv run uvicorn backend.app.main:app --reload

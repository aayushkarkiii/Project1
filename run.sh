#!/bin/bash
# Start script for Event Booking App
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Please set up the venv first."
    exit 1
fi

echo "Starting Event Booking Server..."
./venv/bin/uvicorn app:app --host 0.0.0.0 --port 8000 --reload

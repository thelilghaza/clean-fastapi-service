# Clean FastAPI Service

Production-ready microservice built with FastAPI, adhering to standard DevOps practices.

## Installation
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the App
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Testing
```bash
pytest
```

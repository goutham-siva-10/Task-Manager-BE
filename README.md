# Backend

FastAPI backend for the Task Manager project.

## Tech Stack

- FastAPI
- SQLAlchemy
- Pydantic
- JWT authentication
- Supabase PostgreSQL

## Run locally

From the `backend` folder:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Backend runs at:

- `http://127.0.0.1:8000`
- Docs: `http://127.0.0.1:8000/docs`

## Environment variables

Create `backend/.env`:

```env
SECRET_KEY=replace-with-a-long-random-string
DATABASE_URL=postgresql+psycopg2://postgres:YOUR_SUPABASE_PASSWORD@db.YOUR_PROJECT_REF.supabase.co:5432/postgres
CORS_ORIGINS=http://127.0.0.1:5173,http://localhost:5173
```

## Endpoints

### Authentication

- `POST /register`
- `POST /login`

### Tasks

- `POST /tasks`
- `GET /tasks`
- `GET /tasks/{task_id}`
- `PUT /tasks/{task_id}`
- `DELETE /tasks/{task_id}`

## Tests

From the `backend` folder:

```powershell
pytest
```

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import os
import psycopg2

app = FastAPI()

# model danych
class Task(BaseModel):
    name: str
    status: str = "pending"

# przykładowa baza w pamięci
fake_db = []

@app.get("/")
def read_root():
    return {"message": "Aplikacja DevOps działa!"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return fake_db

@app.post("/tasks")
def add_task(task: Task):
    fake_db.append(task)
    return {"message": "Zadanie dodane", "task": task}

# symuluje zmienną środowiskową do połączenia z bazą
@app.get("/db-check")
def db_check():
    db_url = os.getenv("DATABASE_URL", "Brak konfiguracji bazy")
    return {"db_connection_string": db_url}

# endpoint sprawdzający połączenie
@app.get("/health-db")
def health_db():
    try:
        # Próba połączenia z bazą PostgreSQL
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        conn.close()
        return {"status": "Database connected successfully!"}
    except Exception as e:
        return {"status": "Database connection failed", "error": str(e)}
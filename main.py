from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import os
import psycopg2

app = FastAPI(title="Study Tasks API")

class Task(BaseModel):
    name: str
    status: str = "pending"

def get_conn():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise RuntimeError("Brak zmiennej DATABASE_URL")
    return psycopg2.connect(db_url)

@app.on_event("startup")
def init_db():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                status TEXT NOT NULL
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("DB init error:", e)

@app.get("/")
def read_root():
    return {"message": "Study Tasks API działa!"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name, status FROM tasks ORDER BY id ASC;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [Task(name=r[0], status=r[1]) for r in rows]

@app.post("/tasks")
def add_task(task: Task):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tasks (name, status) VALUES (%s, %s) RETURNING id;",
        (task.name, task.status)
    )
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Zadanie dodane do DB", "id": new_id, "task": task}

@app.get("/health-db")
def health_db():
    try:
        conn = get_conn()
        conn.close()
        return {"status": "Database connected successfully!"}
    except Exception as e:
        return {"status": "Database connection failed", "error": str(e)}


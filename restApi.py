import app
from fastapi import FastAPI
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="myuser",
    password="mypassword",
    dbname="mydatabase"
)

cursor = conn.cursor()

app = FastAPI()

@app.get("/tasks")
def get_tasks():
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    cur.close()
    return rows

@app.post("/tasks/{title}")
def insert_task(title: str):
    c = conn.cursor()
    cur = c.cursor()
    cur.execute("INSERT INTO tasks(title) VALUES(%s)", (title,))
    c.commit()
    cur.close()
    c.close()
    return {"status": "inserted"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    c = conn.cursor()
    cur = c.cursor()
    cur.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
    c.commit()
    cur.close()
    c.close()
    return {"status": "deleted"}
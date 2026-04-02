from src.db.database import cursor, conn

def handle_task(task_data):
    text = task_data["text"]
    priority = task_data.get("priority", "normal")

    # store in DB with priority
    return f"✅ Task added: {text} (Priority: {priority})"

def get_tasks():
    cursor.execute("SELECT content FROM tasks")
    rows = cursor.fetchall()
    return [r[0] for r in rows]
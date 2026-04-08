from src.db.database import cursor, conn

def handle_calendar(user_input: str):
    cursor.execute("INSERT INTO events (content) VALUES (?)", (user_input,))
    conn.commit()
    return f"📅 Event saved: {user_input}"
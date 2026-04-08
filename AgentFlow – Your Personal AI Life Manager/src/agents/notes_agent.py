from src.db.database import cursor, conn

def handle_notes(user_input: str):
    cursor.execute("INSERT INTO notes (content) VALUES (?)", (user_input,))
    conn.commit()
    return f"📝 Note saved: {user_input}"
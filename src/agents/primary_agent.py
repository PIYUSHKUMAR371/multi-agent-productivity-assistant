import re
from .task_agent import handle_task, get_tasks
from .calendar_agent import handle_calendar
from .notes_agent import handle_notes

def primary_agent(user_input: str):
    user_input_lower = user_input.lower()

    # 🔥 1. HANDLE READ OPERATIONS FIRST (PRO DESIGN)
    if "show tasks" in user_input_lower:
        tasks = get_tasks()
        return "\n".join(tasks) if tasks else "No tasks found."

    responses = []

    # 🔥 2. Extract time
    time_match = re.search(r'(\d{1,2}\s?(am|pm))', user_input_lower)

    # 🔥 3. TASK
    # TASK
    if "task" in user_input_lower or "todo" in user_input_lower:
        task_text = user_input.replace("task", "").strip()

        priority = "high" if "urgent" in user_input_lower else "normal"

        responses.append(handle_task({
            "text": task_text,
            "priority": priority
    }))

    # 🔥 4. EVENT
    if "meeting" in user_input_lower or "schedule" in user_input_lower:
        event_text = user_input
        if time_match:
            event_text = f"Meeting at {time_match.group()}"
        responses.append(handle_calendar(event_text))

    # 🔥 5. NOTES
    if "note" in user_input_lower:
        responses.append(handle_notes(user_input))

    # 🔥 6. FALLBACK
    if not responses:
        return "❌ Couldn't understand request."

    return "\n".join(responses)
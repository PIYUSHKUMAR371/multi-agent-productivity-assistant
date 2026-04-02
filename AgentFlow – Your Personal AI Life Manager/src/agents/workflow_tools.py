from google.adk.tools import Tool

def create_task_and_event(task: str, time: str):
    return f"""
    ✅ Workflow Completed:
    - Task Created: {task}
    - Event Scheduled at: {time}
    """

workflow_tool = Tool.from_function(create_task_and_event)
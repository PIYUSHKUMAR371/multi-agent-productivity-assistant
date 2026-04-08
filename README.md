# 🚀 Multi-Agent Productivity Assistant

A clean, API-based multi-agent system that helps users manage tasks, schedules, and notes through intelligent request routing and tool coordination.

---

## 🧠 Overview

This project demonstrates a **multi-agent architecture** where a primary agent interprets user input and delegates actions to specialized sub-agents.

The system supports:

* Task management
* Meeting scheduling
* Note-taking
* Multi-step workflows (handling multiple actions in one request)

---

## ⚙️ Architecture

```
Primary Agent (Router)
        ↓
 ┌───────────────┐
 │ Task Agent    │ → SQLite (tasks)
 │ CalendarAgent │ → SQLite (events)
 │ Notes Agent   │ → SQLite (notes)
 └───────────────┘
        ↓
     FastAPI API
```

---

## ✨ Features

* 🧠 **Primary Agent Routing** — Understands user intent and delegates tasks
* 🔧 **Modular Sub-Agents** — Separate agents for tasks, calendar, and notes
* 🔄 **Multi-Step Workflows** — Handles multiple actions in a single request
* 💾 **Persistent Storage** — Uses SQLite for structured data storage
* 🌐 **REST API** — Built with FastAPI for easy integration
* ⚡ **Lightweight & Scalable Design**

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Language:** Python
* **Database:** SQLite
* **Architecture:** Multi-Agent System

---

## 📡 API Endpoints

### 🔹 POST `/chat`

Process user input and trigger agent actions.

#### Request:

```json
{
  "message": "Add urgent task to finish project and schedule meeting at 5pm"
}
```

#### Response:

```json
{
  "status": "success",
  "response": {
    "actions": [
      "Task added",
      "Meeting scheduled"
    ]
  }
}
```

---

### 🔹 GET `/tasks`

Retrieve all stored tasks.

#### Response:

```json
{
  "status": "success",
  "tasks": [
    "Finish project (Priority: high)"
  ]
}
```

---

### 🔹 GET `/health`

Check if API is running.

```json
{
  "status": "running"
}
```

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/multi-agent-productivity-assistant.git
cd multi-agent-productivity-assistant
```

### 2. Install Dependencies

```bash
pip install fastapi uvicorn
```

### 3. Run the Server

```bash
uvicorn src.main:app --reload
```

### 4. Open in Browser

* API Docs: http://127.0.0.1:8000/docs

---

## 🧪 Example Usage

Input:

> "Add urgent task to complete assignment and schedule meeting at 6pm"

Output:

* Task created with high priority
* Meeting scheduled

---

## 🎯 Goal of the Project

To demonstrate:

* Agent coordination
* Tool integration
* Structured data handling
* Real-world workflow automation

---

## 🔮 Future Improvements

* Add natural language processing (LLM integration)
* UI dashboard (Streamlit / React)
* Authentication system
* Advanced scheduling logic
* Notifications/reminders

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📌 Author

**Piyush Kumar**

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!

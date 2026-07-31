# 📚 Library Management System

A modular, command-line interface (CLI) Python application integrated with an SQLite database to manage book inventories, memberships, and transaction loans seamlessly.

---

## 📊 Project Overview

| Project | Description | Key Features |
| :--- | :--- | :--- |
| **Library Management System** | Manages books, members, and loans dynamically using a local relational database. | • Add/Track books & members<br>• Monitor book availability status<br>• Handle real-time loans and returns |

---

## 🛠️ Technologies Used

*   **Python 3.x** – Core programming language.
*   **SQLite3** – Lightweight, serverless relational database engine.
*   **Datetime** – Built-in Python module utilized for tracking precise loan and return deadlines.

---

## 📁 Project Structure

The project follows a clean, modular design separating database setup, business logic, and user interaction:

*   `database_setup.py` ── Initializes the SQLite database and establishes the relational table schemas.
*   `app.py` ───────────── Contains core business logic and primary database interaction methods.
*   `main.py` ──────────── Provides the command-line interface (CLI) text menus for user interaction.
*   `*.db` ────────────── The local SQLite database binary file (automatically generated upon the first run).

---

## 🚀 How to Run the Project

Each project module is contained within its own dedicated directory. To execute the CLI application, navigate to your root directory and run the main entry point:

```bash
python3 library_management/main.py
```

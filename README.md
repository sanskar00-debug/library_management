
# Python Database Projects

This collection includes three Python projects that demonstrate how to interact with an SQLite database. Each project features a modular design with a separate database setup script, an application logic class, and a command-line interface (CLI).

## Projects Overview

| Project | Description | Key Features |
| :--- | :--- | :--- |
| **Library Management System** | Manage books, members, and loans. | Add books/members, track book status, handle loans and returns. |

## How to Run the Projects

Each project is located in its own directory. To run a project, navigate to its directory and execute the `main.py` script.

### 1. Library Management System
```bash
python3 library_management/main.py
```

## Project Structure

For each project, the structure is as follows:
- `database_setup.py`: Initializes the SQLite database and creates the necessary tables.
- `app.py`: Contains the core logic and database interaction methods.
- `main.py`: Provides the command-line interface for the user.
- `*.db`: The SQLite database file (generated upon first run).

## Technologies Used
- **Python 3**: The primary programming language.
- **SQLite3**: A lightweight, disk-based database that doesn't require a separate server process.
- **Datetime**: Python's built-in module for handling dates and times.


# Todo Application

A simple, in-memory console-based Todo application built with Python.

## Overview

Phase I of a multi-phase AI-native Todo application that evolves from a simple console app into a full-featured, cloud-native system.

## Features

- Create new todo items with title and optional description
- List all todos with their status
- View individual todo details
- Update todo title, description, or status
- Delete todos
- In-memory storage (no persistence across sessions)

## Quick Start

### Using uv (recommended)

```bash
uv run python main.py
```

### Using Python directly

```bash
python main.py
```

## Menu Options

1. **Create a new todo** - Add a new task with title and optional description
2. **List all todos** - Display all tasks with their details
3. **View a single todo** - See detailed view of a specific task
4. **Update a todo** - Modify title, description, or status
5. **Delete a todo** - Remove a task
6. **Exit** - Close the application

## Project Structure

```
To-do-App/
├── main.py           # Application entry point and control flow
├── todo.py           # Todo data model and CRUD operations
├── ui.py             # Console input/output handling
├── pyproject.toml    # Project configuration (uv)
└── README.md         # This file
```

## Requirements

- Python 3.12+
- uv (optional, for dependency management)

## Development Phases

This project follows a phased development approach:

- **Phase I**: In-Memory Python Console App (current)
- **Phase II**: Full-Stack Web Application
- **Phase III**: AI-Powered Todo Chatbot
- **Phase IV**: Local Kubernetes Deployment
- **Phase V**: Advanced Cloud Deployment

## Running Tests

Manual testing only for Phase I:

```bash
uv run python main.py
```

Then follow the menu prompts to test all CRUD operations.

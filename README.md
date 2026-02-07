# Todo App - Phase I

A simple console-based todo application that stores data in memory only.

## Features

- Add new todo items
- View all todo items
- Update existing todo items
- Mark items as complete
- Exit the application

## Requirements

- Python 3.13 or higher

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Run the application using Python:

```bash
python main.py
```

## Usage

Once the application is running, you can use the following commands:

- `add <task description>` - Add a new todo item
- `list` - View all todo items
- `update <task_number> <new_description>` - Update a todo item
- `complete <task_number>` - Mark a task as complete
- `exit` - Exit the application

### Example

```
Todo App> add Buy groceries
Added: "Buy groceries" (ID: 1)
Todo App> list
1. [ ] Buy groceries
Todo App> complete 1
Completed task 1: "Buy groceries"
Todo App> list
1. [x] Buy groceries
Todo App> exit
Goodbye!
```

## Architecture

The application follows a clean architecture pattern with the following components:

- `models`: Contains the data models (TodoItem)
- `repositories`: Handles data storage (in-memory repository)
- `services`: Contains business logic (TodoService)
- `cli`: Handles user input and output
- `utils`: Contains utility functions and validation
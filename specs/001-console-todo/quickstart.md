# Quickstart Guide: Phase I - In-Memory Python Console Todo App

## Prerequisites

- Python 3.13 or higher
- UV package manager installed
- Terminal/console access

## Setup

1. Clone or navigate to the project directory
2. Install dependencies (if any):
   ```bash
   uv sync
   ```
   Or if using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. Verify installation:
   ```bash
   python --version
   ```

## Running the Application

1. Execute the main application:
   ```bash
   python main.py
   ```

2. The application will start and display a command prompt

## Available Commands

### Add a new task
```
add <task description>
```
Example: `add Buy groceries`

### List all tasks
```
list
```
Shows all tasks with their completion status and position numbers

### Update a task
```
update <task_number> <new_description>
```
Example: `update 2 Buy food for dinner`

### Mark task as complete
```
complete <task_number>
```
Example: `complete 3`

### Exit the application
```
exit
```
Terminates the program gracefully

## Sample Session

```
Todo App> add Buy groceries
Added: "Buy groceries" (ID: 1)
Todo App> add Walk the dog
Added: "Walk the dog" (ID: 2)
Todo App> list
1. [ ] Buy groceries
2. [ ] Walk the dog
Todo App> complete 2
Task 2 marked as complete: "Walk the dog"
Todo App> list
1. [ ] Buy groceries
2. [x] Walk the dog
Todo App> exit
Goodbye!
```

## Error Handling

- Invalid commands show helpful error messages
- Out-of-range task numbers return error indicating valid range
- Empty task descriptions return error requesting non-empty input
- Unknown commands return list of valid commands

## Troubleshooting

If the application fails to start:
1. Verify Python 3.13+ is installed
2. Check that all dependencies are installed
3. Ensure main.py has execute permissions if needed

For command issues:
- Use "list" to see current tasks and their valid numbers
- Remember commands are case-sensitive
- Task numbers are 1-indexed, not 0-indexed
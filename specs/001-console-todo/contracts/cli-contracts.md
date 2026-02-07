# API Contracts: Phase I - In-Memory Python Console Todo App

## Command Interface Definition

### Add Command
```
Command: add <task_description>
Input: String containing task description (min 1 char, max 500 chars)
Output: Success message with assigned ID and task text
Error Cases:
  - Empty description: "Error: Task description cannot be empty"
  - Description too long: "Error: Task description exceeds 500 character limit"
Response Format: "Added: \"{task}\" (ID: {id})"
```

### List Command
```
Command: list
Input: None
Output: Formatted list of all tasks with completion status and IDs
Error Cases: None (empty list returns "No tasks found")
Response Format:
"{id}. [{status}] {task}"
Where [status] is [ ] for pending or [x] for completed
Example:
"1. [ ] Buy groceries"
"2. [x] Walk the dog"
```

### Update Command
```
Command: update <task_id> <new_description>
Input: Integer task ID (1-based) and new description string
Validation:
  - task_id must exist in current list
  - new_description must not be empty after trimming
Error Cases:
  - Invalid ID: "Error: Task {id} does not exist"
  - Empty description: "Error: Task description cannot be empty"
Response Format: "Updated task {id}: \"{new_task}\""
```

### Complete Command
```
Command: complete <task_id>
Input: Integer task ID (1-based)
Validation:
  - task_id must exist in current list
Error Cases:
  - Invalid ID: "Error: Task {id} does not exist"
Response Format: "Completed task {id}: \"{task_text}\""
```

### Exit Command
```
Command: exit
Input: None
Output: Graceful shutdown message
Error Cases: None
Response Format: "Goodbye!" followed by program termination
```

## Data Models

### TodoItem
```
{
  "id": int,           // Unique identifier, positive integer
  "title": str,        // Task description, non-empty
  "completed": bool    // Completion status, default false
}
```

### TodoList
```
[
  TodoItem,    // Array of TodoItem objects in insertion order
  ...
]
```

### Response Objects
```
Success Response:
{
  "success": true,
  "message": str,
  "data": optional object
}

Error Response:
{
  "success": false,
  "error": str,
  "code": str
}
```

## CLI Interaction Contract

### Input Processing
- Commands are case-sensitive
- Arguments separated by whitespace
- Commands parsed as: `[command] [arg1] [arg2] ...`
- Quoted strings preserved as single arguments

### Output Formatting
- All output goes to stdout
- Error messages to stderr
- Consistent formatting for readability
- UTF-8 encoded text

### Session Flow
1. Display prompt: "Todo App> "
2. Accept command input
3. Process command
4. Display result
5. Repeat until exit command
6. Clean shutdown
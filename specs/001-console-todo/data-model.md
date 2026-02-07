# Data Model: Phase I - In-Memory Python Console Todo App

## Primary Entity: TodoItem

### Attributes
- **id** (int): Unique identifier assigned sequentially, immutable after creation
- **title** (str): Text description of the task, mutable via update operations
- **completed** (bool): Completion status (true for completed, false for pending), mutable via complete/incomplete operations

### Validation Rules
- **id**: Must be positive integer, automatically assigned by system, cannot be changed by user
- **title**: Must be non-empty string after trimming whitespace, maximum length 500 characters
- **completed**: Boolean value only, defaults to False on creation

### State Transitions
- **Creation**: id=assigned, title=user_input, completed=False
- **Complete**: completed changes from False to True (irreversible in initial implementation)
- **Update**: title changes to new value, id and completed status preserved
- **Deletion**: Item removed from active list (transitional state)

## Collection: TodoList

### Characteristics
- **Type**: Ordered collection (Python list) of TodoItem objects
- **Access**: Indexed by sequential position (1-based for user display, 0-based internally)
- **Uniqueness**: Each TodoItem.id must be unique within the collection
- **Ordering**: Maintains insertion order for consistent user experience

### Operations
- **Add**: Append new TodoItem to end of list with next available id
- **View**: Iterate through list showing all items with positional numbers
- **Update**: Locate item by id, modify title attribute
- **Complete**: Locate item by id, set completed to True
- **Delete**: Remove item by id (not implemented separately - items remain but marked complete)

## Relationship Patterns

### Identity Management
- TodoItem.id uses auto-incrementing sequence starting from 1
- Id assignment happens at creation and remains constant
- Duplicate ids are prevented by using max(id) + 1 pattern

### Lifecycle Constraints
- TodoItem objects exist only in memory during application runtime
- No persistence mechanism exists in Phase I
- Items are garbage collected when application exits
- All state resets on application restart

## Data Integrity Rules

### Consistency Requirements
- Each TodoItem must have valid id, title, and completed status
- Title cannot be empty or consist only of whitespace
- Id must be unique within the TodoList collection
- Internal 0-based indexing and external 1-based user numbering must remain synchronized

### Error Conditions
- Invalid id format or value raises ValidationError
- Empty title raises ValidationError
- Attempt to update non-existent item raises ItemNotFoundError
- Attempt to complete non-existent item raises ItemNotFoundError
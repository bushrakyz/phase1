#!/usr/bin/env python3
"""
Quick test to verify the Todo application is working properly.
"""

from src.cli.cli_app import TodoApp
from src.services.todo_service import TodoService
from src.repositories.todo_repository import TodoRepository

def test_basic_functionality():
    """Test the basic functionality of the todo app."""
    print("Testing basic functionality...")

    # Test using the service layer directly
    repository = TodoRepository()
    service = TodoService(repository)

    # Add a task
    item = service.add_item("Test task")
    print(f"SUCCESS: Added task: {item.title} with ID {item.id}")

    # List tasks
    items = service.get_all_items()
    print(f"SUCCESS: Retrieved {len(items)} task(s)")

    # Update the task
    updated_item = service.update_item(item.id, "Updated test task")
    print(f"SUCCESS: Updated task to: {updated_item.title}")

    # Complete the task
    completed_item = service.complete_item(item.id)
    print(f"SUCCESS: Completed task: {completed_item.title} (completed: {completed_item.completed})")

    # Test CLI app creation
    app = TodoApp()
    print("SUCCESS: Created TodoApp instance successfully")

    print("\nAll basic functionality tests passed!")

if __name__ == "__main__":
    test_basic_functionality()
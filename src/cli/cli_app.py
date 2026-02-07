"""
Command Line Interface application for the Todo app.

This module implements the TodoApp class which handles user input,
command parsing, and output display for the console-based todo application.
"""

from typing import List, Optional
import sys
from ..services.todo_service import TodoService
from ..repositories.todo_repository import TodoRepository
from ..utils.exceptions import ValidationError, ItemNotFoundError
from ..utils.validators import validate_task_id, validate_command_parts


class TodoApp:
    """
    Main CLI application class for the Todo app.

    This class handles the main application loop, command parsing,
    and interaction with the TodoService for all business operations.
    """

    def __init__(self) -> None:
        """Initialize the application with repository and service instances."""
        self.repository = TodoRepository()
        self.service = TodoService(self.repository)

    def run(self) -> None:
        """Start the main application loop."""
        print("Welcome to Todo App! Type 'help' for available commands or 'exit' to quit.")

        while True:
            try:
                # Display prompt and get user input
                user_input = input("\nTodo App> ").strip()

                if not user_input:
                    continue

                # Parse and execute the command
                if not self.execute_command(user_input):
                    break  # Exit the loop if execute_command returns False

            except KeyboardInterrupt:
                print("\n\nReceived interrupt signal. Goodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break

    def execute_command(self, user_input: str) -> bool:
        """
        Parse and execute a user command.

        Args:
            user_input: The raw user input string

        Returns:
            True to continue running, False to exit
        """
        parts = user_input.split()

        if not parts:
            return True

        command = parts[0].lower()

        if command == "add":
            self._handle_add(parts[1:])
        elif command == "list":
            self._handle_list()
        elif command == "update":
            self._handle_update(parts[1:])
        elif command == "complete":
            self._handle_complete(parts[1:])
        elif command == "exit":
            return self._handle_exit()
        elif command == "help":
            self._handle_help()
        else:
            print(f"Unknown command: '{command}'. Type 'help' for available commands.")

        return True

    def _handle_add(self, args: List[str]) -> None:
        """
        Handle the 'add' command to create new todo items.

        Args:
            args: The command arguments after 'add'
        """
        try:
            validate_command_parts(['add'] + args, 2, 'add')
            title = ' '.join(args)

            item = self.service.add_item(title)
            print(f"Added: \"{item.title}\" (ID: {item.id})")
        except ValidationError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error adding task: {e}")

    def _handle_list(self) -> None:
        """Handle the 'list' command to display all todo items."""
        try:
            items = self.service.get_all_items()

            if not items:
                print("No tasks in your todo list.")
                return

            print("Your todo list:")
            for item in items:
                print(f"{item.id}. {item}")
        except Exception as e:
            print(f"Unexpected error listing tasks: {e}")

    def _handle_update(self, args: List[str]) -> None:
        """
        Handle the 'update' command to modify existing todo items.

        Args:
            args: The command arguments after 'update'
        """
        try:
            validate_command_parts(['update'] + args, 3, 'update')

            item_id = validate_task_id(args[0])
            new_title = ' '.join(args[1:])

            item = self.service.update_item(item_id, new_title)
            print(f"Updated task {item.id}: \"{item.title}\"")
        except ValidationError as e:
            print(f"Error: {e}")
        except ItemNotFoundError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error updating task: {e}")

    def _handle_complete(self, args: List[str]) -> None:
        """
        Handle the 'complete' command to mark items as completed.

        Args:
            args: The command arguments after 'complete'
        """
        try:
            validate_command_parts(['complete'] + args, 2, 'complete')

            item_id = validate_task_id(args[0])

            item = self.service.complete_item(item_id)
            print(f"Completed task {item.id}: \"{item.title}\"")
        except ValidationError as e:
            print(f"Error: {e}")
        except ItemNotFoundError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error completing task: {e}")

    def _handle_exit(self) -> bool:
        """
        Handle the 'exit' command to terminate the application.

        Returns:
            False to indicate the application should exit
        """
        print("Goodbye!")
        return False

    def _handle_help(self) -> None:
        """Handle the 'help' command to display available commands."""
        help_text = """
Available commands:
  add <task>          - Add a new todo item
  list                - View all todo items
  update <id> <task>  - Update an existing todo item
  complete <id>       - Mark a task as complete
  exit                - Exit the application
  help                - Show this help message
        """.strip()
        print(help_text)
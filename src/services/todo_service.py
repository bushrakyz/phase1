"""
Business logic service for managing todo items.

This module implements the TodoService class which encapsulates all
business logic for managing todo items, including adding, retrieving,
updating, and completing tasks.
"""

from typing import List
from ..models.todo import TodoItem
from ..repositories.todo_repository import TodoRepository
from ..utils.exceptions import ValidationError, ItemNotFoundError
from ..utils.validators import validate_task_title


class TodoService:
    """
    Service class containing business logic for todo operations.

    This class orchestrates operations on todo items by coordinating
    between validation, repository storage, and business rules.
    """

    def __init__(self, repository: TodoRepository) -> None:
        """
        Initialize the service with a repository.

        Args:
            repository: The repository to use for data storage operations
        """
        self.repository = repository

    def add_item(self, title: str) -> TodoItem:
        """
        Add a new todo item after validating the input.

        Args:
            title: The title of the new todo item

        Returns:
            The newly created TodoItem

        Raises:
            ValidationError: If the title is invalid
        """
        validate_task_title(title)
        return self.repository.add_item(title.strip())

    def get_all_items(self) -> List[TodoItem]:
        """
        Retrieve all todo items from the repository.

        Returns:
            A list of all todo items
        """
        return self.repository.get_all_items()

    def update_item(self, item_id: int, new_title: str) -> TodoItem:
        """
        Update the title of an existing todo item after validation.

        Args:
            item_id: The ID of the item to update
            new_title: The new title for the item

        Returns:
            The updated TodoItem

        Raises:
            ValidationError: If the new title is invalid
            ItemNotFoundError: If no item exists with the given ID
        """
        validate_task_title(new_title)
        return self.repository.update_item(item_id, new_title.strip())

    def complete_item(self, item_id: int) -> TodoItem:
        """
        Mark a todo item as completed.

        Args:
            item_id: The ID of the item to mark as completed

        Returns:
            The completed TodoItem

        Raises:
            ItemNotFoundError: If no item exists with the given ID
        """
        return self.repository.complete_item(item_id)

    def delete_item(self, item_id: int) -> bool:
        """
        Remove a todo item from the repository.

        Args:
            item_id: The ID of the item to delete

        Returns:
            True if the item was deleted, False if it didn't exist
        """
        return self.repository.delete_item(item_id)
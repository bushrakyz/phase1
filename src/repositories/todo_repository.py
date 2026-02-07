"""
In-memory repository for storing todo items.

This module implements the TodoRepository class which provides an in-memory
storage solution for todo items using a list-based approach.
"""

from typing import List, Optional
from ..models.todo import TodoItem
from ..utils.exceptions import ItemNotFoundError


class TodoRepository:
    """
    Repository for managing TodoItem objects in memory.

    This class handles all data storage operations for todo items,
    including creating, retrieving, updating, and deleting items.
    All data is stored in memory and will be lost when the application exits.
    """

    def __init__(self) -> None:
        """Initialize the repository with an empty list of todo items."""
        self._items: List[TodoItem] = []
        self._next_id: int = 1

    def add_item(self, title: str) -> TodoItem:
        """
        Add a new todo item to the repository.

        Args:
            title: The title/description of the new todo item

        Returns:
            The newly created TodoItem with a unique ID
        """
        item = TodoItem(id=self._next_id, title=title, completed=False)
        self._items.append(item)
        self._next_id += 1
        return item

    def get_all_items(self) -> List[TodoItem]:
        """
        Retrieve all todo items from the repository.

        Returns:
            A list containing all todo items in the repository
        """
        return self._items.copy()  # Return a copy to prevent external modification

    def get_item_by_id(self, item_id: int) -> TodoItem:
        """
        Retrieve a specific todo item by its ID.

        Args:
            item_id: The ID of the todo item to retrieve

        Returns:
            The TodoItem with the specified ID

        Raises:
            ItemNotFoundError: If no item exists with the given ID
        """
        for item in self._items:
            if item.id == item_id:
                return item
        raise ItemNotFoundError(f"Todo item with ID {item_id} not found")

    def update_item(self, item_id: int, new_title: str) -> TodoItem:
        """
        Update the title of an existing todo item.

        Args:
            item_id: The ID of the item to update
            new_title: The new title for the item

        Returns:
            The updated TodoItem

        Raises:
            ItemNotFoundError: If no item exists with the given ID
        """
        item = self.get_item_by_id(item_id)
        item.update_title(new_title)
        return item

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
        item = self.get_item_by_id(item_id)
        item.mark_completed()
        return item

    def delete_item(self, item_id: int) -> bool:
        """
        Remove a todo item from the repository.

        Args:
            item_id: The ID of the item to delete

        Returns:
            True if the item was deleted, False if it didn't exist
        """
        for i, item in enumerate(self._items):
            if item.id == item_id:
                del self._items[i]
                return True
        return False

    def clear_all(self) -> None:
        """Remove all items from the repository."""
        self._items.clear()
        self._next_id = 1
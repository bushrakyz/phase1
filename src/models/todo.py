"""
TodoItem data model representing a single todo task.

This module defines the TodoItem class which represents a single todo task
with an ID, title, and completion status.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class TodoItem:
    """
    Represents a single todo item with id, title, and completion status.

    Attributes:
        id: Unique identifier for the todo item
        title: Description of the todo task
        completed: Boolean indicating whether the task is completed
    """

    id: int
    title: str
    completed: bool = False

    def __str__(self) -> str:
        """
        String representation of the todo item.

        Returns:
            Formatted string showing completion status and title
        """
        status = "[x]" if self.completed else "[ ]"
        return f"{status} {self.title}"

    def mark_completed(self) -> None:
        """Mark the todo item as completed."""
        self.completed = True

    def update_title(self, new_title: str) -> None:
        """
        Update the title of the todo item.

        Args:
            new_title: New title for the todo item
        """
        self.title = new_title
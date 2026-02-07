"""
Input validation utilities for the Todo application.

This module provides functions for validating various types of user input
to ensure data integrity and proper application behavior.
"""

from typing import Union
from .exceptions import ValidationError


def validate_task_title(title: str) -> None:
    """
    Validate that a task title is not empty or only whitespace.

    Args:
        title: The task title to validate

    Raises:
        ValidationError: If the title is empty or only whitespace
    """
    if not title or not title.strip():
        raise ValidationError("Task title cannot be empty or only whitespace")


def validate_task_id(task_id: Union[str, int]) -> int:
    """
    Validate that a task ID is a positive integer.

    Args:
        task_id: The task ID to validate (as string or int)

    Returns:
        The validated task ID as an integer

    Raises:
        ValidationError: If the task ID is not a positive integer
    """
    try:
        task_id_int = int(task_id)
        if task_id_int <= 0:
            raise ValidationError(f"Task ID must be a positive integer, got {task_id_int}")
        return task_id_int
    except ValueError:
        raise ValidationError(f"Invalid task ID format: {task_id}")


def validate_command_parts(parts: list, min_parts: int, command_name: str) -> None:
    """
    Validate that a command has the required number of parts.

    Args:
        parts: The command parts (split by whitespace)
        min_parts: The minimum number of parts required
        command_name: The name of the command (for error messages)

    Raises:
        ValidationError: If the command doesn't have enough parts
    """
    if len(parts) < min_parts:
        raise ValidationError(f"'{command_name}' command requires at least {min_parts - 1} arguments")
"""
Custom exception classes for the Todo application.

This module defines custom exception classes used throughout the application
for specific error conditions.
"""


class ValidationError(Exception):
    """
    Raised when validation fails for user input or data integrity.

    This exception is raised when input validation fails, such as when
    a task description is empty or when an invalid task ID is provided.
    """

    pass


class ItemNotFoundError(Exception):
    """
    Raised when attempting to access a todo item that does not exist.

    This exception is raised when trying to update, complete, or access
    a todo item using an ID that does not correspond to any existing item.
    """

    pass
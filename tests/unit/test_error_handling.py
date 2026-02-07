"""
Unit tests for error handling in the Todo application.

These tests verify that appropriate exceptions are raised and handled
correctly throughout the application.
"""

import io
import sys
from unittest.mock import patch
from src.models.todo import TodoItem
from src.services.todo_service import TodoService
from src.repositories.todo_repository import TodoRepository
from src.utils.exceptions import ValidationError, ItemNotFoundError
from src.cli.cli_app import TodoApp


class TestErrorHandling:
    """Test suite for error handling functionality."""

    def test_todo_service_validation_errors(self):
        """Test that TodoService properly validates input and raises ValidationError."""
        repository = TodoRepository()
        service = TodoService(repository)

        # Test empty title validation
        try:
            service.add_item("")
            assert False, "Expected ValidationError for empty title"
        except ValidationError as e:
            assert "cannot be empty" in str(e)

        # Test whitespace-only title validation
        try:
            service.add_item("   ")
            assert False, "Expected ValidationError for whitespace-only title"
        except ValidationError as e:
            assert "cannot be empty" in str(e)

        # Test update with empty title
        item = service.add_item("Valid task")
        try:
            service.update_item(item.id, "")
            assert False, "Expected ValidationError for empty update title"
        except ValidationError as e:
            assert "cannot be empty" in str(e)

    def test_todo_service_not_found_errors(self):
        """Test that TodoService raises ItemNotFoundError for non-existent items."""
        repository = TodoRepository()
        service = TodoService(repository)

        # Add one item
        service.add_item("Valid task")

        # Try to update non-existent item
        try:
            service.update_item(999, "New title")
            assert False, "Expected ItemNotFoundError for non-existent item"
        except ItemNotFoundError as e:
            assert "not found" in str(e)

        # Try to complete non-existent item
        try:
            service.complete_item(999)
            assert False, "Expected ItemNotFoundError for non-existent item"
        except ItemNotFoundError as e:
            assert "not found" in str(e)

    def test_todo_repository_not_found_errors(self):
        """Test that TodoRepository raises ItemNotFoundError for non-existent items."""
        repository = TodoRepository()

        # Add one item
        repository.add_item("Valid task")

        # Try to get non-existent item
        try:
            repository.get_item_by_id(999)
            assert False, "Expected ItemNotFoundError for non-existent item"
        except ItemNotFoundError as e:
            assert "not found" in str(e)

    def test_cli_validation_error_handling(self):
        """Test that CLI properly handles ValidationError."""
        app = TodoApp()

        # Test add command with no arguments
        captured_output = io.StringIO()

        with patch('sys.stdout', captured_output):
            app._handle_add([])  # No arguments should trigger validation error

        output = captured_output.getvalue().strip()
        assert "Error:" in output
        assert "requires at least 1 arguments" in output

    def test_cli_item_not_found_error_handling(self):
        """Test that CLI properly handles ItemNotFoundError."""
        app = TodoApp()

        # Test complete command with non-existent ID
        captured_output = io.StringIO()

        with patch('sys.stdout', captured_output):
            app._handle_complete(["999"])  # Non-existent ID

        output = captured_output.getvalue().strip()
        assert "Error:" in output
        assert "not found" in output

    def test_cli_update_validation_error_handling(self):
        """Test that CLI properly handles validation errors in update command."""
        app = TodoApp()

        # Add one item
        app.service.add_item("Valid task")

        # Test update command with insufficient arguments
        captured_output = io.StringIO()

        with patch('sys.stdout', captured_output):
            app._handle_update(["1"])  # Missing new title

        output = captured_output.getvalue().strip()
        assert "Error:" in output
        assert "requires at least 2 arguments" in output

    def test_cli_invalid_command_parts_handling(self):
        """Test that CLI handles various invalid command formats."""
        app = TodoApp()

        # Test update with ID but no new title
        captured_output = io.StringIO()

        with patch('sys.stdout', captured_output):
            app._handle_update(["1"])  # ID without new title

        output = captured_output.getvalue().strip()
        assert "Error:" in output
        assert "requires at least 2 arguments" in output

    def test_cli_invalid_task_id_format(self):
        """Test that CLI handles invalid task ID formats."""
        app = TodoApp()

        # Test complete with non-numeric ID
        captured_output = io.StringIO()

        with patch('sys.stdout', captured_output):
            app._handle_complete(["abc"])  # Invalid ID format

        output = captured_output.getvalue().strip()
        assert "Error:" in output
        assert "Invalid task ID format" in output

    def test_cli_negative_task_id(self):
        """Test that CLI handles negative task IDs."""
        app = TodoApp()

        # Test complete with negative ID
        captured_output = io.StringIO()

        with patch('sys.stdout', captured_output):
            app._handle_complete(["-1"])  # Negative ID

        output = captured_output.getvalue().strip()
        assert "Error:" in output
        assert "positive integer" in output
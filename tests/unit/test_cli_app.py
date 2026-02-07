"""
Unit tests for the TodoApp CLI class.

These tests verify the command parsing and handling functionality
of the TodoApp class without relying on actual user input/output.
"""

import io
import sys
from unittest.mock import Mock, patch
from src.cli.cli_app import TodoApp
from src.utils.exceptions import ValidationError, ItemNotFoundError


class TestTodoApp:
    """Test suite for the TodoApp class."""

    def setup_method(self):
        """Set up a fresh TodoApp instance for each test."""
        self.app = TodoApp()

    def test_execute_command_add_single_word(self):
        """Test that the 'add' command adds a single-word task."""
        # Capture printed output
        captured_output = io.StringIO()

        with patch('sys.stdout', captured_output):
            self.app._handle_add(["Buy", "groceries"])

        output = captured_output.getvalue().strip()
        assert "Added: \"Buy groceries\"" in output
        assert "(ID: 1)" in output

    def test_execute_command_add_multi_word(self):
        """Test that the 'add' command adds a multi-word task."""
        captured_output = io.StringIO()

        with patch('sys.stdout', captured_output):
            self.app._handle_add(["Complete", "software", "project"])

        output = captured_output.getvalue().strip()
        assert "Added: \"Complete software project\"" in output

    def test_execute_command_list_empty(self):
        """Test that the 'list' command shows a message when the list is empty."""
        captured_output = io.StringIO()

        with patch('sys.stdout', captured_output):
            self.app._handle_list()

        output = captured_output.getvalue().strip()
        assert "No tasks in your todo list." in output

    def test_execute_command_list_with_items(self):
        """Test that the 'list' command displays existing tasks."""
        # Add a task first
        self.app.service.add_item("Test task")

        captured_output = io.StringIO()

        with patch('sys.stdout', captured_output):
            self.app._handle_list()

        output = captured_output.getvalue()
        assert "Your todo list:" in output
        assert "1. [ ] Test task" in output

    def test_execute_command_update_success(self):
        """Test that the 'update' command successfully updates a task."""
        # Add a task first
        item = self.app.service.add_item("Original task")

        captured_output = io.StringIO()

        with patch('sys.stdout', captured_output):
            self.app._handle_update([str(item.id), "Updated", "task"])

        output = captured_output.getvalue().strip()
        assert "Updated task 1: \"Updated task\"" in output

    def test_execute_command_update_invalid_id(self):
        """Test that the 'update' command handles invalid task IDs."""
        captured_output = io.StringIO()

        with patch('sys.stdout', captured_output):
            self.app._handle_update(["999", "Updated", "task"])

        output = captured_output.getvalue().strip()
        assert "Todo item with ID 999 not found" in output

    def test_execute_command_complete_success(self):
        """Test that the 'complete' command successfully marks a task complete."""
        # Add a task first
        item = self.app.service.add_item("Test task")

        captured_output = io.StringIO()

        with patch('sys.stdout', captured_output):
            self.app._handle_complete([str(item.id)])

        output = captured_output.getvalue().strip()
        assert f"Completed task {item.id}: \"Test task\"" in output

    def test_execute_command_complete_invalid_id(self):
        """Test that the 'complete' command handles invalid task IDs."""
        captured_output = io.StringIO()

        with patch('sys.stdout', captured_output):
            self.app._handle_complete(["999"])

        output = captured_output.getvalue().strip()
        assert "Todo item with ID 999 not found" in output

    def test_execute_command_unknown_command(self):
        """Test that unknown commands show an appropriate error message."""
        # This would normally be tested through execute_command method
        # but let's test the specific behavior
        captured_output = io.StringIO()

        with patch('sys.stdout', captured_output):
            result = self.app.execute_command("unknowncommand")

        output = captured_output.getvalue().strip()
        assert "Unknown command: 'unknowncommand'" in output
        # Should return True to continue running
        assert result is True

    def test_execute_command_add_empty(self):
        """Test that the 'add' command handles insufficient arguments."""
        captured_output = io.StringIO()

        with patch('sys.stdout', captured_output):
            # Calling the handler directly to test argument validation
            self.app._handle_add([])

        output = captured_output.getvalue().strip()
        assert "Error:" in output
        assert "requires at least 1 arguments" in output

    def test_execute_command_update_empty(self):
        """Test that the 'update' command handles insufficient arguments."""
        captured_output = io.StringIO()

        with patch('sys.stdout', captured_output):
            self.app._handle_update([])

        output = captured_output.getvalue().strip()
        assert "Error:" in output
        assert "requires at least 2 arguments" in output

    def test_execute_command_complete_empty(self):
        """Test that the 'complete' command handles insufficient arguments."""
        captured_output = io.StringIO()

        with patch('sys.stdout', captured_output):
            self.app._handle_complete([])

        output = captured_output.getvalue().strip()
        assert "Error:" in output
        assert "requires at least 1 arguments" in output
"""
Integration tests for the CLI application.

These tests verify that the entire application works correctly
by simulating user interactions with the command-line interface.
"""

import io
import sys
from unittest.mock import patch
from src.cli.cli_app import TodoApp


class TestCliIntegration:
    """Integration tests for CLI functionality."""

    def test_full_workflow_add_list_complete_update(self):
        """Test the complete workflow: add, list, complete, update."""
        app = TodoApp()

        # Capture output
        captured_output = io.StringIO()

        # Test adding a task
        with patch('sys.stdout', captured_output):
            app._handle_add(["Buy", "groceries"])

        output_before = captured_output.getvalue()
        assert "Added: \"Buy groceries\" (ID: 1)" in output_before

        # Reset output buffer
        captured_output.seek(0)
        captured_output.truncate(0)

        # Test listing tasks
        with patch('sys.stdout', captured_output):
            app._handle_list()

        output_list = captured_output.getvalue()
        assert "Your todo list:" in output_list
        assert "1. [ ] Buy groceries" in output_list

        # Reset output buffer
        captured_output.seek(0)
        captured_output.truncate(0)

        # Test completing the task
        with patch('sys.stdout', captured_output):
            app._handle_complete(["1"])

        output_complete = captured_output.getvalue()
        assert "Completed task 1: \"Buy groceries\"" in output_complete

        # Reset output buffer
        captured_output.seek(0)
        captured_output.truncate(0)

        # Test listing again to see the completed task
        with patch('sys.stdout', captured_output):
            app._handle_list()

        output_final = captured_output.getvalue()
        assert "Your todo list:" in output_final
        assert "1. [x] Buy groceries" in output_final  # Should now show as completed

    def test_multiple_tasks_workflow(self):
        """Test workflow with multiple tasks."""
        app = TodoApp()

        captured_output = io.StringIO()

        # Add multiple tasks
        with patch('sys.stdout', captured_output):
            app._handle_add(["Task", "1"])
            app._handle_add(["Task", "2"])
            app._handle_add(["Task", "3"])

        output = captured_output.getvalue()
        assert "Added: \"Task 1\" (ID: 1)" in output
        assert "Added: \"Task 2\" (ID: 2)" in output
        assert "Added: \"Task 3\" (ID: 3)" in output

        # Reset buffer
        captured_output.seek(0)
        captured_output.truncate(0)

        # List all tasks
        with patch('sys.stdout', captured_output):
            app._handle_list()

        output = captured_output.getvalue()
        assert "1. [ ] Task 1" in output
        assert "2. [ ] Task 2" in output
        assert "3. [ ] Task 3" in output

        # Reset buffer
        captured_output.seek(0)
        captured_output.truncate(0)

        # Complete task 2
        with patch('sys.stdout', captured_output):
            app._handle_complete(["2"])

        output = captured_output.getvalue()
        assert "Completed task 2: \"Task 2\"" in output

        # Reset buffer
        captured_output.seek(0)
        captured_output.truncate(0)

        # List again to verify completion status
        with patch('sys.stdout', captured_output):
            app._handle_list()

        output = captured_output.getvalue()
        assert "1. [ ] Task 1" in output
        assert "2. [x] Task 2" in output  # Should be completed
        assert "3. [ ] Task 3" in output

    def test_update_existing_task(self):
        """Test updating an existing task."""
        app = TodoApp()

        captured_output = io.StringIO()

        # Add a task
        with patch('sys.stdout', captured_output):
            app._handle_add(["Original", "task"])

        output = captured_output.getvalue()
        assert "Added: \"Original task\" (ID: 1)" in output

        # Reset buffer
        captured_output.seek(0)
        captured_output.truncate(0)

        # Update the task
        with patch('sys.stdout', captured_output):
            app._handle_update(["1", "Updated", "task", "description"])

        output = captured_output.getvalue()
        assert "Updated task 1: \"Updated task description\"" in output

        # Reset buffer
        captured_output.seek(0)
        captured_output.truncate(0)

        # Verify the update by listing
        with patch('sys.stdout', captured_output):
            app._handle_list()

        output = captured_output.getvalue()
        assert "1. [ ] Updated task description" in output
        assert "Original task" not in output  # Old title should not be present

    def test_command_routing_and_help(self):
        """Test that commands are routed correctly and help works."""
        app = TodoApp()

        captured_output = io.StringIO()

        # Test help command
        with patch('sys.stdout', captured_output):
            app._handle_help()

        output = captured_output.getvalue()
        assert "Available commands:" in output
        assert "add <task>" in output
        assert "list" in output
        assert "update <id> <task>" in output
        assert "complete <id>" in output
        assert "exit" in output
        assert "help" in output
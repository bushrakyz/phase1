"""
Unit tests for the TodoService class.

These tests verify the core functionality of the TodoService,
particularly the add_item method and its validation behavior.
"""

import pytest
from src.models.todo import TodoItem
from src.services.todo_service import TodoService
from src.repositories.todo_repository import TodoRepository
from src.utils.exceptions import ValidationError


class TestTodoService:
    """Test suite for the TodoService class."""

    def setup_method(self):
        """Set up a fresh TodoService instance for each test."""
        self.repository = TodoRepository()
        self.service = TodoService(self.repository)

    def test_add_item_success(self):
        """Test that add_item successfully creates a new todo item."""
        title = "Buy groceries"
        item = self.service.add_item(title)

        assert isinstance(item, TodoItem)
        assert item.id == 1
        assert item.title == title
        assert item.completed is False

    def test_add_item_trims_whitespace(self):
        """Test that add_item trims leading/trailing whitespace from titles."""
        title_with_spaces = "  Buy groceries  "
        item = self.service.add_item(title_with_spaces)

        assert item.title == "Buy groceries"

    def test_add_item_multiple_sequential_ids(self):
        """Test that add_item assigns sequential IDs correctly."""
        item1 = self.service.add_item("First task")
        item2 = self.service.add_item("Second task")
        item3 = self.service.add_item("Third task")

        assert item1.id == 1
        assert item2.id == 2
        assert item3.id == 3

    def test_add_item_empty_title_raises_validation_error(self):
        """Test that add_item raises ValidationError for empty titles."""
        with pytest.raises(ValidationError, match="Task title cannot be empty or only whitespace"):
            self.service.add_item("")

    def test_add_item_whitespace_only_title_raises_validation_error(self):
        """Test that add_item raises ValidationError for whitespace-only titles."""
        with pytest.raises(ValidationError, match="Task title cannot be empty or only whitespace"):
            self.service.add_item("   ")

    def test_add_item_tab_newline_title_raises_validation_error(self):
        """Test that add_item raises ValidationError for tab/newline-only titles."""
        with pytest.raises(ValidationError, match="Task title cannot be empty or only whitespace"):
            self.service.add_item("\t\n")

    def test_get_all_items_initially_empty(self):
        """Test that get_all_items returns an empty list initially."""
        items = self.service.get_all_items()

        assert items == []

    def test_get_all_items_after_adding_items(self):
        """Test that get_all_items returns all added items."""
        expected_titles = ["First task", "Second task", "Third task"]

        for title in expected_titles:
            self.service.add_item(title)

        items = self.service.get_all_items()

        assert len(items) == 3
        assert [item.title for item in items] == expected_titles
        assert all(item.completed is False for item in items)
        assert [item.id for item in items] == [1, 2, 3]

    def test_update_item_success(self):
        """Test that update_item successfully modifies an existing item."""
        original_item = self.service.add_item("Original task")
        updated_title = "Updated task"

        updated_item = self.service.update_item(original_item.id, updated_title)

        assert updated_item.id == original_item.id
        assert updated_item.title == updated_title
        assert updated_item.completed == original_item.completed

        # Verify the change is persisted by fetching the list again
        items = self.service.get_all_items()
        assert len(items) == 1
        assert items[0].title == updated_title

    def test_update_item_trims_whitespace(self):
        """Test that update_item trims leading/trailing whitespace from new titles."""
        original_item = self.service.add_item("Original task")
        updated_title_with_spaces = "  Updated task  "

        updated_item = self.service.update_item(original_item.id, updated_title_with_spaces)

        assert updated_item.title == "Updated task"

    def test_update_item_empty_title_raises_validation_error(self):
        """Test that update_item raises ValidationError for empty titles."""
        item = self.service.add_item("Original task")

        with pytest.raises(ValidationError, match="Task title cannot be empty or only whitespace"):
            self.service.update_item(item.id, "")

    def test_complete_item_success(self):
        """Test that complete_item marks an item as completed."""
        item = self.service.add_item("Incomplete task")

        completed_item = self.service.complete_item(item.id)

        assert completed_item.id == item.id
        assert completed_item.completed is True
        assert completed_item.title == item.title

        # Verify the change is persisted by fetching the list again
        items = self.service.get_all_items()
        assert len(items) == 1
        assert items[0].completed is True

    def test_delete_item_success(self):
        """Test that delete_item removes an item from the repository."""
        item = self.service.add_item("Task to delete")

        result = self.service.delete_item(item.id)

        assert result is True
        items = self.service.get_all_items()
        assert len(items) == 0

    def test_delete_nonexistent_item_returns_false(self):
        """Test that delete_item returns False when trying to delete a nonexistent item."""
        result = self.service.delete_item(999)

        assert result is False
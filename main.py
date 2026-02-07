#!/usr/bin/env python3
"""
Todo App - Phase I In-Memory Console Application

A simple console-based todo application that stores data in memory only.
Supports add, list, update, complete, and exit commands.
"""

from src.cli.cli_app import TodoApp


def main():
    """Main entry point for the Todo application."""
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()
# Tasks: Phase I - In-Memory Python Console Todo App

**Feature**: Phase I - In-Memory Python Console Todo App
**Directory**: specs/001-console-todo/
**Created**: 2026-02-07
**Status**: Active

**Dependencies**: Python 3.13+, UV package manager (if using)

## Implementation Strategy

MVP approach focusing on User Story 1 (Add) as the foundation, then building incrementally through each user story. Each story should be independently testable with clear acceptance criteria. Implementation follows clean architecture with separation of concerns between models, repositories, services, and CLI layer.

---

## Phase 1: Setup

Initialize the project structure and basic configuration following the planned architecture.

- [X] T001 Create project directory structure: src/, src/models/, src/repositories/, src/services/, src/cli/, src/utils/, tests/, tests/unit/, tests/integration/
- [X] T002 Create pyproject.toml with project metadata and dependencies (if any)
- [X] T003 Create main.py entry point with basic structure
- [X] T004 Create README.md with project overview and setup instructions

---

## Phase 2: Foundational Components

Create foundational components that will be used across all user stories.

- [X] T005 Create TodoItem data model in src/models/todo.py with id, title, completed attributes
- [X] T006 Create custom exception classes in src/utils/exceptions.py (ValidationError, ItemNotFoundError)
- [X] T007 Create TodoRepository in-memory storage in src/repositories/todo_repository.py
- [X] T008 [P] Create validators in src/utils/validators.py for input validation

---

## Phase 3: User Story 1 - Add New Todo Item (Priority: P1)

As a user, I want to add a new task to my todo list by typing a command in the console. The task should appear in the list with a unique identifier.

**Goal**: Support adding new todo items with unique identifiers via "add" command.

**Independent Test**: Enter "add Buy groceries", verify task appears in list with ID.

- [X] T009 [US1] Implement TodoService.add_item method in src/services/todo_service.py
- [X] T010 [US1] Create unit tests for adding todo items in tests/unit/test_todo_service.py
- [X] T011 [US1] Implement "add" command handler in main.py
- [X] T012 [US1] Test basic add functionality by running manual test

---

## Phase 4: User Story 2 - View Todo List (Priority: P1)

As a user, I want to see all my pending tasks by entering a command to display the current todo list with tasks numbered for easy reference.

**Goal**: Display all tasks with completion status and numbering via "list" command.

**Independent Test**: Add sample tasks and run "list" command to verify correct display.

- [X] T013 [US2] Implement TodoService.get_all_items method in src/services/todo_service.py
- [X] T014 [US2] Create unit tests for viewing todo list in tests/unit/test_todo_service.py
- [X] T015 [US2] Implement "list" command handler in main.py
- [X] T016 [US2] Test list functionality with empty and populated lists

---

## Phase 5: User Story 3 - Update or Modify Existing Task (Priority: P2)

As a user, I want to change the text of an existing task by entering a command with the task number and the updated description.

**Goal**: Allow users to update task descriptions via "update" command.

**Independent Test**: Modify a task and verify the change appears when viewing the list.

- [X] T017 [US3] Implement TodoService.update_item method in src/services/todo_service.py
- [X] T018 [US3] Create unit tests for updating todo items in tests/unit/test_todo_service.py
- [X] T019 [US3] Implement "update" command handler in main.py
- [X] T020 [US3] Test update functionality by changing task descriptions

---

## Phase 6: User Story 4 - Mark Task as Complete (Priority: P2)

As a user, I want to mark completed tasks so they no longer appear in the active list by using a "complete" command.

**Goal**: Mark tasks as complete via "complete" command with appropriate status display.

**Independent Test**: Mark a task complete and verify it appears differently in the list view.

- [X] T021 [US4] Implement TodoService.complete_item method in src/services/todo_service.py
- [X] T022 [US4] Create unit tests for marking tasks complete in tests/unit/test_todo_service.py
- [X] T023 [US4] Implement "complete" command handler in main.py
- [X] T024 [US4] Test complete functionality by marking tasks and viewing list

---

## Phase 7: User Story 5 - Exit the Application (Priority: P1)

As a user, I want to gracefully exit the console application when finished with my todo list.

**Goal**: Provide clean exit mechanism via "exit" command.

**Independent Test**: Enter "exit" command and verify program terminates cleanly.

- [X] T025 [US5] Implement "exit" command handler in main.py
- [X] T026 [US5] Test exit functionality and ensure clean shutdown

---

## Phase 8: Error Handling & Validation

Implement proper error handling and validation for all commands to ensure robust user experience.

- [X] T027 [P] Implement input validation for all commands with appropriate error messages
- [X] T028 [P] Handle edge cases like invalid task IDs, empty descriptions
- [X] T029 [P] Add command parsing validation and error reporting
- [X] T030 [P] Create comprehensive error handling tests in tests/unit/test_error_handling.py

---

## Phase 9: CLI Loop & User Experience

Implement the main command loop and enhance user experience with proper prompting and messaging.

- [X] T031 Create main CLI loop in main.py for continuous command processing
- [X] T032 Add proper user prompts and output formatting
- [X] T033 Implement command routing logic to delegate to appropriate handlers
- [X] T034 Create integration tests in tests/integration/cli_integration_test.py

---

## Phase 10: Polish & Cross-Cutting Concerns

Final touches and quality improvements.

- [X] T035 Add comprehensive documentation to all public methods
- [X] T036 Perform full manual testing of all user stories
- [X] T037 Optimize performance and memory usage for large lists
- [X] T038 Create usage examples in README.md
- [X] T039 Run all tests and ensure 100% success rate

---

## Dependencies

- User Story 1 must complete before US2, US3, US4 (need items to view/update/complete)
- User Story 2 may be implemented in parallel with US3, US4 after US1 foundation
- User Story 5 can be implemented anytime but should be available before testing

## Parallel Execution Opportunities

- T006, T007, T008 (foundational components) can be developed in parallel
- T013-T016 (US2) and T017-T020 (US3) can be developed in parallel after US1
- T021-T024 (US4) can be developed in parallel with US2/US3
- T027-T030 (error handling) can be developed alongside other features

## MVP Scope

Core MVP includes Phase 1, 2, and 3 (basic add functionality), sufficient for a minimally viable todo application.
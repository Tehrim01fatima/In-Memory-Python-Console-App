# Implementation Plan: In-Memory Python Console Todo Application

**Branch**: `001-console-todo` | **Date**: 2026-01-01 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-console-todo/spec.md`

## Summary

Implement a deterministic, in-memory, console-based Todo application using Python
standard library only. The application provides CRUD operations for todo items
with clear separation between data model, business logic, and user interface layers.
The implementation prioritizes code clarity, predictable behavior, and clean structure
as the foundation for future scalable phases.

## Technical Context

**Language/Version**: Python 3.x (standard library only)
**Primary Dependencies**: None (standard library only)
**Storage**: In-memory (Python list/dict)
**Testing**: Manual testing via console interaction
**Target Platform**: Terminal/CLI (cross-platform Python)
**Project Type**: Single CLI application
**Performance Goals**: N/A - Phase I focuses on correctness over performance
**Constraints**: No file storage, no databases, no external libraries, no persistence
**Scale/Scope**: Single-user session, typically 1-100 todos

## Constitution Check

- [x] **I. Simplicity First, Scalability Later**: Using Python standard library only, no external dependencies
- [x] **II. Deterministic Behavior in Early Phases**: In-memory storage, explicit state transitions, predictable outputs
- [x] **III. Clear Separation of Concerns**: Separate modules for data model (todo.py), UI (ui.py), and control flow (main.py)
- [x] **IV. Incremental Evolution Without Breaking Guarantees**: Clean structure enables Phase II extension
- [x] **V. Human-Readable, Maintainable Code**: Clear naming, single responsibility per module
- [x] **VI. AI-Assisted Features Remain Explainable**: N/A in Phase I

**GATE**: PASSED - Ready to proceed with implementation

## Project Structure

### Documentation (this feature)

```text
specs/001-console-todo/
├── plan.md              # This file (/sp.plan command output)
├── spec.md              # Feature specification (/sp.specify output)
└── checklists/
    └── requirements.md  # Quality validation checklist
```

### Source Code (repository root)

```text
main.py                 # Application entry point and control flow
todo.py                 # Todo data model and business logic
ui.py                   # Console input/output handling
```

**Structure Decision**: Three-file structure with clear separation:
- `todo.py` handles data model and core operations (CRUD)
- `ui.py` handles all user interaction (menus, input, output)
- `main.py` orchestrates the application flow

No tests/ directory for Phase I - manual testing only per constitution.

## Milestones

### Milestone 1 — Project Initialization

1. Create the three required files: `main.py`, `todo.py`, `ui.py`
2. Verify application starts with `python main.py`
3. Display initial menu to confirm basic structure works
4. No placeholder or unused files allowed

**Verification**: Running `python main.py` displays menu without errors

### Milestone 2 — Todo Data Model & Core Logic

1. Define Todo data structure with attributes:
   - id (int, auto-incremented)
   - title (str, required)
   - description (str, optional, defaults to empty)
   - status (str, "pending" or "completed")
2. Implement in-memory storage using a list
3. Implement core operations:
   - `create_todo(title, description)` -> Todo
   - `list_todos()` -> list of todos
   - `get_todo_by_id(todo_id)` -> Todo or None
   - `update_todo(todo_id, title, description, status)` -> bool
   - `delete_todo(todo_id)` -> bool
4. Implement deterministic ID auto-increment (next_id counter)
5. Keep this layer pure - no print/input statements

**Verification**: All functions return expected values, no I/O in todo.py

### Milestone 3 — Console UI Layer

1. Implement menu rendering function showing available actions
2. Implement input collection for:
   - Menu selection (1-7)
   - Todo title (non-empty string)
   - Todo description (optional string)
   - Todo ID (integer)
   - Status selection (pending/completed)
3. Validate all user inputs before passing to logic layer
4. Display clear success and error messages
5. No business logic in ui.py - pure presentation layer

**Verification**: All user inputs validated, clear messages displayed

### Milestone 4 — Application Control Flow

1. Implement main loop in main.py:
   - Display menu
   - Capture user choice
   - Dispatch to appropriate handlers
   - Continue until exit command
2. Handle each menu option:
   - 1: Create todo (collect title/description via ui.py)
   - 2: List all todos
   - 3: View single todo (prompt for ID)
   - 4: Update todo (prompt for ID and fields)
   - 5: Delete todo (prompt for ID)
   - 6: Exit
3. Gracefully terminate on exit command

**Verification**: Application runs, responds to all menu options, exits cleanly

### Milestone 5 — Error Handling & Edge Cases

1. Handle invalid menu selections (non-numeric, out of range)
2. Handle empty todo list states (list, view, delete when empty)
3. Handle non-existent todo IDs (view, update, delete)
4. Prevent empty titles (create and update)
5. Prevent invalid status values (only "pending" or "completed")
6. Application must never crash due to user input

**Verification**: All error scenarios produce clear messages, no crashes

### Milestone 6 — Manual Testing & Validation

1. Test all CRUD operations:
   - Create todos with various title/description combinations
   - List todos and verify all details shown
   - View individual todos by ID
   - Update titles, descriptions, and statuses
   - Delete todos and verify removal
2. Test edge cases:
   - Delete non-existent todo
   - Update completed todo back to pending
   - List when no todos exist
   - View non-existent ID
   - Create todo with empty title (should error)
   - Invalid menu selection
3. Confirm deterministic behavior (same inputs = same outputs)
4. Confirm no state persistence after restart (fresh session = empty list)

**Verification**: All tests pass, no crashes, predictable behavior

### Milestone 7 — Final Review & Cleanup

1. Remove any unused code or dead branches
2. Ensure consistent naming conventions throughout
3. Add minimal inline comments where intent is unclear
4. Re-run full manual test pass
5. Confirm Phase I acceptance criteria from spec are met:
   - [SC-001] Application starts with `python main.py`
   - [SC-002] All CRUD operations work without crashes
   - [SC-003] Clear error messages within 1 second
   - [SC-004] State maintained throughout session
   - [SC-005] Full workflow completes in under 5 minutes
   - [SC-006] IDs remain unique, no reuse after deletion
   - [SC-007] Plain text output (no emojis)

**Verification**: Codebase clean, readable, all acceptance criteria met

## Completion Gate

Phase I is complete when:
- All 7 milestones are satisfied
- Application behaves predictably (deterministic outputs)
- Codebase is clean and readable
- No scope violations (no file persistence, no external libraries)
- Ready to be extended in Phase II without refactor

**Final Checklist**:
- [ ] `python main.py` starts application
- [ ] Create, List, View, Update, Delete all work
- [ ] Error handling for all edge cases
- [ ] No crashes from any user input
- [ ] In-memory only (no files, no persistence)
- [ ] Three clean files: main.py, todo.py, ui.py
- [ ] All Phase I acceptance criteria verified

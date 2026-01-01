# Tasks: In-Memory Python Console Todo Application

**Input**: Design documents from `/specs/001-console-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: Manual testing only per constitution - no automated test tasks

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Project Initialization)

**Purpose**: Create the three required files per implementation plan

- [x] T001 Create main.py with minimal entry point and stub functions in the repository root
- [x] T002 Create todo.py with Todo class stub and functions stub in the repository root
- [x] T003 Create ui.py with menu display and input functions stub in the repository root

**Checkpoint**: All three files exist at repository root

---

## Phase 2: Foundational (Todo Data Model & Core Logic)

**Purpose**: Implement the Todo data structure and in-memory storage - REQUIRED before any user story

**CRITICAL**: This phase MUST be complete before any user story implementation

- [x] T004 [P] Define Todo class with id, title, description, status attributes in todo.py
- [x] T005 [P] Implement Todo.__init__ method with id auto-increment logic in todo.py
- [x] T006 Implement in-memory storage using a list variable in todo.py
- [x] T007 Implement next_id counter for deterministic ID generation in todo.py
- [x] T008 Implement create_todo(title, description) function in todo.py (returns Todo, adds to storage)
- [x] T009 Implement list_todos() function in todo.py (returns list of all todos)
- [x] T010 Implement get_todo_by_id(todo_id) function in todo.py (returns Todo or None)
- [x] T011 Implement update_todo(todo_id, title, description, status) function in todo.py (returns bool)
- [x] T012 Implement delete_todo(todo_id) function in todo.py (returns bool)

**Verification**: All functions return expected values, no print/input in todo.py

**Checkpoint**: Todo data model and CRUD operations complete - user stories can now begin

---

## Phase 3: User Story 1 - Create and List Todos (Priority: P1) MVP

**Goal**: Users can create new todo items and see a list of all their todos

**Independent Test**: Create todos with various titles/descriptions and list them. Delivers a working todo tracking system.

- [x] T013 [P] [US1] Implement display_menu function showing create/list/view/update/delete/exit options in ui.py
- [x] T014 [P] [US1] Implement get_menu_choice function that validates numeric input (1-6) in ui.py
- [x] T015 [P] [US1] Implement get_todo_title function that collects and validates non-empty title in ui.py
- [x] T016 [P] [US1] Implement get_todo_description function that collects optional description in ui.py
- [x] T017 [US1] Implement list_todos_display function that formats and prints all todos in ui.py
- [x] T018 [US1] Wire create todo flow in main.py: menu option 1 collects title/description via ui.py, calls create_todo, displays success
- [x] T019 [US1] Wire list todos flow in main.py: menu option 2 calls list_todos, displays via ui.py

**Acceptance Scenarios Verified**:
1. Todo created with title "Buy groceries" gets status "pending" and unique ID
2. Listing todos shows all todos with ID, title, status, description
3. Creating todo with no description saves with empty description field

**Checkpoint**: User Story 1 complete - users can create and list todos

---

## Phase 4: User Story 2 - View and Update Individual Todos (Priority: P1)

**Goal**: Users can view a specific todo and update its title, description, and status

**Independent Test**: View todo by ID and update its title/description/status. Delivers full CRUD capability.

- [x] T020 [P] [US2] Implement get_todo_id function that validates integer input for todo ID in ui.py
- [x] T021 [P] [US2] Implement get_update_choice function for selecting which field to update in ui.py
- [x] T022 [P] [US2] Implement get_new_title function for updating title with validation in ui.py
- [x] T023 [P] [US2] Implement get_new_description function for updating description in ui.py
- [x] T024 [P] [US2] Implement get_new_status function that validates "pending" or "completed" input in ui.py
- [x] T025 [US2] Implement display_todo function that shows single todo details in ui.py
- [x] T026 [US2] Implement view_single_todo flow in main.py: menu option 3 prompts for ID, calls get_todo_by_id, displays via ui.py
- [x] T027 [US2] Implement update_todo flow in main.py: menu option 4 prompts for ID and field to update, calls update_todo, displays result

**Acceptance Scenarios Verified**:
1. Viewing todo 1 shows complete details (ID, title, description, status)
2. Updating todo 1 title changes it permanently
3. Updating todo 1 status from "pending" to "completed" persists
4. Updating todo 1 description stores and displays new value

**Checkpoint**: User Story 2 complete - users can view and update individual todos

---

## Phase 5: User Story 3 - Delete Todos (Priority: P1)

**Goal**: Users can delete todo items by ID, removing them permanently

**Independent Test**: Create todos and delete them by ID. Delivers complete lifecycle management.

- [x] T028 [US3] Implement delete_todo flow in main.py: menu option 5 prompts for ID, calls delete_todo, displays result

**Acceptance Scenarios Verified**:
1. Deleting todo 1 removes it permanently from the list
2. Deleting non-existent ID shows appropriate error message
3. Deleting one todo does not affect other todos

**Checkpoint**: User Story 3 complete - users can delete todos

---

## Phase 6: User Story 4 - Application Navigation and Exit (Priority: P2)

**Goal**: Clear menu navigation and graceful exit

**Independent Test**: Navigate menu, perform actions, exit cleanly.

- [x] T029 [US4] Implement main loop in main.py that continuously displays menu, captures choice, dispatches to handlers
- [x] T030 [US4] Wire exit flow in main.py: menu option 6 terminates loop and exits gracefully

**Acceptance Scenarios Verified**:
1. Application displays clear menu on start
2. Invalid menu selection shows error and re-displays menu
3. Exiting terminates cleanly without errors

**Checkpoint**: All user stories complete

---

## Phase 7: Error Handling & Edge Cases (Polish)

**Purpose**: Handle all error scenarios gracefully - application must never crash

- [x] T031 Handle invalid menu selections (non-numeric, out of range) in get_menu_choice in ui.py
- [x] T032 Handle empty todo list state in list_todos_display in ui.py (show "No todos" message)
- [x] T033 Handle non-existent todo ID in view_single_todo flow (error message)
- [x] T034 Handle non-existent todo ID in update flow (error message)
- [x] T035 Handle non-existent todo ID in delete flow (error message)
- [x] T036 Prevent empty title in get_todo_title in ui.py (loop until valid input)
- [x] T037 Prevent empty title in get_new_title in ui.py (loop until valid input)
- [x] T038 Validate status input in get_new_status in ui.py (only "pending" or "completed")
- [x] T039 Ensure ID uniqueness is maintained (no ID reuse after deletion)

**Checkpoint**: All edge cases handled, no crashes possible

---

## Phase 8: Final Review & Cleanup

**Purpose**: Polish code and verify all acceptance criteria

- [x] T040 Remove any unused code or dead branches across all files
- [x] T041 Ensure consistent naming conventions across main.py, todo.py, ui.py
- [x] T042 Add minimal inline comments where intent is unclear
- [x] T043 Re-run full manual test pass covering all user stories
- [x] T044 Verify all Phase I acceptance criteria from spec.md:
  - [SC-001] `python main.py` starts application without errors
  - [SC-002] All CRUD operations work without crashes
  - [SC-003] Clear error messages for all invalid inputs
  - [SC-004] State maintained throughout session
  - [SC-005] Full workflow completes in under 5 minutes
  - [SC-006] IDs remain unique, no reuse after deletion
  - [SC-007] Plain text output (no emojis or graphical characters)

**Checkpoint**: Phase I complete and ready for Phase II

---

## Dependencies & Execution Order

### Phase Dependencies

| Phase | Depends On | Blocks |
|-------|-----------|--------|
| Phase 1: Setup | None | Phase 2 |
| Phase 2: Foundational | Phase 1 | Phases 3-6 |
| Phase 3: US1 | Phase 2 | Phase 7 |
| Phase 4: US2 | Phase 2 | Phase 7 |
| Phase 5: US3 | Phase 2 | Phase 7 |
| Phase 6: US4 | Phase 2 | Phase 7 |
| Phase 7: Error Handling | Phases 3-6 | Phase 8 |
| Phase 8: Final Review | Phase 7 | Complete |

### User Story Dependencies

- **User Story 1 (Create/List)**: Depends on Phase 2 - No other story dependencies
- **User Story 2 (View/Update)**: Depends on Phase 2 - No other story dependencies
- **User Story 3 (Delete)**: Depends on Phase 2 - No other story dependencies
- **User Story 4 (Navigation)**: Depends on Phase 2 - Integrates all other stories

All user stories can proceed in parallel after Phase 2 since they work on different files:
- todo.py (all stories - Phase 2 complete)
- ui.py (US1: T013-T019, US2: T020-T025, US3: T028, US4: T029-T030)
- main.py (US1: T018-T019, US2: T026-T027, US3: T028, US4: T029-T030)

### Within Each User Story

- todo.py CRUD operations (Phase 2) must be complete
- UI functions can be implemented in any order within [P] marked tasks
- Main.py wiring depends on both todo.py and ui.py components

---

## Parallel Execution Examples

### After Phase 2 (Foundational) is Complete

All user stories can proceed in parallel:

**Developer 1 - User Story 1 (Create/List)**:
- T013, T014, T015, T016, T017 (ui.py functions)
- T018, T019 (main.py wiring)

**Developer 2 - User Story 2 (View/Update)**:
- T020, T021, T022, T023, T024, T025 (ui.py functions)
- T026, T027 (main.py wiring)

**Developer 3 - User Stories 3 & 4 (Delete/Navigation)**:
- T028 (US3 delete flow)
- T029, T030 (US4 navigation and exit)

### Within User Story 1

```bash
# All these can run in parallel (different files):
T013: Implement display_menu in ui.py
T014: Implement get_menu_choice in ui.py
T015: Implement get_todo_title in ui.py
T016: Implement get_todo_description in ui.py
T017: Implement list_todos_display in ui.py
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T003)
2. Complete Phase 2: Foundational (T004-T012)
3. Complete Phase 3: User Story 1 (T013-T019)
4. **STOP and VALIDATE**: Test create and list operations
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Phase 1 + Phase 2 → Foundation ready
2. Add User Story 1 → Test → Demo (MVP!)
3. Add User Story 2 → Test → Demo
4. Add User Story 3 → Test → Demo
5. Add User Story 4 → Test → Demo
6. Add Error Handling → Polish
7. Final Review → Phase I Complete

### Recommended: Sequential (Single Developer)

1. Phase 1: Setup (all 3 files)
2. Phase 2: Foundational (all CRUD operations)
3. Phase 3: User Story 1 (create + list)
4. Phase 4: User Story 2 (view + update)
5. Phase 5: User Story 3 (delete)
6. Phase 6: User Story 4 (navigation + exit)
7. Phase 7: Error handling (all edge cases)
8. Phase 8: Final review and cleanup

---

## Summary

| Metric | Value |
|--------|-------|
| **Total Tasks** | 44 |
| **Phase 1: Setup** | 3 tasks |
| **Phase 2: Foundational** | 9 tasks |
| **Phase 3: US1 Create/List** | 7 tasks |
| **Phase 4: US2 View/Update** | 8 tasks |
| **Phase 5: US3 Delete** | 1 task |
| **Phase 6: US4 Navigation** | 2 tasks |
| **Phase 7: Error Handling** | 9 tasks |
| **Phase 8: Final Review** | 5 tasks |

**MVP Scope**: Phases 1-3 (Setup + Foundational + US1) - creates and lists todos

**Parallel Opportunities**: 19 tasks marked [P] can run in parallel (different files, no dependencies)

**Files Created**:
- `todo.py` - Data model and CRUD operations
- `ui.py` - Console input/output handling
- `main.py` - Application control flow

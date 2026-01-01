---
id: "0002"
title: "Create Phase I console todo plan"
stage: "plan"
date: "2026-01-01"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "console-todo"
branch: "001-console-todo"
user: "human"
command: "/sp.plan"
labels: [plan,console-app,phase-i,implementation]
links:
  spec: "specs/001-console-todo/spec.md"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - specs/001-console-todo/plan.md
tests: []
---

## Prompt

/sp.plan

Project: Phase I — In-Memory Python Console Todo Application

Goal:
Implement a deterministic, in-memory, console-based Todo application
using Python standard library only, with clean structure and predictable behavior.

Guiding Rules:
- Follow /sp.constitution and /sp.specify exactly
- Do not introduce features outside Phase I scope
- Favor clarity over cleverness
- No persistence, no external libraries

Milestones & Steps:

Milestone 1 — Project Initialization
1. Create a clean project directory
2. Add only the required files:
   - main.py
   - todo.py
   - ui.py
3. Verify application starts with:
   - `python main.py`
4. No placeholder or unused files allowed

Milestone 2 — Todo Data Model & Core Logic
1. Define Todo data structure:
   - id
   - title
   - description
   - status
2. Implement in-memory storage:
   - Use a controlled list or dictionary
3. Implement core operations:
   - create_todo
   - list_todos
   - get_todo_by_id
   - update_todo
   - delete_todo
4. Ensure ID auto-increment logic is deterministic
5. No input/output logic in this layer

Milestone 3 — Console UI Layer
1. Implement menu rendering:
   - Display available actions clearly
2. Implement input collection:
   - Menu selection
   - Todo fields
3. Validate all user inputs before passing to logic
4. Display clear success and error messages
5. No business logic in UI layer

Milestone 4 — Application Control Flow
1. Implement main loop in main.py:
   - Display menu
   - Capture user choice
   - Dispatch to appropriate handlers
2. Ensure application continues until explicit exit
3. Gracefully terminate on exit command
4. No infinite loops without exit condition

Milestone 5 — Error Handling & Edge Cases
1. Handle invalid menu selections
2. Handle empty todo list states
3. Handle non-existent todo IDs
4. Prevent empty titles
5. Prevent invalid status updates
6. Application must never crash due to user input

Milestone 6 — Manual Testing & Validation
1. Test all CRUD operations manually
2. Test edge cases:
   - Delete non-existent todo
   - Update completed todo
   - List when no todos exist
3. Confirm deterministic behavior
4. Confirm no state persistence after restart

Milestone 7 — Final Review & Cleanup
1. Remove unused code
2. Ensure consistent naming conventions
3. Add minimal inline comments where intent is unclear
4. Re-run full manual test pass
5. Confirm Phase I acceptance criteria are met

Constraints Enforcement:
- Python standard library only
- In-memory state only
- Single responsibility per file
- No future-phase scaffolding

Completion Gate:
Phase I is complete when:
- All milestones are satisfied
- Application behaves predictably
- Codebase is clean and readable
- No scope violations are present
- Ready to be extended in Phase II without refactor

Do Not:
- Add file persistence
- Add databases
- Add external libraries

## Response snapshot

Created implementation plan at `specs/001-console-todo/plan.md` with:
- Technical context (Python stdlib, in-memory storage, manual testing)
- Constitution check: All 6 principles passed
- Project structure: Three-file structure (main.py, todo.py, ui.py)
- 7 detailed milestones with verification criteria
- Completion gate checklist for Phase I acceptance

## Outcome

- ✅ Impact: Phase I implementation plan complete with 7 milestones and clear verification steps
- 🧪 Tests: N/A - planning phase
- 📁 Files: 1 created (plan.md)
- 🔁 Next prompts: /sp.tasks to generate task list or /sp.implement to start coding
- 🧠 Reflection: Detailed milestones map directly to user-provided steps; clear completion gate defined

## Evaluation notes (flywheel)

- Failure modes observed: "null"
- Graders run and results (PASS/FAIL): "N/A"
- Prompt variant (if applicable): "null"
- Next experiment (smallest change to try): "null"

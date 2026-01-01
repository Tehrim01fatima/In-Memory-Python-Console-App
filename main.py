"""Todo Application - Main entry point and control flow."""

import ui
from todo import (
    create_todo,
    list_todos,
    get_todo_by_id,
    update_todo,
    delete_todo,
)


def main():
    """Main application entry point."""
    while True:
        ui.display_menu()
        choice = ui.get_menu_choice()

        if choice == 1:
            handle_create()
        elif choice == 2:
            handle_list()
        elif choice == 3:
            handle_view()
        elif choice == 4:
            handle_update()
        elif choice == 5:
            handle_delete()
        elif choice == 6:
            print("\nThank you for using Todo Application. Goodbye!")
            break


def handle_create():
    """Handle creating a new todo."""
    title = ui.get_todo_title()
    description = ui.get_todo_description()
    todo = create_todo(title, description)
    ui.show_message(f"Todo created successfully! (ID: {todo.id})")


def handle_list():
    """Handle listing all todos."""
    todos = list_todos()
    ui.list_todos_display(todos)


def handle_view():
    """Handle viewing a single todo."""
    todo_id = ui.get_todo_id()
    todo = get_todo_by_id(todo_id)
    ui.display_todo(todo)


def handle_update():
    """Handle updating an existing todo."""
    todo_id = ui.get_todo_id()
    todo = get_todo_by_id(todo_id)
    if todo is None:
        ui.show_error(f"Todo with ID {todo_id} not found.")
        return

    update_choice = ui.get_update_choice()

    if update_choice == 5:
        ui.show_message("Update cancelled.")
        return

    if update_choice in (1, 4):
        new_title = ui.get_new_title()
    else:
        new_title = None

    if update_choice in (2, 4):
        new_description = ui.get_new_description()
    else:
        new_description = None

    if update_choice in (3, 4):
        new_status = ui.get_new_status()
    else:
        new_status = None

    success = update_todo(
        todo_id,
        title=new_title,
        description=new_description,
        status=new_status
    )

    if success:
        ui.show_message("Todo updated successfully!")
    else:
        ui.show_error("Failed to update todo.")


def handle_delete():
    """Handle deleting a todo."""
    todo_id = ui.get_todo_id()
    todo = get_todo_by_id(todo_id)
    if todo is None:
        ui.show_error(f"Todo with ID {todo_id} not found.")
        return

    success = delete_todo(todo_id)
    if success:
        ui.show_message("Todo deleted successfully!")
    else:
        ui.show_error("Failed to delete todo.")


if __name__ == "__main__":
    main()

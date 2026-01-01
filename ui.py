"""Console input/output handling."""


def display_menu():
    """Display the main menu."""
    print("\n=== Todo Application ===")
    print("1. Create a new todo")
    print("2. List all todos")
    print("3. View a single todo")
    print("4. Update a todo")
    print("5. Delete a todo")
    print("6. Exit")
    print("=======================")


def get_menu_choice():
    """Get and validate menu choice from user."""
    # TODO: Implement with error handling (Phase 7)
    while True:
        try:
            choice = int(input("\nEnter your choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Please enter a valid number.")


def get_todo_title():
    """Get todo title from user with validation."""
    # TODO: Implement with empty title prevention (Phase 7)
    while True:
        title = input("Enter todo title: ").strip()
        if title:
            return title
        print("Title cannot be empty. Please enter a title.")


def get_todo_description():
    """Get optional todo description from user."""
    desc = input("Enter description (optional, press Enter to skip): ").strip()
    return desc


def list_todos_display(todos):
    """Display all todos in a formatted list."""
    if not todos:
        print("No todos found.")
        return
    print("\n--- Your Todos ---")
    for todo in todos:
        desc = todo.description if todo.description else "(no description)"
        print(f"[{todo.id}] {todo.title} - {todo.status}")
        print(f"    Description: {desc}")
    print("------------------\n")


def get_todo_id():
    """Get and validate todo ID from user."""
    # TODO: Implement with validation (Phase 4)
    while True:
        try:
            todo_id = int(input("Enter todo ID: "))
            if todo_id > 0:
                return todo_id
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")


def get_update_choice():
    """Get user's choice for which field to update."""
    print("\nWhat would you like to update?")
    print("1. Title")
    print("2. Description")
    print("3. Status")
    print("4. All fields")
    print("5. Cancel")
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if 1 <= choice <= 5:
                return choice
            print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")


def get_new_title():
    """Get new title for update."""
    while True:
        title = input("Enter new title: ").strip()
        if title:
            return title
        print("Title cannot be empty. Please enter a title.")


def get_new_description():
    """Get new description for update."""
    desc = input("Enter new description (press Enter to clear): ").strip()
    return desc


def get_new_status():
    """Get and validate new status for update."""
    # TODO: Implement with validation (Phase 7)
    print("Available statuses: pending, completed")
    while True:
        status = input("Enter new status: ").strip().lower()
        if status in ("pending", "completed"):
            return status
        print("Please enter 'pending' or 'completed'.")


def display_todo(todo):
    """Display a single todo in detail."""
    if todo is None:
        print("Todo not found.")
        return
    print(f"\n--- Todo #{todo.id} ---")
    print(f"Title: {todo.title}")
    print(f"Description: {todo.description if todo.description else '(no description)'}")
    print(f"Status: {todo.status}")
    print("-------------------\n")


def show_message(message):
    """Display a message to the user."""
    print(message)


def show_error(message):
    """Display an error message."""
    print(f"Error: {message}")

"""Todo data model and core operations."""

# In-memory storage for todos
_todos = []
_next_id = 1


class Todo:
    """Represents a single todo item."""

    def __init__(self, title, description, status="pending"):
        global _next_id
        self.id = _next_id
        _next_id += 1
        self.title = title
        self.description = description
        self.status = status

    def __repr__(self):
        return f"Todo(id={self.id}, title={self.title!r}, status={self.status!r})"


def create_todo(title, description=""):
    """Create a new todo and add to storage."""
    todo = Todo(title, description)
    _todos.append(todo)
    return todo


def list_todos():
    """Return list of all todos."""
    return _todos.copy()


def get_todo_by_id(todo_id):
    """Return todo with given ID, or None if not found."""
    for todo in _todos:
        if todo.id == todo_id:
            return todo
    return None


def update_todo(todo_id, title=None, description=None, status=None):
    """Update todo with given ID. Returns True if successful."""
    todo = get_todo_by_id(todo_id)
    if todo is None:
        return False
    if title is not None:
        todo.title = title
    if description is not None:
        todo.description = description
    if status is not None:
        todo.status = status
    return True


def delete_todo(todo_id):
    """Delete todo with given ID. Returns True if successful."""
    for i, todo in enumerate(_todos):
        if todo.id == todo_id:
            del _todos[i]
            return True
    return False

from storage import load_tasks, save_tasks
from utils import get_next_id, find_task, display_task, current_time


def add_task(description):
    """Create a new task."""

    tasks = load_tasks()

    task = {
        "id": get_next_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": current_time(),
        "updatedAt": current_time()
    }

    tasks.append(task)

    save_tasks(tasks)

    print(
        f'Task added successfully '
        f'(ID: {task["id"]})'
    )


def update_task(task_id, description):
    """Update an existing task."""

    tasks = load_tasks()

    task = find_task(tasks, task_id)

    if task is None:
        print(
            f"Error: Task with ID "
            f"{task_id} not found."
        )
        return

    task["description"] = description
    task["updatedAt"] = current_time()

    save_tasks(tasks)

    print(
        f"Task {task_id} "
        f"updated successfully."
    )


def delete_task(task_id):
    """Delete a task."""

    tasks = load_tasks()

    task = find_task(tasks, task_id)

    if task is None:
        print(
            f"Error: Task with ID "
            f"{task_id} not found."
        )
        return

    tasks.remove(task)

    save_tasks(tasks)

    print(
        f"Task {task_id} "
        f"deleted successfully."
    )


def change_status(task_id, status):
    """Change task status."""

    tasks = load_tasks()

    task = find_task(tasks, task_id)

    if task is None:
        print(
            f"Error: Task with ID "
            f"{task_id} not found."
        )
        return

    task["status"] = status
    task["updatedAt"] = current_time()

    save_tasks(tasks)

    print(
        f"Task {task_id} "
        f"marked as {status}."
    )


def list_tasks(status=None):
    """List tasks, optionally filtered by status."""

    tasks = load_tasks()

    if status is not None:

        tasks = [
            task
            for task in tasks
            if task["status"] == status
        ]

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        display_task(task)
from datetime import datetime


def get_next_id(tasks):
    """Generate the next available task ID."""

    if not tasks:
        return 1

    return max(task["id"] for task in tasks) + 1


def find_task(tasks, task_id):
    """Find a task using its ID."""

    for task in tasks:

        if task["id"] == task_id:
            return task

    return None


def display_task(task):
    """Display one task."""

    print(
        f'[{task["id"]}] '
        f'{task["description"]} '
        f'({task["status"]})'
    )


def current_time():
    """Return the current date and time."""

    return datetime.now().isoformat(
        timespec="seconds"
    )
import json
import os
import sys


FILE_NAME = "Tasks.json"


def load_tasks():
    """Load tasks from the JSON file."""

    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Error: Tasks.json must contain a list of tasks.")
            sys.exit(1)

        return data

    except json.JSONDecodeError:
        print("Error: Tasks.json contains invalid JSON.")
        sys.exit(1)

    except OSError as error:
        print(f"Error reading Tasks.json: {error}")
        sys.exit(1)


def save_tasks(tasks):
    """Save tasks to the JSON file."""

    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)

    except OSError as error:
        print(f"Error writing to Tasks.json: {error}")
        sys.exit(1)
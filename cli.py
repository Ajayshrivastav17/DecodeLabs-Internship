import argparse

from tasks import (
    add_task,
    update_task,
    delete_task,
    change_status,
    list_tasks
)


def create_parser():

    parser = argparse.ArgumentParser(
        description="CLI Task Tracker"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    
    # ADD
    

    add_parser = subparsers.add_parser(
        "add",
        help="Add a new task"
    )

    add_parser.add_argument(
        "description",
        help="Task description"
    )

    
    # UPDATE
    

    update_parser = subparsers.add_parser(
        "update",
        help="Update a task"
    )

    update_parser.add_argument(
        "id",
        type=int,
        help="Task ID"
    )

    update_parser.add_argument(
        "description",
        help="New task description"
    )

    
    # DELETE
    

    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete a task"
    )

    delete_parser.add_argument(
        "id",
        type=int,
        help="Task ID"
    )

    
    # MARK IN PROGRESS
    

    progress_parser = subparsers.add_parser(
        "mark-in-progress",
        help="Mark task as in progress"
    )

    progress_parser.add_argument(
        "id",
        type=int,
        help="Task ID"
    )


    # MARK DONE
    

    done_parser = subparsers.add_parser(
        "mark-done",
        help="Mark task as done"
    )

    done_parser.add_argument(
        "id",
        type=int,
        help="Task ID"
    )

    
    # LIST

    list_parser = subparsers.add_parser(
        "list",
        help="List tasks"
    )

    list_parser.add_argument(
        "filter",
        nargs="?",
        choices=[
            "done",
            "not-done",
            "in-progress"
        ],
        help="Optional task filter"
    )

    return parser


def run_cli():

    parser = create_parser()

    args = parser.parse_args()

    # ADD

    if args.command == "add":

        add_task(args.description)

    # UPDATE

    elif args.command == "update":

        update_task(
            args.id,
            args.description
        )

    # DELETE

    elif args.command == "delete":

        delete_task(args.id)

    # MARK IN PROGRESS

    elif args.command == "mark-in-progress":

        change_status(
            args.id,
            "in-progress"
        )

    # MARK DONE

    elif args.command == "mark-done":

        change_status(
            args.id,
            "done"
        )

    # LIST

    elif args.command == "list":

        if args.filter == "done":

            list_tasks("done")

        elif args.filter == "not-done":

            list_tasks("todo")

        elif args.filter == "in-progress":

            list_tasks("in-progress")

        else:

            list_tasks()

    else:

        parser.print_help()
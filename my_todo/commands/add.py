# write a function that adds a task to the todo list
from fileinput import close
import json
import click

@click.command()
@click.option('--description','-d', help='Add a task to the todo list.')
@click.option('--isdone', '-i', default="false", help='Add a status to the todo list.')
def cli(description, isdone):
    """Add a task to the todo list."""

    with open('./db/todo.json', 'r') as f:
        todo_list = json.load(f)
        todo_list.append({'id': len(todo_list) + 1, 'description': description, 'status': isdone})

    with open('./db/todo.json', 'w') as f:
        json.dump(todo_list, f)
        close
    print('Added task to the todo list.')



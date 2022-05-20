import click
import json

@click.command()
def cli():
    """Clear all tasks in database."""
    if click.confirm('Are you sure you want to delete all tasks?'):
        with open('./../db/todo.json', 'w') as f:
            json.dump([], f)
        print('Deleted all tasks from the todo list.')
    else:
        print('Aborted.')
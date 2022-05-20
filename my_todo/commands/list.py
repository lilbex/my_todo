import click
import json

@click.command()
def cli():
    """List all task."""
    with open('./db/todo.json', 'r') as f:
        todo_list = json.load(f)
        for todo in todo_list:
          id = todo['id']
          d = todo['description']
          s = todo['isdone']

          click.secho(f'{id} |  {d}  => {s}', bg='blue', fg='white',bold=True)

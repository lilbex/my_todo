import click
import json


def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()


@click.command()
@click.option('--id','-i', help='Enter the id of todo to be deleted')
@click.option('--yes','-y', is_flag=True, callback=abort_if_false,
              expose_value=False,
              prompt='Are you sure you want to delete this task?')
def cli(id: int):
    """Delete a task by ID."""
    # delete a task by ID
    with open('./db/todo.json', 'r') as f:
        todo_list = json.load(f)
        for todo in todo_list:
            if todo['id'] == int(id):
                todo_list.remove(todo)
                break
    with open('./db/todo.json', 'w') as f:
        json.dump(todo_list, f)
    print('Deleted task from the todo list.')

        
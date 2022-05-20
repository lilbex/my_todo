from xmlrpc.client import Boolean
import click
import json

@click.command()
@click.option('--option','-o', help='Enter the status of task to true or false', type=click.Choice([True, False,'true','false','True', 'False', 'TRUE', 'FALSE']))
@click.option('--id','-i', help='Enter the id of task to be updated', type=click.INT)
def cli(option,id):
  """Set the task of a task. True if it has been completed and False if it is not completed"""
  with open('./db/todo.json', 'r') as f:
    todo_list = json.load(f)
    for todo in todo_list:
      if todo['id'] == int(id):
        todo['isdone'] = option
        break
  with open('./db/todo.json', 'w') as f:
    json.dump(todo_list, f)
  print('Updated status of task.')
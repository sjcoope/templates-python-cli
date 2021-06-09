import click
from cli import utils
from cli.entities.entity1 import Entity1
from cli.proxies import proxy1
from cli.utils import general_utils

@click.group()
def command1():
    """
    Command 1 Commands...
    """
    pass

@command1.command("sample")
@click.option("-n", "--name")
def cmd_sample(name):

    # Simulate handling input.
    print(f'Sample: {name}')

    # Simulate building and formatting a dataset
    data = proxy1.get_data()
    entities = []
    for i in data:
      entities.append(Entity1.map(i))

    print(f'Entity Count: {len(entities)}')

    # Simulate output
    print(general_utils.to_json(entities))

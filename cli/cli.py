
import click
from cli.commands import command1

@click.group()
def main():
    """
    Simple CLI
    """
    pass

main.add_command(command1.command1)

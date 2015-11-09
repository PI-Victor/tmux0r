import click

from collection import controller, utils
from collection.commands import vmctx, dockerctx, tmuxctx


cli = click.CommandCollection(sources=[vmctx, dockerctx, tmuxctx])

if __name__ == '__main__':
    cli()

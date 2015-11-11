from click import CommandCollection

from collection import controller, utils
from collection.commands import vmctx, dockerctx, tmuxctx


cli = CommandCollection(sources=[vmctx,dockerctx,tmuxctx])

if __name__ == '__main__':
    cli()

import click
from collection import LibVirtConn
@click.group()
def cli():
    pass

@cli.command()
@click.option('--dirconfig')
def create(dirconfig):
    pass

@cli.command()
def clean():
    pass

if __name__ == '__main__':
    cli()

import click

from collection import controller, utils


@click.group()
def cli():
    pass

@cli.command()
@click.option('--dirconfig')
def list_domains(dirconfig):
    pass

@cli.command()
@click.option('--url')
@click.option('--image_name')
def provision(url, image_name):
    utils.download_image(url, image_name)

@cli.command()
def clean():
    pass

if __name__ == '__main__':
    cli()

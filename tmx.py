import click

from collection import controller, utils


@click.group()
def vmcontext():
    pass

@vmcontext.command()
@click.option('--dirconfig')
def list_domains(dirconfig):
    pass

@vmcontext.command()
@click.option('--url')
@click.option('--image_name')
def vmsetup(url, image_name):
    utils.download_image(url, image_name)

cli = click.CommandCollection(source=[vmctx, tmuxctx, dockerctx, openshiftx])

if __name__ == '__main__':
    cli()

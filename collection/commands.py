import click
from . import utils, docker, tmux, libvirt, openshift


@click.group()
def vmctx():
    pass

@vmctx.command()
def vmlist():
    pass

@vmctx.command()
@click.option('--url')
@click.option('--image_name')
def vmsetup(url, image_name):
    utils.download_image(url, image_name)

@click.group()
def dockerctx():
    pass

@dockerctx.command()
@click.option('--pullimage')
def pullimage(pullimage, registry=None):
    pass

@dockerctx.command()
def images():
    dock = docker.DockerWrapper()
    print(dock)

@click.group()
def tmuxctx():
    pass

@tmuxct.command()
def getwindows():
    tmux.list_windows()

@tmuxctx.command()
@click.option('--openwindow')
def openwindow(openwindow):
    pass

@tmuxctx.command()
@click.option('--openpane')
def openpane(openpane):
    pass

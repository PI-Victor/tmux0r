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
@click.option('--image')
def vmsetup(url, image):
    utils.download_image(url, image)

@vmctx.command()
@click.option('--hypervisor')
def vmlist(hypervisor):
    pass

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
    dock.list_images()

@click.group()
def tmuxctx():
    pass

@tmuxctx.command()
def getwindows():
    tmux.list_windows()

@tmuxctx.command()
@click.option('--sessid')
def tmuxow(sessid):
    pass

@tmuxctx.command()
@click.option('--tmuxop')
def openpane(tmuxop):
    pass

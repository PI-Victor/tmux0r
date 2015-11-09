import click


@click.group()
def vmctx():
    pass

@vmctx.command()
def vmlist(dirconfig):
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
    print(pullimage)

@click.group()
def tmuxctx():
    pass

@tmuxctx.command()
@click.option('--openwindow')
def openwindow(openwindow):
    pass

@tmuxctx.command()
@click.option('--openpane')
def openpane(openpane):
    pass

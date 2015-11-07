import os
from urllib import request, error


def get_dir(subdir=None):
    """get the top level directory of the
    current project if no subdir has been specified,
    otherwise return the concatenated fullpath
    """
    toplevel_dir = os.path.dirname(os.path.os.path.dirname(__file__))
    if subdir is None:
        return toplevel_dir
    return os.path.join(toplevel_dir, subdir)

def download_image(image_url=None, image_name=None):
    """download any specified valid image for virtlib
     to ../images/. If none was specified use
     the current default one, which will probably
     be outdated fast since the datestamp is
     included in the name.
    """
    _images_dir = 'images'
    if image_url is None:
        image_url = 'https://download.fedoraproject.org/pub/fedora/linux/releases/23/Cloud/x86_64/Images/Fedora-Cloud-Base-23-20151030.x86_64.qcow2'
    if image_name is None:
        image_name = 'fedora23.qcow2'
    image_path = '{}/{}'.format(get_dir(_images_dir), image_name)
    try:
        print("Downloading image %s \n Open a beer, this might take a while..." %image_url)
        request.urlretrieve(image_url, image_path)
    except (error.URLError, ValueError) as e:
        print("Failed to download image %s" %e)

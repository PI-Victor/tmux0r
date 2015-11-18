import os
import uuid

from urllib import request, error


class YmlReader(object):
    """Read yml config files and write them to a temporary xml that is
    used to privision domains in libvirt.
    """

    def __init__(self, ymlfile):
        config_path = get_dir("config")
        self.ymlfile = os.path.join(config_path, ymlfile)

    def read_yml(self):
        """Open and return a handler to a yml config file."""
        pass

    def write_to_xml(self):
        """Convert a yml file to xml output and write that xml to a
        temp directory.
        """
        pass

    def get_tmp_file(self):
        tempfile = os.path.join("/tmp/", unique("temp_xml"))
        return tempfile

def unique(name):
    return "{}_{}".format(name, uuid.uuid1())

def get_dir(subdir=None):
    """Get the top level directory of the current project if no subdir has
    been specified, otherwise return the concatenated fullpath.
    """
    toplevel_dir = os.path.dirname(os.path.os.path.dirname(__file__))
    if subdir is None:
        return toplevel_dir
    return os.path.join(toplevel_dir, subdir)

def download_image(image_url=None, image_name=None):
    """Download specified valid image for virtlibto ../images/. If none was
     specified use the current default one, which will probably be outdated
     fast since the datestamp isincluded in the name.
    """
    _images_dir = 'images'
    if image_url is None:
        image_url = "https://download.fedoraproject.org/pub/fedora/linux/releases/23/Cloud/x86_64/Images/Fedora-Cloud-Base-23-20151030.x86_64.qcow2"
    if image_name is None:
        image_name = 'fedora23.qcow2'
    image_path = '{}/{}'.format(get_dir(_images_dir), image_name)
    try:
        print("Downloading image %s \nOpen a beer, this might take a while..."
               % image_url)
        request.urlretrieve(image_url, image_path)
        print("Image downloaded successfully to: %s" % image_path)
    except (error.URLError, ValueError) as e:
        print("Failed to download image %s" % e)

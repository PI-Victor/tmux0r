import docker


DEFAULT_DOCKER_SOCKET='unix://var/run/docker.sock'


class DockerWrapper(object):
    def __init__(self, docker_socket=DEFAULT_DOCKER_SOCKET):
        self.dockerhandler = docker.Client(base_url=docker_socket)

    def provision_container(self, image_id, **kwargs):
        """Create a new container based on an image_id
        """
        pass

    def list_containers(self, image_id=None, *args):
        """List all containers containers.
        :image_id: if it's passed, it shows containers that are bound to that
         docker image.
        :*args: stopped: list only stopped containers
        :running: list only running containers.
        """

        return self.dockerhandler.containers(all=True,
                                            latest=latest,
                                            filters=filters)

    def stop_container(self, container_id=None):
        """Stop a given container, otherwise stop all running containers"""
        pass

    def export_container(self, container_id):
        pass

    def copy_from_container(self,container_id, container_path, host_path):
        pass

    def remove_container(self, container_id=None):
        """Remove a given container, otherwise remove all containers, running
        or not.
        """
        pass

    def attach_to_container(self, container_id):
        """Attach to a bash session of a given running container"""
        pass

    def run_container_command(self, container_id):
        """Run a command inside a given container and output the result.
        """
        pass

    def get_container_log(self, container_id):
        """Return the full log of the specified container."""
        pass

    def refresh_image(self, image_name=None, registry_name=None):
        """Pull the image with the :latest tag, if no image is given,
        refresh all images.
        :registry_name: from a given registry default docker registry
        if not passed.
        """
        pass

    def get_image(self, image_name, image_tag='latest', registry_name=None):
        """Pull a given image with a given tag, default is :latest.
        :registry_name - default docker registry if nothing is passed.
        """
        pass

    def repack_image(self, image_name, copy_to=None):
        """Repack a given image, and copy a file, or a list of files inside it
        """
        pass

    def remove_images(self, image_id=None):
        """If no image was specified, either remove a set of images or all
         images.
        """
        pass

    def list_images(self, notag=False):
        """List all docker images
        :notag - return a list of images with a <none> tag so that they
        can be removed
        """
        pass

    def tag_image(self, image_id, tag_name=None):
        """Tag an image"""
        default_tag = "latest"
        pass

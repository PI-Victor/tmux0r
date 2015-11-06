import docker


class DockerWrapper(object):
    def __init__(self, docker_socket='unix://var/run/docker.sock'):
        self.dockerhandler = docker.Client(base_url=docker_socket)

    def provision_container(self, image_id):
        pass

    def list_containers(self, image_id=None):
        pass

    def stop_container(self):
        pass

    def remove_container(self, container_id=None):
        pass

    def attach_to_container(self, container_id):
        pass

    def run_container_command(self, container_id):
        pass

    def get_container_log(self, container_id):
        pass

    def refresh_image(self, image_name=None):
        pass

    def pull_image(self, image_name, image_tag='latest'):
        pass

    def repack_image(self, image_name):
        pass

    def remove_image(self, image_id=None):
        pass

    def list_images(self):
        pass

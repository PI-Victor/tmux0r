

class OpenShiftWrapper(object):
    """A wrapper around openshift's commands
    """
    def __init__(self):
        pass

    def create_pod(self):
        pass

    def create_project(self):
        pass

    def run_tests(self, testname=None, suite='All'):
        pass

    def setup_registry(self, registry_name=None):
        pass

    def setup_router(self, router_name=None):
        pass

    def cleanup_setup(self, path_name=None):
        pass

    def get_work_dir(self, dir_name=None):
        pass

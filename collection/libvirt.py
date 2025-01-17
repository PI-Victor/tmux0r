import libvirt


# keep this for now here.
# the problem with this is that the default user session has very limited
# access so it's not very flexible for setting network connections, etc.
# the access should be passed as "qemu:///system"
DEFAULT_USER_HYPERVISOR = 'qemu:///session'


class LibVirtConn(object):
    """Provides a wrapper around libvirt. With this you can:
    Create new lxc container/vms. Modify, Create, Snapshots, reset,
    Resume, etc.
    """
    _state = ['test', 'development']
    _tests_type = ['unittests', 'extended', 'e2e']

    def __init__(self, libvirtdriver=DEFAULT_USER_HYPERVISOR):
        try:
            self.handler =  libvirt.open(libvirtdriver)
            self.hypervisor = self.handler.getHostname()
        except libvirt.libvirtError as e:
            #print('Failed to connect to specified driver: %s' % libvirtdriver)
            self.handler = None

    def list_domains(self):
        """Returns a list of defined domains on the host that you can
         use.
        """
        domain_ids = [libvirt for libvirt in self.handler.listAllDomains()
                      if self.handler]
        return [domain for domain_id in domain_ids if domain_id]

    def setup_domain(self, domain):
        """Setup a new domaing with the specified settings"""
        pass

    def destroy_domain(self, domain):
        """Destroy a given domain"""
        pass

    def activate_network(self, domain):
        """Create the network before trying to run a domain"""
        network = self.handler.networkLookupByName(domain)
        if not network.netIsActive():
            network.create()

    def cpu_stats(self):
        """Get cpu stats"""
        pass

    def network_stats(self):
        """Get network stats"""
        pass

    def domain_stats(self, domainid=None):
        """Get all domain stats"""
        pass

    def load_xml(self):
        """Loads the predefined xml file into the object for manipulation"""
        pass

    def get_domain_state(self):
        """Get the state of a domain,
        suspended, off, running, etc.
        """
        return self.handler.state()

    def get_domains(self):
        """Get all domains for the current hypervisor"""
        return self.handler.listAllDomains()

    def close_connection(self):
        """Close current hypervisor connection"""
        self.handler.close()

    def create_snapshot(self, domain):
        """Create a snapshot of the given domain"""
        pass

    def restore_snapshot(self, domain, snapshot_id):
        """Restore a specific domain"""
        pass

    def get_snapshots(self, domain):
        """Get current snapshots of given domain"""
        pass

    def restart_domain(self, domain):
        """Restart a given domain"""
        pass

    def stop_domain(self, domain):
        """Stop a given domain"""
        pass

    def start_domain(self, domain):
        """Start a given domain"""
        pass

    def suspend_domain(self, domain):
        """Suspend a given domain"""
        pass

    def save_domain(self, domain_id):
        """Save the state of a domain and shut it down"""
        pass

    def reset_domain(self, domain):
        """Force reset a domain"""
        pass

    def resume_domain(self, domain):
        """Resume a domain that has been paused"""
        pass

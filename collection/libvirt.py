import libvirt


#keep this for now here
DEFAULT_LIBVIRT_DRIVER = 'qemu:///system'


class LibVirtConn(object):
    """Provides an interface to a libvirt
    connection
    """
    def __init__(self,libvirtdriver=None):
        if libvirtdriver is None:
            libvirtdriver = DEFAULT_LIBVIRT_DRIVER
        try:
            self.libvirthandler =  libvirt.open(libvirtdriver)
        except libvirt.libvirtError as e:
            print('Failed to connect to specified driver: %s' % libvirtdriver)
            self.libvirthandler = None
        self.hypervisor = self.libvirthandler.getHostname()

    def list_domains(self):
        """Returns a list of defined domains
        on the host that you can manipulate.
        """
        domain_ids = [libvirt for libvirt in self.libvirthandler.listAllDomains() if self.libvirthandler]
        for domain_id in domain_ids:
            print(domain_id.name())

    def setup_domain(self, domainid):
        """Setup a new domaing with the
        specified settings
        """
        pass

    def destroy_domain(self, domainid):
        """Destroy a given domain"""
        pass

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
        """Loads the predefined xml file into the
        object for manipulation
        """
        pass

    def get_domain_state(self):
        return self.libvirthandler.state()

    def get_domains(self):
        return self.libvirthandler.listAllDomains()

    def close_connection(self):
        """Close current hypervisor connection"""
        self.libvirthandler.close()

    def create_snapshot(self, domainid):
        """Create a snapshot of the given domain"""
        pass

    def restore_snapshot(self, domainid, snapshotid):
        """Restore a specific domain"""
        pass

    def get_snapshots(self, domainid):
        """Get current snapshots of given domain"""
        pass

    def restart_domain(self, domainid):
        """Restart a given domain"""
        pass

    def stop_domain(self, domainid):
        """Stop a given domain"""
        pass

    def start_domain(self, domainid):
        """Start a given domain"""
        pass

    def suspend_domain(self, domainid):
        """Suspend a given domain"""
        pass

    def save_domain(self, domainid):
        """Save the state of a domain and
        shut it down
        """
        pass

    def reset_domain(self, domainid):
        """Force reset a domain"""
        pass

    def resume_domain(self, domaind):
        """Resume a domain that has been
        paused
        """
        pass

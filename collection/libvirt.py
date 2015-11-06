import libvirt


class LibVirtConn(object):
    '''Provides an interface to a libvirt connection
    '''
    def __init__(self,libvirtdriver=None):
        try:
            libvirtdriver = 'qemu:///system'
            self.libvirthandler =  libvirt.open(libvirtdriver)
        except libvirt.libvirtError as e:
            print('Failed to connect to specified driver: %s' % libvirtdriver)
            self.libvirthandler = None
        self.hypervisor = self.libvirthandler.getHostname()

    def list_domains(self):
        '''Returns a list of defined domains on the host
        that you can manipulate.
        '''
        libvirt_domains = [libvirt for libvirt in self.libvirthandler.listDomainsID() if self.libvirthandler]
        return libvirt_domains

    def setup_domain(self, domainid):
        '''Setup a new domaing with the specified settings'''
        pass

    def destroy_domain(self, domainid):
        '''Destroy a given domain for rebuilding'''
        pass

    def cpu_stats(self):
        '''Get cpu stats'''
        pass

    def network_stats(self):
        '''Get network stats'''
        pass

    def domain_stats(self, domainid=None):
        '''Get all domain stats'''
        pass

    def load_xml(self):
        '''Load the predefined xml file into the object'''
        pass

    def get_domain_state(self):
        return self.libvirthandler.state()

    def get_domains(self):
        return self.libvirthandler.listAllDomains()

    def close_connection(self):
        '''Close current hypervisor connection'''
        self.libvirthandler.close()

    def create_snapshot(self, domainid):
        '''Create a snapshot of the given domain'''
        pass

    def restore_snapshot(self, domainid, snapshotid):
        '''Restore a specific domain'''
        pass

    def get_snapshots(self, domainid):
        '''Get current snapshots of given domain'''
        pass

    def restart_domain(self, domainid):
        '''Restart a given domain'''
        pass

    def stop_domain(self, domainid):
        '''Stop a given domain'''
        pass

    def start_domain(self, domainid):
        '''Start a given domain'''
        pass

    def suspend_domain(self, domainid):
        '''Suspend a given domain'''
        pass

    def save_domain(self, domainid):
        '''Save the state of a domain and shut it down'''
        pass

    def reset_domain(self, domainid):
        pass

    def resume_domain(self, domaind):
        pass

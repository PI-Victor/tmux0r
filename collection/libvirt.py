import libvirt


class LibVirtConn(object):
    '''provides an interface to a libvirt connection
    '''
    def __init__(self,libvirtdriver=None):
        try:
            self.libvirthandler =  libvirt.open(libvirtdriver)
        except libvirt.libvirtError as e:
            print('Failed to connect to specified driver:{}'.format(libvirtdriver))
            self.libvirthandler = None

    def list_domains(self):
        '''get a list of defined domains on the host
        '''
        if self.libvirthandler:
            pass

    def setup_domain(self, domainid):
        '''Setup a new domaing with the specified settings'''
        pass

    def destroy_domain(self, domainid):
        '''Destroy a given domain for rebuilding'''
        pass

import libvirt


class LibVirtConn(object):
    '''provides an interface to a libvirt connection
    '''
    def __init__(self,libvirtdriver=None):
        try:
            self.libvirthandler =  libvirt.openReadOnly(libvirtdriver)
        except libvirt.libvirtError as e:
            print('Failed to connect to specified driver:{}'.format(libvirtdriver))
            self.libvirthandler = None

    def list_domains(self):
        if self.libvirthandler:
            pass

    def provision_domain(self, domainid):
        pass

    def destroy_domain(self, domainid):
        pass

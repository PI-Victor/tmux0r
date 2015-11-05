import tmuxp


class TmuxWrapper(object):

    def __init__(self):


    def window_factory(self, sessionid):
        '''create a new window split in a given a window id'''
        pass

    def tab_factory(self, sessionid):
        '''create a new pane'''
        pass

    def get_active_sessions(self):
        '''return the number of active sessions'''
        pass

    def attach_to_session(self, sessionid):
        '''attach to a specific session'''
        pass

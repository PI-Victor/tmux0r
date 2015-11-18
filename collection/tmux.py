import tmuxp
from tmuxp.exc import TmuxpException, TmuxSessionExists

from collection import utils


BASH_BIN_DEFAULT="/usr/bin/bash"


class TmuxWrapper(object):
    """A wrapper around the tmuxp lib to handle tmux from the cli with the help
    of the pocoo click lib.
    """
    def __init__(self, config_file=None):
        self.server = tmuxp.Server()

    def session_factory(self, session_name='session'):
        """Create a new session with a given name.
        :session_name: the name of the new sesion. To make sure it's unique,
        adds a uuid to it.
        """
        self.server.new_session(utils.unique(session_name))

    def window_factory(self, sessionid):
        """Create a new window split in a given window id."""
        pass

    def close_panes(self, paneid=None):
        """Close a particular split in the current window or close all of
         them if windowid is not passed
        """
        pass

    def get_panes(self, sessionid):
        """Return the names of the window splits for the given window"""
        pass

    def get_windows(self, sessionid):
        """Return the name of the panes
        """
        pass

    def attach_to_pane(self, paneid):
        """Select a given pane
        """
        pass

    def pane_factory(self, windowid=None):
        """Create a new pane with given content if nothing is passed,
        just open a pane with bash
        """
        pass

    def close_pane(self, paneid=None):
        """Close given pane in the session, if no pane is given, close all
        panes in the active session
        """
        pass

    def get_sessions(self):
        """Return the number of active sessions"""
        sessions = []
        try:
            for s in self.server.list_sessions():
                sessions.append(s)
        except TmuxpException:
            print("Couldn't find any available sessions")
            sessions = None

        return sessions

    def attach_to_session(self, sessionid=None):
        """Attach to a specific session if none was provided
        attach to the first listed one.
        """
        if not self.get_sessions():
            return

        if not sessionid:
            sessionid = self.server.list_sessions()[0]

        if self.get_sessions():
            self.server.attach_session(sessionid)

    def filter_output(self, paneid=None, windowid=None):
        """Filter the output of a given window/pane. This comes in handy for
         on-the-fly monitoring of tests in or outside of containers/vms
        """
        pass

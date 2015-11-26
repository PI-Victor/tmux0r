import tmuxp
from tmuxp.exc import TmuxpException, TmuxSessionExists

from collection import utils


BASH_BIN_DEFAULT="/usr/bin/bash"


class TmuxWrapper(object):
    """A wrapper around the tmuxp lib to handle tmux from the cli with the help
    of the pocoo click lib.
    """
    def __init__(self, config_file=None):
        """Create a new tmux server if none is available
        """
        self.server = tmuxp.Server()
    def window_factory(self, session_id):
        """Create a new window in a given session."""
        print(session_id)

    def attach_to_window(self, window_id):
        """Attach to the given id."""
        pass

    def get_windows(self, session_id):
        """Return the name of the windows for the given id.
        """
        print(s)
        for s in self.server.sessions:
            print(s)

    def pane_factory(self, session_id=None, window_id=None):
        """Create a new pane with given content if nothing is passed,
        just open a pane with bash
        """
        pass

    def attach_to_pane(self, pane_id):
        """Select a given pane
        """
        pass

    def get_panes(self, session_id):
        """Return the names of the window splits for the given window"""
        pass

    def close_panes(self, pane_id=None):
        """Close a particular split in the current window or close all of
         them if windowid is not passed
        """
        pass

    def session_factory(self, session_name='session'):
        """Create a new session with a given name.
        :session_name: the name of the new sesion. To make sure it's unique,
        adds a uuid to it.
        """
        self.server.new_session(utils.unique(session_name))

    def attach_to_session(self, session_id=None):
        """Attach to a specific session if none was provided
        attach to the first listed one.
        """
        if not self.get_sessions():
            return

        if not sessionid:
            sessionid = self.server.list_sessions()[0]

        if self.get_sessions():
            self.server.attach_session(sessionid)

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

    def close_session(self, session_id=None):
        """Close given session, or close all.
        """
        pass

    def filter_output(self, pane_id=None, window_id=None):
        """Filter the output of a given window/pane. This comes in handy for
         on-the-fly monitoring of tests in or outside of containers/vms
        """
        pass

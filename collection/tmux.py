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

    def window_factory(self, session_id, window_name='window', config=None):
        """Create a new window in a given session.
        :session_id: create a new window in the given session.
        :window_name: prefix for the window name, to ensure it's unique,
        a UUID is added at the end of the name.
        :config: a windows configuration file (yml, json).
        Returns a window instance.
        """
        # TODO: remember to launch a window config here, to create
        # the window according to a yaml configuration.
        try:
            session = self.server.list_sessions()[session_id]
        except IndexError:
            print("Specified session, doesn't exist!")
            return None

        return session.new_window(utils.unique(window_name))

    def attach_to_window(self, window_id):
        """Attach to the given window."""
        pass

    def get_windows(self, session_id):
        """Return the name of the windows for the given id.
        """
        windows = []
        [session for session in self.server.children if session]
        return windows

    def close_windows(self, window_id):
        """Close a given window id, otherwise close all
        """
        pass

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
        """Attach to session.
        :session_id: attach to the specified session.
        If nothing is passed, attach to the first active session.
        """
        if not self.get_sessions():
            print("No sessions available!")
            return

        if not session_id:
            session_id = self.server.list_sessions()[0]

        if self.get_sessions():
            self.server.attach_session(session_id)

    def get_sessions(self):
        """Return the number of active sessions"""
        sessions = []
        try:
            for s in self.server.list_sessions():
                # this is so dirty it makes my skin crawl!!!
                session_int = int(s._session_id.strip('$'))
                sessions.append(session_int)
        except TmuxpException:
            print("Couldn't find any available sessions")
            sessions = None

        return sessions

    def close_sessions(self, session_id=None):
        """Close given session, or close all.
        """
        if session_id:
            self.server.kill_session(session_id)
            return

        for s in self.get_sessions():
            try:
                self.server.kill_session(s)
            except TmuxpException:
                print('Session unavailable')


    def filter_output(self, pane_id=None, window_id=None):
        """Filter the output of a given window/pane. This comes in handy for
         on-the-fly monitoring of tests in or outside of containers/vms
        """
        pass

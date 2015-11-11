import tmuxp


BASH_BIN_DEFAULT="/usr/bin/bash"


class TmuxWrapper(object):
    """A wrapper around the tmuxp lib to
    manipulate tmux from the cli with the help
    of the pocoo click lib.
    """

    def __init__(self, findid, createservice):
        pass

    def window_factory(self, sessionid):
        """Create a new window split in a
        given window id.
        """
        pass

    def close_window_split(self, windowid=None):
        """Close a particular split in the current
        window or close all of them if windowid is
        not passed
        """
        pass

    def get_window_splits(self, windowid):
        """Return the names of the window splits
        for the given window
        """
        pass

    def get_panes(self, sessionid):
        """Return the name of the panes
        """
        pass

    def attach_to_pane(self, paneid):
        """Select a given pane
        """
        pass

    def pane_factory(self, windowid=None):
        """Create a new pane with given content
        if nothing is passed, just open a pane with bash
        """
        pass

    def close_pane(self, paneid=None):
        """Close given pane in the session,
        if no pane is given, close all panes
        in the active session
        """
        pass

    def get_active_sessions(self):
        """Return the number of active sessions"""
        pass

    def attach_to_session(self, sessionid):
        """Attach to a specific session"""
        pass

    def filter_output(self, paneid=None, windowid=None):
        """Filter the output of a given window/pane
        This comes in handy for on-the-fly monitoring
        of tests in or outside of container/vms
        """
        pass

import tmuxp

from collection import tmux


tmwrap = tmux.TmuxWrapper()

def test_wrapper_type():
    assert tmwrap.server is not None
    assert isinstance(tmwrap.server, tmuxp.server.Server)

def test_session_factory():
    tmwrap.session_factory()
    sessions = tmwrap.get_sessions()
    assert sessions is not None
    for s in sessions:
    tmwrap.close_sessions()

def test_window_factory():
    for i in range(10):
        tmwrap.session_factory()

    for session in tmwrap.get_sessions():
        tmwrap.window_factory(session)

# TODO: remake this part of the test, it's invalid.
# get_windows returns an empty list.
    for s in tmwrap.get_sessions():
        windows = tmwrap.get_windows(s)
        for w in windows:
            assert isinstance(w, tmuxp.window.Window)

    tmwrap.close_sessions()

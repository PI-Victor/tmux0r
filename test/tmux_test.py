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

def test_window_factory():
    for i in range(10):
        tmwrap.session_factory()

    for session in tmwrap.get_sessions():
        tmwrap.window_factory(session)

    for s in tmwrap.get_sessions():
        window = tmwrap.get_windows(s)
        assert isinstance(window, tmuxp.window.Window)


tmwrap.close_sessions()

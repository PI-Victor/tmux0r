#### Tmux docs for tmux0r
---

It's based on the [tmuxp](https://github.com/tony/tmuxp) library.

Tmux0r allows you to take a peek into specific running lxc/docker containers or
libvirt created vms. It comes in handy when running tests inside of vms or in
specific cases when you need to work inside a running lxc/docker container.
It splits windows or creates new panes with output to different stdout for different
sources.
It provides a filtering flag for the stdout that allows you to monitor long logs
for specific words.

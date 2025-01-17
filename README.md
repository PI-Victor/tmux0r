# Tmux0r
##### Unofficial

Status: Prototype  
Build Status: [![Circle CI](https://circleci.com/gh/PI-Victor/tmux0r/tree/master.svg?style=svg)](https://circleci.com/gh/PI-Victor/tmux0r/tree/master)

Created to aid the development of [Openshift V3](https://github.com/openshift/origin).


See the docs for the commands of the wrappers:  
[Tmux Commands](docs/tmux.md)  
[Libvirt Commands](docs/libvirt.md)  
[Docker Commands](docs/docker.md)  
[Openshift Commands](docs/openshift.md)  

---

Make sure you have development files for libvirt (libvirt-devel) installed.

```
[openshift@origin tmux0r]$ virtualenv -p python3 venv
[openshift@origin tmux0r]$ ln -s venv/bin/activate
[openshift@origin tmux0r]$ source activate
[openshift@origin tmux0r]$ pip3 install -r requirements.txt
[openshift@origin tmux0r]$ python3 tmx.py vmsetup
```

---
The boxes use a fedora 23 qcow image that needs to be pulled in first.

#### Use cases:

Spawns a vm with the mounted openshift src folder inside it and runs the tests specified inside a config.yml file in config/.  
Can attach to a container/virtual machine launching a tmux pane/window for either launching commands or tailing logs with a filter.
e.g.: Watch for failed tests. It filters the output of the container/vm for the word 'failed'.

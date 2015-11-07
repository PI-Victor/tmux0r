# Tmux0r
##### Unofficial

Status: Prototype

Created to aid the development of [Openshift V3](https://github.com/openshift/origin).

---

Make sure you have development files for libvirt (libvirt-devel) installed.

```
[openshift@origin tmux0r]$ virtualenv -p python3 venv
[openshift@origin tmux0r]$ ln -s venv/bin/activate
[openshift@origin tmux0r]$ source activate
[openshift@origin tmux0r]$ pip3 install -r requirements.txt
```


---
The boxes use a fedora 23 qcow image that needs to be pulled in first.


#### Use cases:

Spawns a vm with the mounted openshift src folder inside it and runs the tests specified inside the config file in config/.

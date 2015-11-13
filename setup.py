try:
    import setuptools as s
except ImportError:
    import distutils.core as s

config = {
    'name': 'tmuxor',
    'include_package_data': True,
    'version': 'unversioned',
    'author': 'thecodeflavour.org',
    'url': 'http://github.com/PI-Victor/tmux0r',
    'long_description': open('README.md').read(),
    'zip_safe': False,
    'packages': s.find_packages(),
    'install_requires':[
        'tmuxp',
        'docker-py',
        'libvirt-python',
        'click',
        'Fabric'
    ],
}

s.setup(**config)

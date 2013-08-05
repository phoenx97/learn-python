try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My first simple game',
    'author': 'Peter Le',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it',
    'author_email': 'togipete@gmail.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex45'],
    'scripts': [],
    'name': 'simplegame'
}

setup(**config)

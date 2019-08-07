try:
    import setuptools
    from setuptools import setup
except:
    from distutils.core import setup

config = {
    'description': 'example_pkg is for seeing if I can make a project that installs and has a script to run',
    'author': 'Hu jianbo',
    'url': 'No URL',
    'download_url': 'Just local',
    'author_email': 'hujianbo1981@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': setuptools.find_packages(),
    'scripts': ['bin/joke.py'],
    'name': 'example_pkg'
}

setup(**config)
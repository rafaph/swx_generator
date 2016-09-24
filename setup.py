# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

BASE_DIR = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='swx_generator',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.3',

    description='SimWorX generator',
    long_description=long_description,

    # The project's main homepage.
    # url='https://github.com/pypa/sampleproject',

    # Author details
    author='SimWorX',
    author_email='castro@simworx.com.br',

    # What does your project relate to?
    keywords='simworx web django generators',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),
    include_package_data=True
)

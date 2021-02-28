import os
from setuptools import setup, find_packages


def read(*names):
    return open(os.path.join(os.path.dirname(__file__), *names)).read()


setup(
    name="pyarabicshaping",
    version="1.1",
    include_package_data=True,
    packages=find_packages(),
    author="vorujack",
    author_email="vorujack@gmail.com",
    description="arabic shapes",
    long_description=read('README.md'),
    license="MIT",
    url='https://github.com/vorujack/pyarabicshaping',
    download_url='https://github.com/vorujack/pyarabicshaping/tarball/1.0',
    keywords="arabic",
)

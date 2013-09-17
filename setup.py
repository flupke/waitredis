#!/usr/bin/env python
from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()


version = '0.1'

install_requires = [
    'redis',
]


setup(name='waitredis',
    version=version,
    description="Simple wrapper script to wait until redis is ready",
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='redis wrapper-script',
    author='Luper Rouch',
    author_email='luper.rouch@gmail.com',
    url='https://github.com/Stupeflix/waitredis',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['waitredis=waitredis:main']
    }
)

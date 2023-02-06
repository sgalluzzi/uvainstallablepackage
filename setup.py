#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='shared',
      version='1.0.1',
      description='This package has shared components.',
      author='Efrain Olivares edited by Seth Galluzzi',
      author_email='efrain.olivares@gmail.com, vzw6yk@virginia.edu',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      license='LICENSE.txt',
    )

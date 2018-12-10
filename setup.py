# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='numerical_methods',
    version='0.1.0',
    description='Implementation of Numerical Methods',
    long_description=readme,
    author='Benardi Nunes',
    author_email='benardinunes@gmail.com',
    url='https://github.com/Benardi/numerical_methods/',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)


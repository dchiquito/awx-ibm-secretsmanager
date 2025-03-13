#!/usr/bin/env python

from setuptools import setup

requirements = []  # add Python dependencies here
# e.g., requirements = ["PyYAML"]

setup(
    name='ibm-secretsmanager',
    version='0.1',
    author='Ansible, Inc.',
    author_email='daniel.chiquito@gmail.com',
    description='',
    long_description='',
    license='Apache License 2.0',
    keywords='ansible',
    url='http://github.com/dchiquito/awx-ibm-secretsmanager',
    packages=['ibm_secretsmanager'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    install_requires=requirements,
    entry_points={
        'awx.credential_plugins': [
            'ibm_secretsmanager = ibm_secretsmanager:ibm_secretsmanager_plugin',
        ]
    }
)

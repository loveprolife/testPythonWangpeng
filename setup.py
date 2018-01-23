#!/usr/bin/env python
# coding=utf-8

import sys
from os.path import dirname, join
from pip.req import parse_requirements

from setuptools import (
    find_packages,
    setup,
)

setup(
    name="testWangPeng",
    version=100,
    description="testWangPeng description",
    packages=["testPythonWangpeng", "testPythonWangpeng.package_runoob"],
    author="wangPeng",
    author_email="wangPeng@wangPeng.com",
    maintainer="wangpeng",
    maintainer_email="wangpeng@wangPeng.com",
    license='Apache License v2',
    package_data={'': ['*.*']},
    url="https://www.wuaixiang.com",
    install_requires=[],
    zip_safe=False,
    platforms=["all"],
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
)

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='helpful',
    version='1.0.0',
    description='Official Helpful API library client for python',
    author='Pavan Kumar Sunkara',
    author_email='pavan.sss1991@gmail.com',
    url='https://helpful.io',
    license='MIT',
    install_requires=[
        'requests >= 2.1.0'
    ],
    packages=[
        'helpful',
        'helpful.api',
        'helpful.error',
        'helpful.http_client'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

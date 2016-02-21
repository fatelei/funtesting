# -*- coding: utf8 -*-
"""Setup instrucation."""

from setuptools import setup


setup(
    name="funtesting",
    description="Make testing more fun",
    author="fatelei",
    author_email="fatelei@gmail.com",
    install_requires=[
        "fakeredis==0.6.2",
        "mock==1.3.0",
        "nose=1.3.7"
    ],
    packages=["funtesting"],
    zip_safe=False,
    url="https://github.com/fatelei/funtesting",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        'Topic :: Software Development :: Testing',
    ],
    license="BSD License",
    entry_points={
        "nose.plugins.0.10": [
            'funtesting = funtesting.manager:Manager',
        ]
    },
)

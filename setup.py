# -*- coding: utf8 -*-

from setuptools import setup


setup(
    name="funtesting",
    description="Make testing more fun",
    author="fatelei",
    author_email="fatelei@gmail.com",
    install_requires=[
        "fakeredis==0.6.2",
        "mock==1.3.0"
    ],
    packages=["funtesting"],
    zip_safe=False,
    url="https://github.com/fatelei/funtesting",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries",
    ],
    license="BSD License"
)

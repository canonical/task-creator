#!/usr/bin/env python3

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="task-creator",
    version="0.1",
    author="Thomas Bille",
    author_email="toto@canonical.com",
    url="https://github.com/canonical-webteam/task-creator",
    license="GPL-3.0",
    description="Create issues on github under an zenhub epic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["requests", "PyGithub"],
    packages=setuptools.find_namespace_packages(),
    scripts=["task.py"],
)

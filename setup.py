import os

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yaml-stripper",
    version="2.1.2",
    author="Wagner Silva",
    author_email="wra.silva@gmail.com",
    description="A command-line tool for removing specified fields from YAML files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vavasilva/yaml-stripper",
    packages=setuptools.find_packages(),
    project_urls={
        "Bug Tracker": "https://github.com/vavasilva/YamlStripper",
        "Documentation": "https://github.com/vavasilva/YamlStripper",
        "Source Code": "https://github.com/vavasilva/YamlStripper",
        "Homepage": "https://github.com/vavasilva/YamlStripper"
    },
    entry_points={
        'console_scripts': ['yaml-stripper=YamlStripper.cli:main']
    },
    install_requires=['PyYAML>=6.0', 'click>=8.1.3', 'keyring']
    ,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

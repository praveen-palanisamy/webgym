#!/usr/bin/env python
# WebGym Visual MiniWoB environment registration script
# TensorFlow 2 Reinforcement Learning Cookbook | Praveen Palanisamy

from setuptools import setup, find_packages
import pathlib

parent_dir = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (parent_dir / "README.md").read_text(encoding="utf-8")

setup(
    name="webgym",  # Required
    version="1.0.5",  # Required
    description="Reinforcement Learning Environments for 50+ web-based tasks",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://github.com/praveen-palanisamy/webgym",  # Optional
    author="Praveen Palanisamy",  # Optional
    author_email="praveen.palanisamy@outlook.com",
    classifiers=[  # Optional
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="webgym, rl web tasks, rl in browser, Gym environments",  # Optional
    package_dir={"": "src"},  # Optional
    packages=find_packages(where="src"),  # Required
    include_package_data=True,
    python_requires=">=3.6, <4",
    install_requires=["gym"],
    project_urls={  # Optional
        "Source": "https://github.com/praveen-palanisamy/Tensorflow-2-Reinforcement-Learning-Cookbook",
        "Author website": "https://praveenp.com",
    },
)

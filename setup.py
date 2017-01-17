from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

setup(
    name="scoria",
    version="1.0",
    author="Jacob Durrant",
    author_email="durrantj@gmail.com",
    description="A lightweight molecule manipulation codebase.",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta"
    ],
)

import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="hipe_commons",
    url="https://github.com/hipe-eval/HIPE-pycommons",
<<<<<<< HEAD
    version="0.2.1",
=======
    version="0.1.0",
>>>>>>> develop
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.10",
        "Operating System :: POSIX",
    ],
    license="GPL v3"
    ,
    install_requires=[
        "pandas",
        "tabulate"
    ],
    long_description=read("README.md"),
    long_description_content_type='text/markdown'
<<<<<<< HEAD
)
=======
)
>>>>>>> develop

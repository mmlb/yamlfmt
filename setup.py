from setuptools import setup

with open("README") as f:
    long_description = f.read()

classifiers = [
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 2",
    "Topic :: Utilities",
]

setup(
    author="Manuel Mendez",
    author_email="mmendez534@gmail.com",
    classifiers=classifiers,
    description="An opinionated yaml formatter based on ruamel.yaml",
    install_requires=["ruamel.yaml<0.15"],
    keywords="yaml formatter",
    license="GPLV3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="yamlfmt",
    scripts=["yamlfmt"],
    url="https://github.com/mmlb/yamlfmt",
    version="1.0.0",
)

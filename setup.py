from setuptools import setup

with open('README') as f:
    long_description = f.read()

classifiers = [
    'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
    'Programming Language :: Python :: 3',
    'Topic :: Utilities',
]

setup(
    author='Manuel Mendez',
    author_email='mmendez534@gmail.com',
    classifiers=classifiers,
    description='An opinionated yaml formatter based on ruamel.yaml',
    install_requires=['ruamel.yaml<0.15'],
    keywords='yaml format',
    license='[MPLv2.0](https://mozilla.org/MPL/2.0/)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='yamlfmt',
    scripts=['yamlfmt'],
    url='https://github.com/mmlb/yamlfmt',
    version='0.1.5',
)

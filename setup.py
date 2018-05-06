import sys
from setuptools import setup

if sys.version_info[0] < 3:
    sys.stderr.write('Python < 3 is unsupported')

with open('README') as f:
    long_description = f.read()

classifiers = [
    'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Utilities',
]

setup(
    author='Manuel Mendez',
    author_email='mmendez534@gmail.com',
    classifiers=classifiers,
    description='An opinionated yaml formatter based on ruamel.yaml',
    install_requires=['ruamel.yaml<0.15'],
    keywords='yaml format',
    license='MPL 2.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='yamlfmt',
    python_requires='>=3.0',
    scripts=['yamlfmt'],
    url='https://github.com/mmlb/yamlfmt',
    version='0.1.6',
)

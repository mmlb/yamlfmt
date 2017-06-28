from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    long_description = open('README.md').read()

setup(
        name='yamlfmt',
        description='An opinionated yaml formatter based on ruamel.yaml',
        long_description=long_description,
        url='https://github.com/mmlb/yamlfmt',
        author='Manuel Mendez',
        author_email='mmendez534@gmail.com',
        version='0.1.5',
        scripts=['yamlfmt'],
        license='[MPLv2.0](https://mozilla.org/MPL/2.0/)',
        install_requires=['ruamel.yaml<0.15'],
        classifiers=[
            'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
            'Programming Language :: Python :: 3',
            'Topic :: Utilities',
        ],
        keywords='yaml format'
)

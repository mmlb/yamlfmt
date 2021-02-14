"""
Yaml handling, file copying
"""
import os
import sys
import tempfile
from shutil import copyfile

from ruamel import yaml


def round_trip(sout, sin, custom_width=None, version=None, indent=None):
    y = yaml.round_trip_load(sin)
    yaml.round_trip_dump(
        y,
        sout,
        width=custom_width,
        version=(1, 1) if version else None,
        explicit_start=True,
        indent=indent,
        block_seq_indent=indent,
    )


def format_and_write(file, width, version):
    with tempfile.TemporaryFile() as temporary_file, open(file, "r") as sin:
        round_trip(temporary_file, sin, width, version)
        copyfile(temporary_file.name, file)


def format_and_display(file, width, version):
    # what is this ttyname stuff for?
    # file_out = os.ttyname(sys.stdout.fileno())
    with open(file, "r") as sin:  # , open(file_out, 'w') as sout:
        round_trip(sys.stdout, sin, width, version)


def make_temp_file(name):
    # MDM: What was the goal of this code?
    basename = os.path.basename(name)
    dirname = os.path.dirname(name)
    fd, outname = tempfile.mkstemp(prefix=basename + ".", dir=dirname)

    # linux only footwork.
    stat = os.stat(name)
    os.fchmod(fd, stat.st_mode)
    os.fchown(fd, stat.st_uid, stat.st_gid)
    os.close(fd)
    return outname

import subprocess
import shlex

import yamlfmt
from yamlfmt.yamlfmt import round_trip


def test_simple():
    with open("samples/a.yaml", "r") as input, open("samples/a_out.yaml","w") as output:
        round_trip(output, input)

def test_command_line():
    parts = shlex.split("pipenv run python -m yamlfmt samples/a.yaml")
    result = subprocess.run(parts, capture_output=True)
    assert b"a:" in result.stdout
    assert b"b:" in result.stdout

def test_command_line_indent():
    parts = shlex.split("pipenv run python -m yamlfmt -i 5 samples/b.yaml")
    result = subprocess.run(parts, capture_output=True)
    assert b"hash:" in result.stdout

def test_yaml_1_1():
    parts = shlex.split("pipenv run python -m yamlfmt -i 5 --use-yaml-1-1 samples/b.yaml")
    result = subprocess.run(parts, capture_output=True)
    assert b"hash:" in result.stdout


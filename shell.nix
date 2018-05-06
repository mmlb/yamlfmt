# NOTE: for bdist_wheel zip file errors see:
# https://github.com/NixOS/nixpkgs-channels/blob/nixos-unstable/doc/languages-frameworks/python.section.md#python-setuppy-bdist_wheel-cannot-create-whl

with import <nixpkgs> { };
stdenv.mkDerivation rec {
  name = "env";
  env = buildEnv { name = name; paths = buildInputs; };
  buildInputs = [
    python36
    python36Packages.setuptools
    python36Packages.twine
    python36Packages.wheel
  ];
}

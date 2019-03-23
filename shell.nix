with import <nixpkgs> { };
stdenv.mkDerivation rec {
  name = "env";
  env = buildEnv { name = name; paths = buildInputs; };
  SOURCE_DATE_EPOCH = "315532800";
  buildInputs = [
    python3
    python3Packages.black
    python3Packages.setuptools
    python3Packages.twine
    python3Packages.wheel
  ];
}

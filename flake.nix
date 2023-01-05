{
  description = "yamlfmt dev env";

  inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";

    devshell.inputs.flake-utils.follows = "flake-utils";
    devshell.inputs.nixpkgs.follows = "nixpkgs";
    devshell.url = "github:numtide/devshell";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    flake-utils,
    devshell,
    nixpkgs,
  }:
    flake-utils.lib.eachDefaultSystem (system: {
      devShell = let
        pkgs = import nixpkgs {
          inherit system;

          overlays = [devshell.overlay];
        };
      in
        pkgs.devshell.mkShell {
          packages = with pkgs; [
            alejandra
            python3
            python3Packages.black
            python3Packages.python-lsp-server
            python3Packages.setuptools
            python3Packages.twine
            python3Packages.wheel
          ];
        };
    });
}

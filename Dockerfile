FROM nixos/nix

RUN nix-channel --add https://nixos.org/channels/nixpkgs-unstable nixpkgs
RUN nix-channel --update

# TODO: figure out how to use the sell.nix artifact
# RUN nix-build -A pythonFull '<nixpkgs>'
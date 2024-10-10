# To learn more about how to use Nix to configure your environment
# see: https://developers.google.com/idx/guides/customize-idx-env
{ pkgs, ... }: {
  
  channel = "stable-24.05"; # or "unstable"
  packages = [ pkgs.python3 ];
  env = {};
  services.docker.enable = true;
  idx = {
    extensions = [ "ms-python.python" "rangav.vscode-thunder-client" ];
    workspace = {
      # Runs when a workspace is first created with this `dev.nix` file
      onCreate = {
        install =
          "python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt";
        # Open editors for the following files by default, if they exist:
        default.openFiles = [ "README.md" "src/index.html" "main.py" ];
      };
      # Runs when a workspace is (re)started
      onStart = { run-server = "./devserver.sh"; };
    };
  };
}

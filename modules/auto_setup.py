import os
import subprocess

def command_exists(cmd):
    return subprocess.call(["which", cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

def install_dependencies(config):
    dependencies = config.get("dependencies", {
        "subfinder": "https://github.com/projectdiscovery/subfinder",
        "assetfinder": "https://github.com/tomnomnom/assetfinder",
        "httpx": "https://github.com/projectdiscovery/httpx",
        "nuclei": "https://github.com/projectdiscovery/nuclei",
        # Add additional tools as needed
    })
    for tool, repo in dependencies.items():
        if not command_exists(tool):
            print(f"[+] Installing {tool}...")
            # This is a placeholder – the actual installation commands may vary.
            os.system(f"git clone {repo} && cd {tool} && go build .")
        else:
            print(f"[+] {tool} is already installed.")

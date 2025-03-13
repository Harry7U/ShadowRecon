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
        "katana": "https://github.com/projectdiscovery/katana",
        "gf": "https://github.com/tomnomnom/gf",
        "bxss": "https://github.com/1N3/BXSS",
        "sqlmap": "https://github.com/sqlmapproject/sqlmap",
        "redirect-checker": "https://github.com/s0md3v/redirect-checker"
    })
    for tool, repo in dependencies.items():
        if not command_exists(tool):
            print(f"[+] Installing {tool}...")
            if os.path.exists(tool):
                os.system(f"rm -rf {tool}")
            os.system(f"git clone {repo}")
            tool_dir = repo.split('/')[-1]
            os.chdir(tool_dir)
            if not os.path.exists("go.mod") and tool in ['subfinder', 'assetfinder', 'nuclei', 'katana']:
                os.system("go mod init")
            if tool in ['subfinder', 'assetfinder', 'nuclei', 'katana']:
                os.system("go build .")
            if tool == 'gf':
                os.system("go install ./...")
            os.chdir("..")
        else:
            print(f"[+] {tool} is already installed.")

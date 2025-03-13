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
        "openredirect": "https://github.com/ak1t4/openredirect"
    })
    for tool, repo in dependencies.items():
        if not command_exists(tool):
            print(f"[+] Installing {tool}...")
            os.system(f"git clone {repo}")
            tool_dir = repo.split('/')[-1]
            if os.path.exists(f"./{tool_dir}/go.mod"):
                os.chdir(tool_dir)
                os.system("go mod init")
                os.system("go build .")
                os.chdir("..")
            else:
                os.system(f"cd {tool_dir} && go build . && cd ..")
        else:
            print(f"[+] {tool} is already installed.")

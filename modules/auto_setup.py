import os
import subprocess
import argparse
import json

def command_exists(cmd):
    return subprocess.call(["which", cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

def install_dependencies(config, verbose):
    dependencies = config.get("dependencies", {
        "subfinder": "https://github.com/projectdiscovery/subfinder",
        "assetfinder": "https://github.com/tomnomnom/assetfinder",
        "httpx": "https://github.com/projectdiscovery/httpx",
        "nuclei": "https://github.com/projectdiscovery/nuclei",
        "katana": "https://github.com/projectdiscovery/katana",
        "gf": "https://github.com/tomnomnom/gf",
        "bxss": "https://github.com/1N3/BXSS",
        "sqlmap": "https://github.com/sqlmapproject/sqlmap",
        "corsy": "https://github.com/s0md3v/Corsy",
        "subzy": "https://github.com/LukaSikic/subzy"
    })
    for tool, repo in dependencies.items():
        if not command_exists(tool):
            print(f"[+] Installing {tool}...")
            if os.path.exists(tool):
                os.system(f"rm -rf {tool}")
            os.system(f"git clone {repo}")
            tool_dir = repo.split('/')[-1]
            os.chdir(tool_dir)
            if tool in ['subfinder', 'assetfinder', 'httpx', 'nuclei', 'katana']:
                os.system("go build .")
            if tool == 'gf':
                os.system("go install ./...")
            os.chdir("..")
        else:
            print(f"[+] {tool} is already installed.")

def main():
    parser = argparse.ArgumentParser(description="Automated Setup")
    parser.add_argument("--target", required=True, help="Target domain or IP address")
    parser.add_argument("--threads", type=int, default=50, help="Number of threads")
    parser.add_argument("--output", default="./results", help="Output directory")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    args = parser.parse_args()

    # Load config
    with open("config.json", "r") as f:
        config = json.load(f)

    install_dependencies(config, args.verbose)

if __name__ == "__main__":
    main()

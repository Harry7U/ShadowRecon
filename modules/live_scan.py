import os

def find_live_hosts(subdomains_file, config):
    output_file = "subdomains_alive.txt"
    print("[+] Scanning for live hosts...")
    os.system(f"cat {subdomains_file} | httpx -ports 80,443,8080,8000,8888 -threads 200 > {output_file}")
    print(f"[+] Live hosts saved to {output_file}")
    return output_file

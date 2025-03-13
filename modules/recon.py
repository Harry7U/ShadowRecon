import os

def enumerate_subdomains(target, config):
    output_file = "subdomains.txt"
    print(f"[+] Enumerating subdomains for {target}...")
    os.system(f"subfinder -d {target} -all -recursive > {output_file}")
    os.system(f"assetfinder {target} >> {output_file}")
    print(f"[+] Subdomains saved to {output_file}")
    return output_file

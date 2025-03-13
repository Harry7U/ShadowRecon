import os

def enumerate_subdomains(target, config):
    output_file = "subdomains.txt"
    print(f"[+] Enumerating subdomains for {target}...")
    # Using subfinder & assetfinder via bash commands.
    # You could also wrap the commands using subprocess.
    os.system(f"subfinder -d {target} -all -recursive > {output_file}")
    os.system(f"assetfinder {target} >> {output_file}")
    print(f"[+] Subdomains saved to {output_file}")
    return output_file

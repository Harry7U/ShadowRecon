import os
import argparse

def enumerate_subdomains(target, output_dir, verbose):
    output_file = os.path.join(output_dir, "subdomains.txt")
    print(f"[+] Enumerating subdomains for {target}...")
    os.system(f"subfinder -d {target} -all -recursive > {output_file}")
    os.system(f"assetfinder {target} >> {output_file}")
    print(f"[+] Subdomains saved to {output_file}")
    return output_file

def main():
    parser = argparse.ArgumentParser(description="Subdomain Enumeration")
    parser.add_argument("--target", required=True, help="Target domain")
    parser.add_argument("--output", default="./results", help="Output directory")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    args = parser.parse_args()

    enumerate_subdomains(args.target, args.output, args.verbose)

if __name__ == "__main__":
    main()

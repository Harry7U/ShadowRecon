import os
import argparse

def find_live_hosts(subdomains_file, output_dir, verbose):
    output_file = os.path.join(output_dir, "subdomains_alive.txt")
    print("[+] Scanning for live hosts...")
    os.system(f"cat {subdomains_file} | httpx -ports 80,443,8080,8000,8888 -threads 200 -silent > {output_file}")
    print(f"[+] Live hosts saved to {output_file}")
    return output_file

def main():
    parser = argparse.ArgumentParser(description="Live Host Detection")
    parser.add_argument("--output", default="./results", help="Output directory")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    args = parser.parse_args()

    find_live_hosts(os.path.join(args.output, "subdomains.txt"), args.output, args.verbose)

if __name__ == "__main__":
    main()

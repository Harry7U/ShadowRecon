import os
import argparse

def discover_sensitive_files(urls_file, output_dir, verbose):
    sensitive_files = os.path.join(output_dir, "sensitive_files.txt")
    print("[+] Discovering sensitive files...")
    os.system(f"cat {urls_file} | grep -E '\\.txt|\\.log|\\.cache|\\.secret|\\.db|\\.backup|\\.yml|\\.json|\\.gz|\\.rar|\\.zip|\\.config' > {sensitive_files}")
    print(f"[+] Sensitive files saved to {sensitive_files}")
    return sensitive_files

def main():
    parser = argparse.ArgumentParser(description="Sensitive File Discovery")
    parser.add_argument("--output", default="./results", help="Output directory")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    args = parser.parse_args()

    discover_sensitive_files(os.path.join(args.output, "allurls.txt"), args.output, args.verbose)

if __name__ == "__main__":
    main()

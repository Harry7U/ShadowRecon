import os
import argparse

def extract_data(active_hosts_file, output_dir, verbose):
    urls_file = os.path.join(output_dir, "allurls.txt")
    js_file = os.path.join(output_dir, "js.txt")
    sensitive_files = os.path.join(output_dir, "sensitive_files.txt")
    print("[+] Extracting URLs and JavaScript files...")
    os.system(f"katana -list {active_hosts_file} -d 5 -ps -pss waybackarchive,commoncrawl,alienvault -kf -jc -fx -ef woff,css,png,svg,jpg,woff2,jpeg,gif,svg -o {urls_file}")
    os.system(f"cat {urls_file} | grep -E '\\.js$' > {js_file}")
    os.system(f"cat {urls_file} | grep -E '\\.txt|\\.log|\\.cache|\\.secret|\\.db|\\.backup|\\.yml|\\.json|\\.gz|\\.rar|\\.zip|\\.config' > {sensitive_files}")
    print(f"[+] URLs saved to {urls_file}, JavaScript files to {js_file}, and sensitive files to {sensitive_files}")
    return urls_file, js_file, sensitive_files

def main():
    parser = argparse.ArgumentParser(description="URL Extraction")
    parser.add_argument("--output", default="./results", help="Output directory")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    args = parser.parse_args()

    extract_data(os.path.join(args.output, "subdomains_alive.txt"), args.output, args.verbose)

if __name__ == "__main__":
    main()

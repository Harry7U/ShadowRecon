import os
import argparse

def scan_vulnerabilities(active_hosts_file, urls_file, js_file, output_dir, verbose):
    results_file = os.path.join(output_dir, "vuln_results.json")
    js_exposures_file = os.path.join(output_dir, "js_exposures.txt")
    js_root_exposures_file = os.path.join(output_dir, "js_root_exposures.txt")
    print("[+] Scanning for vulnerabilities using nuclei...")
    os.system(f"nuclei -list {active_hosts_file} -tags cve,osint,tech -silent -o nuclei_scan_results.txt")
    os.system(f"cat {urls_file} | grep -E 'lfi' | nuclei -tags lfi -silent -o lfi_results.txt")
    os.system(f"nuclei -list {js_file} -t ~/nuclei-templates/http/exposures/ -c 30 -o {js_exposures_file}")
    os.system(f"echo 'www.target.com' | katana -ps | grep -E '\\.js$' | nuclei -t ~/nuclei-templates/http/exposures/ -c 30 -o {js_root_exposures_file}")
    print(f"[+] Vulnerability scan results saved to {results_file}")
    return results_file, js_exposures_file, js_root_exposures_file

def main():
    parser = argparse.ArgumentParser(description="Vulnerability Scanning")
    parser.add_argument("--output", default="./results", help="Output directory")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    args = parser.parse_args()

    scan_vulnerabilities(
        os.path.join(args.output, "subdomains_alive.txt"),
        os.path.join(args.output, "allurls.txt"),
        os.path.join(args.output, "js.txt"),
        args.output,
        args.verbose
    )

if __name__ == "__main__":
    main()

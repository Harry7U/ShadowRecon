#!/usr/bin/env python3
import argparse
import json
from modules import auto_setup, recon, live_scan, url_extract, vuln_scanner, exploitation, reporting

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description="Automated Bug Hunting & Security Recon Tool")
    parser.add_argument("--target", required=True, help="Target domain or IP address")
    parser.add_argument("--modules", nargs="+", choices=["setup", "recon", "livescan", "url_extract", "vuln", "exploit", "report"],
                        default=["setup", "recon", "livescan", "url_extract", "vuln", "exploit", "report"],
                        help="Specify which modules to run")
    args = parser.parse_args()

    config = load_config()

    if "setup" in args.modules:
        auto_setup.install_dependencies(config)

    if "recon" in args.modules:
        subdomains = recon.enumerate_subdomains(args.target, config)
    else:
        subdomains = "subdomains.txt"  # default file

    if "livescan" in args.modules:
        active_hosts = live_scan.find_live_hosts(subdomains, config)
    else:
        active_hosts = "subdomains_alive.txt"

    if "url_extract" in args.modules:
        urls, js_files = url_extract.extract_data(active_hosts, config)
    
    if "vuln" in args.modules:
        vuln_results = vuln_scanner.scan_vulnerabilities(active_hosts, urls, js_files, config)
    
    if "exploit" in args.modules:
        exploitation.detect_exploits(urls, config)
    
    if "report" in args.modules:
        reporting.generate_report({
            "target": args.target,
            "subdomains": subdomains,
            "active_hosts": active_hosts,
            "urls": urls,
            "js_files": js_files,
            "vuln_results": vuln_results,
        }, config)

if __name__ == "__main__":
    main()

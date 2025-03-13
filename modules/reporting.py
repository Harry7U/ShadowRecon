import os
import json
import csv
import markdown
import argparse

def generate_report(scan_results, output_dir, verbose):
    json_report = os.path.join(output_dir, "report.json")
    csv_report = os.path.join(output_dir, "report.csv")
    md_report = os.path.join(output_dir, "report.md")
    html_report = os.path.join(output_dir, "report.html")

    with open(json_report, "w") as f:
        json.dump(scan_results, f, indent=4)

    with open(csv_report, "w") as f:
        writer = csv.writer(f)
        for key, value in scan_results.items():
            writer.writerow([key, value])

    with open(md_report, "w") as f:
        f.write("# Scan Results\n")
        for key, value in scan_results.items():
            f.write(f"## {key}\n")
            f.write(f"{value}\n")

    with open(md_report, "r") as f:
        html_content = markdown.markdown(f.read())

    with open(html_report, "w") as f:
        f.write(html_content)

    print(f"[+] Reports saved to {output_dir}")

def main():
    parser = argparse.ArgumentParser(description="Reporting")
    parser.add_argument("--output", default="./results", help="Output directory")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    args = parser.parse_args()

    scan_results = {
        "target": args.target,
        "subdomains": os.path.join(args.output, "subdomains.txt"),
        "active_hosts": os.path.join(args.output, "subdomains_alive.txt"),
        "urls": os.path.join(args.output, "allurls.txt"),
        "js_files": os.path.join(args.output, "js.txt"),
        "sensitive_files": os.path.join(args.output, "sensitive_files.txt"),
        "vuln_results": os.path.join(args.output, "vuln_results.json"),
        "js_exposures_file": os.path.join(args.output, "js_exposures.txt"),
        "js_root_exposures_file": os.path.join(args.output, "js_root_exposures.txt")
    }

    generate_report(scan_results, args.output, args.verbose)

if __name__ == "__main__":
    main()

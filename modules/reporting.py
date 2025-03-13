import json
import csv
import os

def generate_report(data, config):
    print("[+] Generating structured reports...")
    with open("report.json", "w") as jf:
        json.dump(data, jf, indent=4)
    print("[+] JSON report generated: report.json")
    with open("report.csv", "w", newline="") as cf:
        writer = csv.writer(cf)
        writer.writerow(["Module", "Output File/Details"])
        writer.writerow(["Subdomains", data.get("subdomains")])
        writer.writerow(["Active Hosts", data.get("active_hosts")])
        writer.writerow(["URLs", data.get("urls")])
        writer.writerow(["JS Files", data.get("js_files")])
        writer.writerow(["Vuln Results", data.get("vuln_results")])
    print("[+] CSV report generated: report.csv")
    with open("report.md", "w") as mf:
        mf.write("# Bug Hunting & Security Recon Report\n\n")
        mf.write(f"**Target:** {data.get('target')}\n\n")
        mf.write("## Summary\n")
        mf.write("- Subdomains: " + str(data.get("subdomains")) + "\n")
        mf.write("- Active Hosts: " + str(data.get("active_hosts")) + "\n")
        mf.write("- Vulnerability Results: " + str(data.get("vuln_results")) + "\n")
    print("[+] Markdown report generated: report.md")
    with open("report.html", "w") as hf:
        hf.write("<html><head><title>Recon Report</title></head><body>")
        hf.write("<h1>Bug Hunting & Security Recon Report</h1>")
        hf.write(f"<h2>Target: {data.get('target')}</h2>")
        hf.write("<ul>")
        hf.write("<li>Subdomains: " + str(data.get("subdomains")) + "</li>")
        hf.write("<li>Active Hosts: " + str(data.get("active_hosts")) + "</li>")
        hf.write("<li>Vulnerability Results: " + str(data.get("vuln_results")) + "</li>")
        hf.write("</ul>")
        hf.write("</body></html>")
    print("[+] HTML report generated: report.html")

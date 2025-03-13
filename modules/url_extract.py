import os

def extract_data(active_hosts_file, config):
    urls_file = "allurls.txt"
    js_file = "js.txt"
    print("[+] Extracting URLs and JavaScript files...")
    os.system(f"katana -u {active_hosts_file} -d 5 -ps -pss waybackarchive,commoncrawl,alienvault -kf -jc -fx -ef -o {urls_file}")
    os.system(f"cat {urls_file} | grep -E '\\.js$' >> {js_file}")
    print(f"[+] URLs saved to {urls_file} and JavaScript files to {js_file}")
    return urls_file, js_file

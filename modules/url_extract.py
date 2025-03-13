import os

def extract_data(active_hosts_file, config):
    urls_file = "allurls.txt"
    js_file = "js.txt"
    sensitive_files = "sensitive_files.txt"
    print("[+] Extracting URLs and JavaScript files...")
    os.system(f"katana -list {active_hosts_file} -d 5 -ps -pss waybackarchive,commoncrawl,alienvault -kf -jc -fx -ef woff,css,png,svg,jpg,woff2,jpeg,gif,svg -o {urls_file}")
    os.system(f"cat {urls_file} | grep -E '\\.js$' > {js_file}")
    os.system(f"cat {urls_file} | grep -E '\\.txt|\\.log|\\.cache|\\.secret|\\.db|\\.backup|\\.yml|\\.json|\\.gz|\\.rar|\\.zip|\\.config' > {sensitive_files}")
    print(f"[+] URLs saved to {urls_file}, JavaScript files to {js_file}, and sensitive files to {sensitive_files}")
    return urls_file, js_file, sensitive_files

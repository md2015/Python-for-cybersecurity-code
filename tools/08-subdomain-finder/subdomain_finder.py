# subdomain_finder.py
# Multithreaded subdomain finder using DNS resolution

import datetime
import socket
from concurrent.futures import ThreadPoolExecutor


domain = input("Enter target domain (e.g. example.com): ").strip()
wordfile = input("Path to wordlist file: ").strip()

try:
    with open(wordfile, "r") as f:
        wordlist = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("Wordlist file not found.")
    raise SystemExit

found = []


def check_subdomain(name):
    subdomain = f"{name}.{domain}"
    try:
        ip = socket.gethostbyname(subdomain)
        return subdomain, ip
    except socket.gaierror:
        return None


with ThreadPoolExecutor(max_workers=20) as executor:
    results = executor.map(check_subdomain, wordlist)

    for result in results:
        if result:
            subdomain, ip = result
            found.append((subdomain, ip))
            print(f"FOUND: {subdomain} -> {ip}")

report_name = f"subdomains_{domain}.txt"
with open(report_name, "w") as report:
    report.write(f"Subdomain report for {domain}\n")
    report.write(f"Generated: {datetime.datetime.now()}\n")
    report.write("=" * 50 + "\n")
    for subdomain, ip in found:
        report.write(f"{subdomain} -> {ip}\n")

print(
    f"Done. Found {len(found)} subdomains. Report saved as {report_name}"
)

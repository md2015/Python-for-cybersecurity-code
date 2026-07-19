# 08 Subdomain Finder

Raw code, terminal commands, sample output, and monospaced templates extracted from the PDF text layer. Page wraps and teaching-snippet indentation are preserved as closely as possible. Use the cleaned scripts in `../tools/` for runnable versions.

## PDF page 83

```python
import socket
def check_subdomain(domain, word):
    subdomain = f"{word}.{domain}"
    try:
        ip = socket.gethostbyname(subdomain)
        return subdomain, ip
    except socket.gaierror:
        return None, None
result, ip = check_subdomain("example.com", "www")
if result:
    print(f"FOUND: {result} -> {ip}")
```

## PDF page 84

```python
from concurrent.futures import ThreadPoolExecutor
def check(word):
    return check_subdomain(domain, word) # defined above
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(check, wordlist)
        for subdomain, ip in results:
            if subdomain:
                print(f"FOUND: {subdomain} -> {ip}")
www
mail
ftp
api
dev
staging
test
admin
portal
vpn
remote
store
shop
blog
docs
support
```

## PDF page 85

```python
help
status
cdn
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
```

## PDF page 86

```python
            found.append((subdomain, ip))
            print(f"FOUND: {subdomain} -> {ip}")
report_name = f"subdomains_{domain}.txt"
with open(report_name, "w") as report:
    report.write(f"Subdomain report for {domain}\n")
    report.write(f"Generated: {datetime.datetime.now()}\n")
    report.write("=" * 50 + "\n")
    for subdomain, ip in found:
        report.write(f"{subdomain} -> {ip}\n")
print(f"Done. Found {len(found)} subdomains. Report saved as 
{report_name}")
```


# 13 Portfolio Toolkit

Raw code, terminal commands, sample output, and monospaced templates extracted from the PDF text layer. Page wraps and teaching-snippet indentation are preserved as closely as possible. Use the cleaned scripts in `../tools/` for runnable versions.

## PDF page 141

```text
Ten working security tools built in Python.
Each tool teaches a security concept while producing
a script I can actually use and explain.
pip install -r requirements.txt
```

## PDF page 142

```text
All tools are for authorized use only.
Test only on systems you own or have permission to test.
SECURITY ASSESSMENT REPORT
Target: [IP address or domain]
Date: [YYYY-MM-DD]
Assessor: [Your name]
Scope: [What was authorized to test]
EXECUTIVE SUMMARY
[2-3 sentences. What was found. How serious. What to do.]
FINDINGS
Finding #1:
Severity: HIGH / MEDIUM / LOW / INFORMATIONAL
Issue: [What the problem is]
Evidence: [What the tool found]
Risk: [What an attacker could do with this]
Fix: [Specific remediation steps]
TOOLS USED
[List the scripts you ran and their outputs]
DISCLAIMER
This assessment was conducted on [date] with written
authorization from [name/organization].
```

## PDF page 145

```python
def get_file_hash(filepath):
"""
Compute the SHA256 hash of a file using chunked reading.
Args: filepath (str) - path to the file
Returns: str - 64-character hexadecimal hash, or None on error
"""
sha256 = hashlib.sha256()
...
# Instead of this:
if count >= 5:
    # Write this:
    ALERT_THRESHOLD = 5
    if count >= ALERT_THRESHOLD:
```

## PDF page 148

```python
import hashlib
def hash_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
h.update(chunk)
return h.hexdigest()
import socket
def port_open(host, port, timeout=1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(timeout)
result = s.connect_ex((host, port))
s.close()
return result == 0
import requests
def safe_get(url, timeout=5):
    try:
        return requests.get(url, timeout=timeout)
    except requests.RequestException:
        return None
import secrets, string
def make_password(length=16):
    pool = string.ascii_letters + string.digits + string.punctuation
    chars = [
secrets.choice(string.ascii_uppercase),
secrets.choice(string.digits),
secrets.choice(string.punctuation),
*[secrets.choice(pool) for _ in range(length - 3)]
]
secrets.SystemRandom().shuffle(chars)
return "".join(chars)
import re
IP_PATTERN = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
```

## PDF page 149

```python
def extract_ip(log_line):
    m = IP_PATTERN.search(log_line)
    return m.group() if m else None
import socket
from concurrent.futures import ThreadPoolExecutor
def check_subdomain(word, domain):
    target = f'{word}.{domain}'
    try: return target, socket.gethostbyname(target)
except socket.gaierror: return None, None
def find_subdomains(domain, wordlist, workers=20):
    found = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for sub, ip in ex.map(lambda w: check_subdomain(w, domain), 
wordlist):
            if sub: found.append((sub, ip))
            return found
import json
def save_json(data, path):
    with open(path, "w") as f: json.dump(data, f, indent=2)
    def load_json(path):
        with open(path, "r") as f: return json.load(f)
PORT_LABELS = {
21: 'FTP', 22: 'SSH', 25: 'SMTP', 53: 'DNS',
80: 'HTTP', 443:'HTTPS', 3306:'MySQL', 8080:'HTTP-Alt',
5432:'PostgreSQL', 6379:'Redis', 27017:'MongoDB',
3389:'RDP', 1433:'MSSQL', 8443:'HTTPS-Alt'
}
SECURITY_HEADERS = [
'Content-Security-Policy',
'X-Frame-Options',
'X-Content-Type-Options',
'Strict-Transport-Security',
'Referrer-Policy',
'Permissions-Policy',
]
def missing_headers(response_headers):
    return [h for h in SECURITY_HEADERS if h not in response_headers]
```


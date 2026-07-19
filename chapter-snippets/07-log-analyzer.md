# 07 Log Analyzer

Raw code, terminal commands, sample output, and monospaced templates extracted from the PDF text layer. Page wraps and teaching-snippet indentation are preserved as closely as possible. Use the cleaned scripts in `../tools/` for runnable versions.

## PDF page 74

```text
192.168.1.100 - admin [15/Jan/2024:10:20:45 -0500] "POST /login HTTP/1.1" 
401 512
```

## PDF page 75

```python
import re
# A simple pattern: match any three digits followed by a dot
pattern = re.compile(r"\d{3}\.")
match = pattern.search("Server responded: 401.5")
if match:
    print(match.group()) # prints 401.
LOG_PATTERN = re.compile(
r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # IP address
r'.*"\S+ (?P<path>\S+) HTTP' # request path
r'.*" (?P<code>\d{3})' # response code
)
from collections import defaultdict
failed_logins = defaultdict(int) # default value is 0 for any new key
# No need to check if the key exists before incrementing:
failed_logins["192.168.1.100"] += 1 # creates key with 0, then adds 1
failed_logins["192.168.1.100"] += 1 # now 2
failed_logins["10.0.0.5"] += 1 # new key, starts at 0, then 1
```

## PDF page 76

```python
# Sort by count, highest first:
sorted_ips = sorted(
failed_logins.items(),
key=lambda x: x[1],
reverse=True
)
for ip, count in sorted_ips[:10]: # top 10
print(f"{ip}: {count} failed attempts")
with open("access.log", "r") as f:
    lines = f.readlines()
    print(f"Loaded {len(lines)} log entries")
LOG_PATTERN = re.compile(
r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
r'.*"\S+ (?P<path>\S+) HTTP'
r'.*" (?P<code>\d{3})'
)
for line in lines:
    match = LOG_PATTERN.search(line)
    if match:
        ip = match.group('ip')
        path = match.group('path')
        code = match.group('code')
THRESHOLD = 5 # alert if an IP has this many failed logins
failed_logins = defaultdict(int)
for line in lines:
    match = LOG_PATTERN.search(line)
    if not match:
        continue
        code = match.group('code')
        ip = match.group('ip')
        if code in ('401', '403'):
failed_logins[ip] += 1
# log_analyzer.py
# Parses Apache/Nginx access logs and flags brute-force attempts
import datetime
```

## PDF page 77

```python
import re
from collections import defaultdict
LOG_FILE = "access.log"
REPORT = "threat_report.txt"
THRESHOLD = 5
LOG_PATTERN = re.compile(
    r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    r'.*"\S+ (?P<path>\S+) HTTP'
    r'.*" (?P<status>\d{3}) '
)
failed_logins = defaultdict(int)
all_requests = 0
suspicious_paths = ["/login", "/admin", "/wp-login.php"]
with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as log:
    for line in log:
        match = LOG_PATTERN.search(line)
        if not match:
            continue
        all_requests += 1
        ip = match.group("ip")
        path = match.group("path")
        status = match.group("status")
        if status in ["401", "403"] or path in suspicious_paths:
            failed_logins[ip] += 1
alerts = {
    ip: count for ip, count in failed_logins.items() if count >= THRESHOLD
}
with open(REPORT, "w") as report:
    report.write("Security Log Analysis Report\n")
    report.write(f"Generated: {datetime.datetime.now()}\n")
    report.write("=" * 50 + "\n")
    report.write(f"Total parsed requests: {all_requests}\n")
    report.write(f"Alert threshold: {THRESHOLD} failed/suspicious 
requests\n\n")
    if alerts:
        report.write("ALERTS\n")
        for ip, count in sorted(alerts.items(), key=lambda item: item[1], 
reverse=True):
            report.write(f"{ip}: {count} suspicious requests\n")
    else:
        report.write("No brute-force alerts detected.\n")
print(f"Analysis complete. Report saved as {REPORT}")
```


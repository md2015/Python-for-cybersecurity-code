# log_analyzer.py
# Parses Apache/Nginx access logs and flags brute-force attempts

import datetime
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
    report.write(
        f"Alert threshold: {THRESHOLD} failed/suspicious requests\n\n"
    )

    if alerts:
        report.write("ALERTS\n")
        for ip, count in sorted(
            alerts.items(), key=lambda item: item[1], reverse=True
        ):
            report.write(f"{ip}: {count} suspicious requests\n")
    else:
        report.write("No brute-force alerts detected.\n")

print(f"Analysis complete. Report saved as {REPORT}")

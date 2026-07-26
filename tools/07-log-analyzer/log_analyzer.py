# log_analyzer.py
# Parses Apache/Nginx access logs and flags repeated
# authorization failures

import datetime
import re
from collections import defaultdict

LOG_FILE = "access.log"
REPORT = "threat_report.txt"
THRESHOLD = 5

LOG_PATTERN = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})'
    r'.*"\S+ (?P<path>\S+) HTTP/[^\"]+" '
    r'(?P<status>\d{3}) '
)


def analyze_log(log_file, threshold=5):
    if threshold < 1:
        raise ValueError("Threshold must be at least 1.")

    failed_logins = defaultdict(int)
    all_requests = 0

    with open(
        log_file,
        "r",
        encoding="utf-8",
        errors="ignore",
    ) as log:
        for line in log:
            match = LOG_PATTERN.search(line)
            if not match:
                continue

            all_requests += 1
            status = match.group("status")

            if status in {"401", "403"}:
                ip = match.group("ip")
                failed_logins[ip] += 1

    alerts = {
        ip: count
        for ip, count in failed_logins.items()
        if count >= threshold
    }

    return all_requests, alerts


def main():
    try:
        all_requests, alerts = analyze_log(LOG_FILE, THRESHOLD)
    except (OSError, ValueError) as error:
        print(f"Could not analyze the log: {error}")
        return

    with open(REPORT, "w", encoding="utf-8") as report:
        report.write("Security Log Analysis Report\n")
        report.write(
            "Generated: "
            + datetime.datetime.now().isoformat(
                timespec="seconds"
            )
            + "\n"
        )
        report.write("=" * 50 + "\n")
        report.write(f"Total parsed requests: {all_requests}\n")
        report.write(
            f"Alert threshold: {THRESHOLD} "
            "authorization failures\n\n"
        )

        if alerts:
            report.write("ALERTS\n")
            for ip, count in sorted(
                alerts.items(),
                key=lambda item: item[1],
                reverse=True,
            ):
                report.write(
                    f"{ip}: {count} "
                    "authorization failures\n"
                )
        else:
            report.write("No brute-force alerts detected.\n")

    print(f"Analysis complete. Report saved as {REPORT}")


if __name__ == "__main__":
    main()

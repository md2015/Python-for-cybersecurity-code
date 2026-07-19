# username_search.py
# OSINT tool: searches a username across multiple websites

import datetime

import requests


username = input("Enter a username to search: ").strip()

sites = [
    "https://github.com/",
    "https://reddit.com/u/",
    "https://x.com/",
    "https://instagram.com/",
    "https://linkedin.com/in/",
    "https://medium.com/@",
    "https://dev.to/",
]

report_name = f"osint_report_{username}.txt"

with open(report_name, "w", encoding="utf-8") as report:
    report.write(f"OSINT Username Report: {username}\n")
    report.write(f"Generated: {datetime.datetime.now()}\n")
    report.write("=" * 50 + "\n")

    for site in sites:
        url = site + username
        print(f"Checking {url}")

        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                result = f"FOUND: {url}"
            elif response.status_code == 404:
                result = f"Not found: {url}"
            else:
                result = f"Unknown ({response.status_code}): {url}"
        except requests.RequestException as error:
            result = f"Error checking {url}: {error}"

        print(result)
        report.write(result + "\n")

print(f"Report saved as {report_name}")

# username_search.py
# Consent-based OSINT checker for public profile URL patterns

import datetime
import re
from urllib.parse import quote

import requests

SITES = [
    "https://github.com/{}",
    "https://reddit.com/u/{}",
    "https://x.com/{}",
    "https://instagram.com/{}",
    "https://linkedin.com/in/{}",
    "https://medium.com/@{}",
    "https://dev.to/{}",
]

USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9_.-]{1,100}$")


def search_username(username, timeout=5):
    if not USERNAME_PATTERN.fullmatch(username):
        raise ValueError(
            "Use only letters, numbers, periods, "
            "underscores, and hyphens."
        )

    encoded_username = quote(username, safe="")
    headers = {
        "User-Agent": (
            "Python-Cybersecurity-Book/2.0 "
            "educational OSINT checker"
        )
    }
    results = []

    for site in SITES:
        url = site.format(encoded_username)
        print(f"Checking {url}")

        try:
            response = requests.get(
                url,
                timeout=timeout,
                headers=headers,
                allow_redirects=True,
            )
            if response.status_code == 404:
                result = f"Not found: {url}"
            elif response.status_code == 200:
                result = f"Possible match: {url}"
            else:
                result = (
                    f"Inconclusive "
                    f"({response.status_code}): {url}"
                )
        except requests.RequestException as error:
            result = f"Error checking {url}: {error}"

        print(result)
        results.append(result)

    return results


def main():
    username = input("Enter a username to search: ").strip()

    try:
        results = search_username(username)
    except ValueError as error:
        print(f"Invalid username: {error}")
        return

    report_name = f"osint_report_{username}.txt"
    with open(report_name, "w", encoding="utf-8") as report:
        report.write(f"OSINT Username Report: {username}\n")
        report.write(
            "Generated: "
            + datetime.datetime.now().isoformat(
                timespec="seconds"
            )
            + "\n"
        )
        report.write("=" * 50 + "\n")
        report.write("\n".join(results) + "\n")

    print(f"Report saved as {report_name}")


if __name__ == "__main__":
    main()

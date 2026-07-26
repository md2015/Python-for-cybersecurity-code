# subdomain_finder.py
# Multithreaded subdomain finder using DNS resolution

import datetime
import re
import socket
from concurrent.futures import ThreadPoolExecutor

DOMAIN_PATTERN = re.compile(
    r"^(?=.{1,253}$)"
    r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+"
    r"[A-Za-z]{2,63}$"
)


def check_subdomain(name, domain):
    subdomain = f"{name}.{domain}"
    try:
        ip = socket.gethostbyname(subdomain)
        return subdomain, ip
    except (socket.gaierror, UnicodeError):
        return None


def find_subdomains(domain, wordlist, workers=20):
    if not DOMAIN_PATTERN.fullmatch(domain):
        raise ValueError(
            "Enter a valid domain such as example.com."
        )
    if workers < 1:
        raise ValueError("Workers must be at least 1.")

    with ThreadPoolExecutor(
        max_workers=workers
    ) as executor:
        results = executor.map(
            lambda word: check_subdomain(word, domain),
            wordlist,
        )

    return sorted(result for result in results if result)


def main():
    domain = input(
        "Enter target domain (e.g. example.com): "
    ).strip().lower()
    wordfile = input("Path to wordlist file: ").strip()

    try:
        with open(wordfile, "r", encoding="utf-8") as file:
            wordlist = [
                line.strip().lower()
                for line in file
                if line.strip()
            ]
        found = find_subdomains(domain, wordlist)
    except (OSError, ValueError) as error:
        print(f"Could not start the search: {error}")
        return

    for subdomain, ip in found:
        print(f"FOUND: {subdomain} -> {ip}")

    report_name = f"subdomains_{domain}.txt"
    with open(report_name, "w", encoding="utf-8") as report:
        report.write(f"Subdomain report for {domain}\n")
        report.write(
            "Generated: "
            + datetime.datetime.now().isoformat(
                timespec="seconds"
            )
            + "\n"
        )
        report.write("=" * 50 + "\n")
        for subdomain, ip in found:
            report.write(f"{subdomain} -> {ip}\n")

    print(
        f"Done. Found {len(found)} subdomains. "
        f"Report saved as {report_name}"
    )


if __name__ == "__main__":
    main()

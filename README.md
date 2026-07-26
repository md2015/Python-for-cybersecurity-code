# Python for Cybersecurity: Companion Code

Official companion code for **Python for Cybersecurity: Build 10 Real Security Tools and Become Job Ready** by **Md Shafiqul Baten Sumon**.

This corrected edition contains the complete Python programs from the final publication-ready manuscript. The scripts were checked for syntax, indentation, resource handling, input validation, and expected behavior in controlled tests.

## Tools

| # | Tool | Main file |
|---|---|---|
| 1 | Password Strength Checker | `tools/01-password-strength-checker/password_checker.py` |
| 2 | TCP Port Scanner | `tools/02-network-scanner/scanner.py` |
| 3 | Passive Banner Grabber | `tools/03-banner-grabber/banner.py` |
| 4 | OSINT Username Tracker | `tools/04-osint-username-tracker/username_search.py` |
| 5 | Secure Password Generator | `tools/05-password-generator/generate.py` |
| 6 | File Integrity Monitor | `tools/06-file-integrity-monitor/monitor.py` |
| 7 | Log Analyzer | `tools/07-log-analyzer/log_analyzer.py` |
| 8 | Subdomain Finder | `tools/08-subdomain-finder/subdomain_finder.py` |
| 9 | Packet Sniffer | `tools/09-packet-sniffer/sniffer.py` |
| 10 | Limited Web Security Checker | `tools/10-web-vulnerability-scanner/web_scanner.py` |

The Chapter 1 setup script is available at `chapter-01-setup/hello.py`.

## Requirements

Use Python 3.10 or newer.

```bash
python -m venv venv
```

Windows:

```powershell
venv\Scripts\activate
```

macOS or Linux:

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run the automated tests:

```bash
pytest -q
```

## Quick examples

Password checker:

```bash
python tools/01-password-strength-checker/password_checker.py
```

Port scanner, configured by constants near the top of the file:

```bash
python tools/02-network-scanner/scanner.py
```

Secure password generator. Its default is one mixed 16-character password:

```bash
python tools/05-password-generator/generate.py
python tools/05-password-generator/generate.py --length 20 --count 5
python tools/05-password-generator/generate.py --no-symbols
```

Log analyzer:

```bash
cp sample-data/access.log tools/07-log-analyzer/access.log
python tools/07-log-analyzer/log_analyzer.py
```

On Windows PowerShell, use:

```powershell
Copy-Item sample-data\access.log tools\07-log-analyzer\access.log
python tools\07-log-analyzer\log_analyzer.py
```

Subdomain finder:

```bash
python tools/08-subdomain-finder/subdomain_finder.py
```

When prompted, enter a domain that you are authorized to assess and provide `sample-data/subdomains.txt` as the wordlist path.

Packet sniffer:

```bash
sudo python tools/09-packet-sniffer/sniffer.py
```

Packet capture normally requires administrator or root privileges. Use it only on networks and systems where capture is explicitly authorized.

## Important limitations

The password checker is a teaching exercise, not a complete enterprise password-policy engine. The username tracker can produce false positives because some sites return custom pages instead of standard `404` responses. The web checker performs a few limited, non-exploitative checks and cannot prove that a site is secure.

## Testing status

All ten tools pass controlled automated tests. Network and web tests use local or mocked services. The packet sniffer is tested with a synthetic packet rather than a live capture. See `TEST_STATUS.md` for details.

## Legal and ethical use

Use these programs only on systems you own or systems for which you have clear, explicit, written permission. See `DISCLAIMER.md`.

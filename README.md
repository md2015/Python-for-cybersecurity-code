# Python for Cybersecurity: Companion Code

Code extracted from **Python for Cybersecurity: Build 10 Real Security Tools and Become Job Ready** by **Md Shafiqul Baten Sumon**.

The PDF line wrapping and indentation were cleaned so the complete scripts are valid Python. The program logic remains faithful to the book. The `chapter-snippets` and `reference` folders preserve the smaller examples, terminal commands, sample output, and supplementary code shown throughout the book.

## Tools

| # | Tool | Main file |
|---|---|---|
| 1 | Password Strength Checker | `tools/01-password-strength-checker/password_checker.py` |
| 2 | Network Scanner | `tools/02-network-scanner/scanner.py` |
| 3 | Banner Grabber | `tools/03-banner-grabber/banner.py` |
| 4 | OSINT Username Tracker | `tools/04-osint-username-tracker/username_search.py` |
| 5 | Secure Password Generator | `tools/05-password-generator/generate.py` |
| 6 | File Integrity Monitor | `tools/06-file-integrity-monitor/monitor.py` |
| 7 | Log Analyzer | `tools/07-log-analyzer/log_analyzer.py` |
| 8 | Subdomain Finder | `tools/08-subdomain-finder/subdomain_finder.py` |
| 9 | Packet Sniffer | `tools/09-packet-sniffer/sniffer.py` |
| 10 | Web Vulnerability Scanner | `tools/10-web-vulnerability-scanner/web_scanner.py` |

The first lab script is also included at `chapter-01-setup/hello.py`.

## Setup

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS or Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Example commands

```bash
python tools/01-password-strength-checker/password_checker.py
python tools/05-password-generator/generate.py --length 20 --count 5 --upper --digits --symbols
python tools/06-file-integrity-monitor/monitor.py
```

For the log analyzer, copy the sample log into its tool folder first:

```bash
cp sample-data/access.log tools/07-log-analyzer/access.log
python tools/07-log-analyzer/log_analyzer.py
```

For the subdomain finder, provide `sample-data/subdomains.txt` when prompted.

The packet sniffer normally requires administrator or root privileges.

## Legal and ethical use

Use these tools only on systems you own or systems for which you have clear, explicit, written permission. Unauthorized scanning, packet capture, OSINT investigations, password testing, or web assessment may be illegal. No permission means no testing.

## Repository contents

* `tools/`: the ten cleaned, complete scripts
* `chapter-01-setup/`: the first Python lab script
* `chapter-snippets/`: code examples organized by chapter and page
* `reference/all-code-like-text-by-page.md`: every monospaced code, command, output, and template line extracted from the PDF text layer
* `sample-data/`: a DNS wordlist and synthetic Apache-style access log

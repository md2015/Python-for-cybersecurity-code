# 04 Osint Username Tracker

Raw code, terminal commands, sample output, and monospaced templates extracted from the PDF text layer. Page wraps and teaching-snippet indentation are preserved as closely as possible. Use the cleaned scripts in `../tools/` for runnable versions.

## PDF page 49

```python
import requests
url = "https://github.com/testuser"
response = requests.get(url, timeout=5)
print(response.status_code)
import requests
username = "testuser"
url = "https://github.com/" + username
response = requests.get(url, timeout=5)
if response.status_code == 200:
    print("FOUND:", url)
else:
    print("Not found:", url)
import requests
username = "testuser"
sites = [
"https://github.com/",
"https://reddit.com/u/",
"https://x.com/",
"https://instagram.com/",
"https://linkedin.com/in/"
]
for site in sites:
    url = site + username
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        print("[FOUND] ", url)
    else:
        print("[NOT FOUND] ", url)
```

## PDF page 50

```python
try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        result = "[FOUND] " + url
    else:
        result = "[NOT FOUND] " + url
    except Exception:
        result = "[ERROR] " + url
username = input("Enter a username to search: ")
import requests
import datetime
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
filename = username + "_report.txt"
with open(filename, "w") as f:
f.write(f"OSINT Report: {username}\n")
f.write(f"Generated: {timestamp}\n")
f.write("=" * 40 + "\n\n")
for site in sites:
    url = site + username
    try:
        response = requests.get(url, timeout=5)
        result = "[FOUND] " + url if response.status_code == 200 else 
"[NOT FOUND] " + url
    except Exception:
        result = "[ERROR] " + url
        print(result)
f.write(result + "\n")
# username_search.py
# OSINT tool: searches a username across multiple websites
```

## PDF page 51

```python
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
```


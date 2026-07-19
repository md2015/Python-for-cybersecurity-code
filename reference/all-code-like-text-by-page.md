# All Code-Like Text Extracted by PDF Page

This file contains every line rendered in the PDF with the monospaced font. It includes Python code, shell commands, sample output, error messages, report templates, and a small amount of monospaced explanatory text.

## PDF page 13

```text
Add Python to PATH
```

## PDF page 14

```text
python --version
python3 --version
python3 --version
```

## PDF page 15

```text
sudo apt update
sudo apt install python3 python3-pip -y
```

## PDF page 16

```python
# Windows - creates the folder on your Desktop
cd Desktop
mkdir security_tools
cd security_tools
# Mac or Linux - same result
cd ~/Desktop
mkdir security_tools
cd security_tools
```

## PDF page 17

```python
# Windows
python -m venv venv
# Mac or Linux
python3 -m venv venv
# Windows
venv\Scripts\activate
# Mac or Linux
source venv/bin/activate
```

## PDF page 18

```text
(venv) C:\Desktop\security_tools>
pip is Python's package installer. It downloads libraries from the Python 
Package Index, a public repository with hundreds of thousands of packages. 
pip comes bundled with Python so there is nothing extra to install.
requests
scapy
```

## PDF page 19

```python
pip install -r requirements.txt
pip list
print("My security lab is ready. Let's build something.")
```

## PDF page 20

```python
# Windows
python hello.py
# Mac or Linux
python3 hello.py
My security lab is ready. Let's build something.
```

## PDF page 21

```text
cd foldername: Change Directory. Moves your terminal into a specific 
folder. cd Desktop moves you to the Desktop. cd security_tools moves you 
into that project folder.
cd ..: Moves up one level. If you are inside security_tools, cd .. 
takes you back to Desktop.
python filename.py: Runs a Python script. Replace filename.py with 
the actual script name.
pip install library: Installs a Python library into the active 
virtual environment.
pip list: Shows all installed libraries in the current environment.
```

## PDF page 26

```python
password = "hello123" # stores the text hello123 with the label "password"
score = 0 # stores the number 0 with the label score
issues = [] # stores an empty list with the label issues
```

## PDF page 27

```python
def check_password(password):
    # all the checking code goes inside here
    # indented by four spaces
    return score, issues
    # Calling the function later:
result_score, result_issues = check_password("hello123")
score = 3
if score <= 1:
    verdict = "VERY WEAK" # runs only if score is 0 or 1
elif score == 2:
    verdict = "WEAK" # runs only if score is exactly 2
elif score == 3:
    verdict = "FAIR" # runs only if score is exactly 3
elif score == 4:
    verdict = "STRONG" # runs only if score is exactly 4
else:
    verdict = "VERY STRONG" # runs for any score that did not match above
```

## PDF page 28

```python
issues = [] # empty list
issues.append("Password is too short") # now has one item
issues.append("No numbers found") # now has two items
# Loop through every item in the list:
for issue in issues:
    print(" Problem:", issue)
"A".isupper() # True - is this an uppercase letter?
"3".isdigit() # True - is this a digit?
len("hello") # 5 - how many characters?
# any() checks every character in one line:
any(c.isupper() for c in "Hello123") # True - at least one uppercase found
any(c.isdigit() for c in "Hello123") # True - at least one digit found
```

## PDF page 29

```python
def check_password(password):
    score = 0 # starts at 0, increases for each rule passed
    issues = [] # collects every problem found
if len(password) >= 8:
score += 1
else:
issues.append("Password is too short. Use at least 8 characters.")
has_upper = any(c.isupper() for c in password)
if has_upper:
score += 1
else:
issues.append("No uppercase letters found. Add at least one capital 
letter.")
```

## PDF page 30

```python
has_digit = any(c.isdigit() for c in password)
if has_digit:
score += 1
else:
issues.append("No numbers found. Add at least one digit.")
special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
has_special = any(c in special_chars for c in password)
if has_special:
score += 1
else:
issues.append("No special characters found. Try ! @ # $ or %.")
if len(password) >= 12:
score += 1 # maximum score is 5
return score, issues
def get_verdict(score):
    if score <= 1: return "VERY WEAK"
elif score == 2: return "WEAK"
elif score == 3: return "FAIR"
elif score == 4: return "STRONG"
else: return "VERY STRONG"
def print_results(score, issues):
    verdict = get_verdict(score)
    print(f"Score: {score} / 5")
    print(f"Verdict: {verdict}")
    print()
    if issues:
        print("Issues found:")
```

## PDF page 31

```python
        for issue in issues:
            print(f" - {issue}")
        else:
            print("Excellent password. No issues found.")
            print()
print(): calling print with no argument prints a blank line. Useful 
for spacing out output.
if issues: a list evaluates to True if it has at least one item in 
it. This checks whether any issues were found without needing to count 
them.
print("=" * 40)
print(" Password Strength Checker")
print("=" * 40)
print("Type 'quit' to exit.\n")
while True:
    password = input("Enter a password: ")
    if password.lower() == "quit":
        print("Goodbye.")
        break
score, issues = check_password(password)
print_results(score, issues)
while True: an infinite loop. It keeps running until break is 
called.
input("..."): pauses the script and waits for the user to type 
something and press Enter. Returns whatever they typed as a string.
# password_checker.py
# Scores any password out of 5 and explains every weakness found
def check_password(password):
    score = 0
    issues = []
    if len(password) >= 8:
        score += 1
```

## PDF page 32

```python
    else:
        issues.append("Too short - use at least 8 characters.")
    has_upper = any(c.isupper() for c in password)
    if has_upper:
        score += 1
    else:
        issues.append("No uppercase letters - add at least one capital.")
    has_digit = any(c.isdigit() for c in password)
    if has_digit:
        score += 1
    else:
        issues.append("No numbers - add at least one digit.")
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    has_special = any(c in special_chars for c in password)
    if has_special:
        score += 1
    else:
        issues.append("No special characters - try ! @ # or $.")
    if len(password) >= 12:
        score += 1
    return score, issues
def get_verdict(score):
    if score <= 1:
        return "VERY WEAK"
    elif score == 2:
        return "WEAK"
    elif score == 3:
        return "FAIR"
    elif score == 4:
        return "STRONG"
    else:
        return "VERY STRONG"
def print_results(score, issues):
    verdict = get_verdict(score)
    print(f"Score: {score} / 5")
    print(f"Verdict: {verdict}")
    print()
    if issues:
        print("Issues found:")
        for issue in issues:
            print(f" - {issue}")
    else:
        print("Excellent. No issues found.")
    print()
print("=" * 40)
print(" Password Strength Checker")
print("=" * 40)
print("Type 'quit' to exit.\n")
```

## PDF page 33

```python
while True:
    password = input("Enter a password: ")
    if password.lower() == "quit":
        print("Goodbye.")
        break
    score, issues = check_password(password)
    print_results(score, issues)
python password_checker.py
hello -> Score: 0 / 5 (VERY WEAK) - short, no upper, no digit, no special
Hello1 -> Score: 2 / 5 (WEAK) - no special, too short
Hello123 -> Score: 3 / 5 (FAIR) - no special
Hello123! -> Score: 4 / 5 (STRONG) - all rules, but under 12 chars
Hello123!abc -> Score: 5 / 5 (VERY STRONG) - all rules including length 
bonus
```

## PDF page 38

```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET = use IPv4 addresses
# SOCK_STREAM = use TCP (connection-based, reliable)
result = s.connect_ex(('127.0.0.1', 80))
# result == 0 means connection succeeded = port is OPEN
# result != 0 means connection failed = port is CLOSED or FILTERED
import socket
target = "127.0.0.1"
port = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)
result = s.connect_ex((target, port))
if result == 0:
```

## PDF page 39

```python
    print(f"Port {port} is OPEN")
else:
    print(f"Port {port} is closed")
s.close()
s.settimeout(1): wait at most 1 second for a response. Without this, 
a scan can hang indefinitely on unresponsive ports.
s.close(): always close the socket after using it. Leaving sockets 
open wastes resources.
import socket
target = "127.0.0.1"
start_port = 1
end_port = 1024
print(f"Scanning {target} ...")
for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.5)
result = s.connect_ex((target, port))
if result == 0:
    print(f"Port {port} --- OPEN")
s.close()
port_labels = {
21: "FTP", 22: "SSH", 25: "SMTP", 53: "DNS",
80: "HTTP", 443: "HTTPS", 3306: "MySQL", 8080: "HTTP-Alt"
}
# Inside the port loop:
label = port_labels.get(port, "Unknown")
print(f"Port {port} --- OPEN ({label})")
# scanner.py
# Port scanner with service labels, timing, and file output
import socket
import time
```

## PDF page 40

```python
target = "127.0.0.1"  # change this to your target
start_port = 1
end_port = 1024
output_file = "scan_results.txt"
port_labels = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt",
}
print(f"Scanning {target} ...")
start_time = time.time()
open_ports = 0
found_ports = []
for port in range(start_port, end_port + 1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            label = port_labels.get(port, "Unknown")
            print(f"Port {port} --- OPEN ({label})")
            open_ports += 1
            found_ports.append((port, label))
        s.close()
    except KeyboardInterrupt:
        print("\nScan stopped.")
        break
    except Exception:
        pass
duration = round(time.time() - start_time, 2)
print(f"\nDone. {open_ports} open port(s). Time: {duration}s")
with open(output_file, "w") as f:
    f.write(f"Scan: {target}\n")
    f.write("=" * 40 + "\n")
    for port, label in found_ports:
        f.write(f"Port {port} OPEN ({label})\n")
    f.write(f"\nTotal: {open_ports} open | Time: {duration}s\n")
print(f"Results saved: {output_file}")
```

## PDF page 41

```python
# banner.py
# Grabs service banners to identify software and version information
import socket
def grab_banner(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024).decode("utf-8", errors="ignore").strip()
        s.close()
        return banner
    except Exception:
        return None
target = "127.0.0.1"
ports_to_check = [21, 22, 25, 80, 110, 143]
for port in ports_to_check:
    print(f"Checking port {port}...")
    banner = grab_banner(target, port)
    if banner:
        print(f" Banner: {banner[:100]}")
    else:
        print(" No banner received")
```

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

## PDF page 57

```python
import random
print(random.choice('abcdefghijklmnopqrstuvwxyz'))
import secrets
print(secrets.choice('abcdefghijklmnopqrstuvwxyz'))
```

## PDF page 58

```python
import string
print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits) # 0123456789
print(string.punctuation) # !"#$%&'()*+,-./:;<=>?@[]^_`{|}~
# The long way:
chars = []
for _ in range(10):
chars.append(secrets.choice('abc'))
# The short way (list comprehension):
chars = [secrets.choice('abc') for _ in range(10)]
```

## PDF page 59

```python
# Both produce the same result: a list of 10 random characters
import argparse
parser = argparse.ArgumentParser(description='Secure Password Generator')
parser.add_argument('--length', type=int, default=12)
parser.add_argument('--upper', action='store_true' )
parser.add_argument('--digits', action='store_true' )
parser.add_argument('--symbols', action='store_true' )
args = parser.parse_args()
print(args.length) # 12 by default, or whatever the user typed
print(args.upper) # False by default, True if --upper was passed
# join() turns a list of characters into a single string
chars = ["H", "e", "l", "l", "o"]
word = "".join(chars)
print(word) # Hello
# The string before .join() is the separator between items
"-".join(["a", "b", "c"]) # a-b-c
"".join(["a", "b", "c"]) # abc (no separator)
def generate_password(length, upper, digits, symbols):
    required = []
    available = string.ascii_lowercase
```

## PDF page 60

```python
    if upper:
        required.append(secrets.choice(string.ascii_uppercase))
        available += string.ascii_uppercase
    if digits:
        required.append(secrets.choice(string.digits))
        available += string.digits
    if symbols:
        required.append(secrets.choice(SYMBOLS))
        available += SYMBOLS
    if length < len(required):
        raise ValueError("Length is too short.")
    chars = required.copy()
    while len(chars) < length:
        chars.append(secrets.choice(available))
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)
# generate.py
# Secure password generator
import argparse
import secrets
import string
SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?"
def generate_password(length, upper, digits, symbols):
    required = []
    available = string.ascii_lowercase
```

## PDF page 61

```python
    if upper:
        required.append(
            secrets.choice(string.ascii_uppercase)
        )
        available += string.ascii_uppercase
    if digits:
        required.append(
            secrets.choice(string.digits)
        )
        available += string.digits
    if symbols:
        required.append(secrets.choice(SYMBOLS))
        available += SYMBOLS
    if length < len(required):
        raise ValueError("Length is too short.")
    chars = required.copy()
    while len(chars) < length:
        chars.append(secrets.choice(available))
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)
def main():
    parser = argparse.ArgumentParser(
        description="Secure password generator"
    )
    parser.add_argument(
        "-l", "--length",
        type=int,
        default=12
    )
    parser.add_argument(
        "-c", "--count",
        type=int,
        default=1
    )
    parser.add_argument(
        "--upper",
        action="store_true"
    )
    parser.add_argument(
        "--digits",
        action="store_true"
    )
    parser.add_argument(
        "--symbols",
        action="store_true"
    )
    parser.add_argument(
        "--save",
        help="Save passwords to a text file"
    )
    args = parser.parse_args()
    passwords = []
    for _ in range(args.count):
        passwords.append(
            generate_password(
```

## PDF page 62

```python
                args.length,
                args.upper,
                args.digits,
                args.symbols
            )
        )
    for password in passwords:
        print(password)
    if args.save:
        with open(args.save, "w") as file:
            for password in passwords:
                file.write(password + "\n")
        print("Passwords saved.")
if __name__ == "__main__":
    main()
# One basic 12-character lowercase password
python generate.py
# 16-character password with all character types
python generate.py --length 16 --upper --digits --symbols
# Five 20-character passwords saved to a file
python generate.py --length 20 --count 5 --upper --digits --symbols --save 
passwords.txt
# Built-in help message
python generate.py --help
```

## PDF page 66

```python
import hashlib
h1 = hashlib.sha256(b"hello world").hexdigest()
h2 = hashlib.sha256(b"hello world!").hexdigest() # one character added
print(h1)
# b94d27b9934d3e08a52e52d7da7dabfac484efe04294e576d...
print(h2)
# 7509e5bda0c762d2bac7f90d758b5b2263fa01ccbc542ab5...
# Read as text (only for text files you need to display):
with open("config.txt", "r") as f:
    content = f.read() # returns a string
    # Read as bytes (for hashing - always use this for FIM):
    with open("config.txt", "rb") as f:
        content = f.read() # returns bytes
```

## PDF page 67

```python
import hashlib
def hash_file(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        while True:
            chunk = f.read(65536) # 64 KB at a time
            if not chunk:
                break
sha256.update(chunk) # feed each chunk to the hasher
return sha256.hexdigest()
import json
baseline = {
"/etc/config.txt": "a4b2c3d4...",
"/usr/bin/app": "e5f6g7h8..."
}
# Save to file:
with open("baseline.json", "w") as f:
    json.dump(baseline, f, indent=2)
    # Load from file:
    with open("baseline.json", "r") as f:
        loaded = json.load(f)
```

## PDF page 68

```python
os.walk visits every folder and file in a directory tree. You give it a 
starting folder and it recursively descends through every subfolder.
import os
for root, dirs, files in os.walk("my_folder"):
    for filename in files:
        filepath = os.path.join(root, filename)
        print(filepath) # prints every file path in the tree
import hashlib
def hash_file(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b''):
sha256.update(chunk)
return sha256.hexdigest()
except Exception:
    return None
def build_baseline(target_dir):
    baseline = {}
    for root, _, files in os.walk(target_dir):
        for name in files:
            filepath = os.path.normpath(os.path.join(root, name))
            file_hash = hash_file(filepath)
            if file_hash:
baseline[filepath] = file_hash
return baseline
def compare_hashes(baseline, current):
```

## PDF page 69

```python
    alerts = []
    for path, old_hash in baseline.items():
        if path not in current:
alerts.append(f"DELETED: {path}")
elif current[path] != old_hash:
alerts.append(f"MODIFIED: {path}")
for path in current:
    if path not in baseline:
alerts.append(f"NEW FILE: {path}")
return alerts
# monitor.py
# File integrity monitor using SHA256 cryptographic hashing
import datetime
import hashlib
import json
import os
BASELINE_FILE = "baseline.json"
TARGET_DIR = "."  # monitor current directory; change as needed
def hash_file(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except OSError:
        return None
def scan_directory(directory):
    hashes = {}
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d != "venv"]
        for name in files:
            path = os.path.join(root, name)
            if name == BASELINE_FILE:
                continue
            file_hash = hash_file(path)
            if file_hash:
                hashes[path] = file_hash
    return hashes
def create_baseline():
```

## PDF page 70

```python
    baseline = scan_directory(TARGET_DIR)
    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=4)
    print(f"Baseline created with {len(baseline)} files.")
def check_integrity():
    if not os.path.exists(BASELINE_FILE):
        print("No baseline found. Create one first.")
        return
    with open(BASELINE_FILE, "r") as f:
        old = json.load(f)
    current = scan_directory(TARGET_DIR)
    old_files = set(old.keys())
    current_files = set(current.keys())
    added = current_files - old_files
    deleted = old_files - current_files
    common = old_files & current_files
    modified = [path for path in common if old[path] != current[path]]
    print(f"Integrity check: {datetime.datetime.now()}")
    for path in added:
        print(f"ADDED: {path}")
    for path in deleted:
        print(f"DELETED: {path}")
    for path in modified:
        print(f"MODIFIED: {path}")
    if not added and not deleted and not modified:
        print("No changes detected.")
choice = input("Create baseline or check integrity? (create/check): 
").lower().strip()
if choice == "create":
    create_baseline()
elif choice == "check":
    check_integrity()
else:
    print("Please choose create or check.")
python monitor.py
python monitor.py
```

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

## PDF page 83

```python
import socket
def check_subdomain(domain, word):
    subdomain = f"{word}.{domain}"
    try:
        ip = socket.gethostbyname(subdomain)
        return subdomain, ip
    except socket.gaierror:
        return None, None
result, ip = check_subdomain("example.com", "www")
if result:
    print(f"FOUND: {result} -> {ip}")
```

## PDF page 84

```python
from concurrent.futures import ThreadPoolExecutor
def check(word):
    return check_subdomain(domain, word) # defined above
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(check, wordlist)
        for subdomain, ip in results:
            if subdomain:
                print(f"FOUND: {subdomain} -> {ip}")
www
mail
ftp
api
dev
staging
test
admin
portal
vpn
remote
store
shop
blog
docs
support
```

## PDF page 85

```python
help
status
cdn
# subdomain_finder.py
# Multithreaded subdomain finder using DNS resolution
import datetime
import socket
from concurrent.futures import ThreadPoolExecutor
domain = input("Enter target domain (e.g. example.com): ").strip()
wordfile = input("Path to wordlist file: ").strip()
try:
    with open(wordfile, "r") as f:
        wordlist = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("Wordlist file not found.")
    raise SystemExit
found = []
def check_subdomain(name):
    subdomain = f"{name}.{domain}"
    try:
        ip = socket.gethostbyname(subdomain)
        return subdomain, ip
    except socket.gaierror:
        return None
with ThreadPoolExecutor(max_workers=20) as executor:
    results = executor.map(check_subdomain, wordlist)
    for result in results:
        if result:
            subdomain, ip = result
```

## PDF page 86

```python
            found.append((subdomain, ip))
            print(f"FOUND: {subdomain} -> {ip}")
report_name = f"subdomains_{domain}.txt"
with open(report_name, "w") as report:
    report.write(f"Subdomain report for {domain}\n")
    report.write(f"Generated: {datetime.datetime.now()}\n")
    report.write("=" * 50 + "\n")
    for subdomain, ip in found:
        report.write(f"{subdomain} -> {ip}\n")
print(f"Done. Found {len(found)} subdomains. Report saved as 
{report_name}")
```

## PDF page 91

```python
from scapy.all import sniff
def process_packet(packet):
    print(packet.summary())
    sniff(count=10, prn=process_packet, store=False)
```

## PDF page 92

```python
from scapy.all import IP, TCP, UDP, ICMP
def process_packet(packet):
    if packet.haslayer(IP):
        src = packet[IP].src # source IP
        dst = packet[IP].dst # destination IP
        if packet.haslayer(TCP):
            sport = packet[TCP].sport # source port
            dport = packet[TCP].dport # destination port
            if packet.haslayer(UDP):
                sport = packet[UDP].sport
                dport = packet[UDP].dport
```

## PDF page 93

```python
# sniffer.py
# Live packet sniffer with protocol labeling and capture file output
import datetime
from scapy.all import ICMP, IP, TCP, UDP, sniff
PORT_LABELS = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt",
}
COUNTS = {"TCP": 0, "UDP": 0, "ICMP": 0, "Other": 0}
LOGFILE = "capture.txt"
PACKET_MAX = 50
def label_port(port):
    return PORT_LABELS.get(port, "Unknown")
def handle_packet(packet):
    if IP not in packet:
        return
    src = packet[IP].src
    dst = packet[IP].dst
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if TCP in packet:
        proto = "TCP"
        sport = packet[TCP].sport
        dport = packet[TCP].dport
    elif UDP in packet:
        proto = "UDP"
        sport = packet[UDP].sport
        dport = packet[UDP].dport
    elif ICMP in packet:
        proto = "ICMP"
        sport = "-"
        dport = "-"
    else:
        proto = "Other"
        sport = "-"
        dport = "-"
    COUNTS[proto] += 1
```

## PDF page 94

```python
    service = label_port(dport) if isinstance(dport, int) else "-"
    line = f"{timestamp} {proto} {src}:{sport} -> {dst}:{dport} 
({service})"
    print(line)
    with open(LOGFILE, "a") as f:
        f.write(line + "\n")
print(f"Capturing {PACKET_MAX} packets. Press Ctrl+C to stop.")
sniff(prn=handle_packet, count=PACKET_MAX, store=False)
print("Summary:")
for proto, count in COUNTS.items():
    print(f"{proto}: {count}")
# Linux / Mac - requires sudo:
sudo python3 sniffer.py
# Windows - run Command Prompt as Administrator, then:
python sniffer.py
```

## PDF page 96

```python
tcp.port == 80 # all HTTP traffic
ip.addr == 192.168.1.5 # all traffic to or from this IP
http.request.method == 'POST' # only HTTP POST requests
tcp.flags.syn == 1 # TCP connection initiations
dns # all DNS traffic
```

## PDF page 100

```python
from urllib.parse import urljoin
base = 'https://example.com/app/'
relative = '../admin'
full = urljoin(base, relative)
print(full) # example.com/admin
# String concatenation would break this:
print(base + relative) # example.com/app/../admin (wrong)
import requests
url = "https://example.com"
```

## PDF page 101

```python
response = requests.get(url, timeout=10)
headers = response.headers
print(headers.get('Server', 'Not disclosed'))
print(headers.get('X-Powered-By', 'Not disclosed'))
REQUIRED_HEADERS = [
'Content-Security-Policy',
'X-Frame-Options',
'X-Content-Type-Options',
'Strict-Transport-Security',
]
def check_security_headers(response):
    findings = []
    for h in REQUIRED_HEADERS:
        if h not in response.headers:
findings.append(f"Missing: {h}")
return findings
def check_server_info(response):
    findings = []
    server = response.headers.get('Server', '')
    powered = response.headers.get('X-Powered-By', '')
    if server:
findings.append(f"Server header exposed: {server}")
if powered:
findings.append(f"X-Powered-By exposed: {powered}")
return findings
DIRECTORY_SIGNALS = [
'Index of /',
'Directory listing for',
'Parent Directory',
]
def check_directory_listing(response):
    findings = []
    text = response.text.lower()
    for signal in DIRECTORY_SIGNALS:
        if signal.lower() in text:
findings.append(f"Directory listing detected: '{signal}'")
break
return findings
SQL_ERROR_PATTERNS = [
'sql syntax',
'mysql_fetch',
'unclosed quotation mark',
'ORA-01756',
'syntax error',
]
def check_sql_errors(url, response):
    findings = []
    text = response.text.lower()
    for pattern in SQL_ERROR_PATTERNS:
        if pattern.lower() in text:
findings.append(f"SQL error pattern in response: '{pattern}'")
return findings
```

## PDF page 102

```python
# web_scanner.py
# Web vulnerability scanner - safe educational tool
import datetime
from urllib.parse import urljoin
import requests
REQUIRED_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
]
DIRECTORY_SIGNALS = ["Index of /", "Directory listing for", "Parent 
Directory"]
SQL_ERROR_PATTERNS = [
    "sql syntax",
    "mysql_fetch",
    "unclosed quotation",
    "ORA-01756",
    "syntax error",
]
def check_headers(response):
    findings = []
    for header in REQUIRED_HEADERS:
        if header not in response.headers:
            findings.append(f"Missing security header: {header}")
    if "Server" in response.headers:
        findings.append(f"Server header exposed: 
{response.headers['Server']}")
    return findings
def check_directory_listing(base_url):
    findings = []
    test_url = urljoin(base_url, "/")
    try:
        response = requests.get(test_url, timeout=5)
        body = response.text.lower()
        for signal in DIRECTORY_SIGNALS:
            if signal.lower() in body:
                findings.append(f"Possible directory listing at 
{test_url}")
                break
    except requests.RequestException as error:
        findings.append(f"Directory listing check failed: {error}")
    return findings
```

## PDF page 103

```python
def check_sql_errors(base_url):
    findings = []
    test_url = base_url.rstrip("/") + "/?id='"
    try:
        response = requests.get(test_url, timeout=5)
        body = response.text.lower()
        for pattern in SQL_ERROR_PATTERNS:
            if pattern.lower() in body:
                findings.append(f"Possible SQL error disclosure at 
{test_url}")
                break
    except requests.RequestException as error:
        findings.append(f"SQL error check failed: {error}")
    return findings
def scan(url):
    findings = []
    try:
        response = requests.get(url, timeout=5)
        findings.extend(check_headers(response))
        findings.extend(check_directory_listing(url))
        findings.extend(check_sql_errors(url))
    except requests.RequestException as error:
        findings.append(f"Request failed: {error}")
    return findings
target = input("Enter target URL: ").strip()
if not target.startswith(("http://", "https://")):
    target = "https://" + target
results = scan(target)
report_name = "web_scan_report.txt"
with open(report_name, "w") as report:
    report.write(f"Web scan report for {target}\n")
    report.write(f"Generated: {datetime.datetime.now()}\n")
    report.write("=" * 50 + "\n")
    if results:
        for finding in results:
            report.write(f"- {finding}\n")
    else:
        report.write("No findings detected.\n")
print(f"Scan complete. Report saved as {report_name}")
python web_scanner.py
# When prompted:
# Enter target domain: testphp.vulnweb.com
```

## PDF page 109

```python
# Mac (using Homebrew):
brew install pyenv
# Linux:
Visit pyenv.run and follow the official installation command shown there.
# After installation, set a local Python version for a project:
cd your_project
pyenv local 3.11.7
# Verify:
```

## PDF page 110

```python
python --version # Should show 3.11.7
Traceback (most recent call last):
File "scanner.py", line 12, in <module>
result = s.connect_ex((target, port))
NameError: name 's' is not defined
```

## PDF page 113

```python
# In a Flask web application:
from password_checker import check_password, get_verdict
@app.route('/register', methods=['POST'])
def register():
    password = request.form.get('password', '')
score, issues = check_password(password)
if score < 3:
    return jsonify({
'error': 'Password too weak',
'issues': issues
}), 400
# Continue with account creation...
```

## PDF page 124

```python
# Add to your analyzer: count 404s per IP
enumeration_count = defaultdict(int)
if code == '404':
enumeration_count[ip] += 1
# Alert if any IP generated more than 20 404s
ENUM_THRESHOLD = 20
enum_alerts = {ip: c for ip, c in enumeration_count.items()
if c >= ENUM_THRESHOLD}
```

## PDF page 131

```text
Finding name: Missing Strict-Transport-Security Header
Severity: LOW
Description:
The application does not include the HTTP Strict-Transport-Security
(HSTS) header in its responses. This allows browsers to access the
```

## PDF page 132

```text
Steps to Reproduce:
2. Observe the HTTP response headers in developer tools
3. Confirm Strict-Transport-Security is absent
Impact:
Without HSTS, users who navigate to the HTTP version of the
application are not automatically redirected to HTTPS, exposing
their session cookies and form inputs to network interception on
unencrypted connections.
Recommendation:
Add the following header to all HTTPS responses:
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

## PDF page 135

```text
git init
git add .
git commit -m "Initial commit: 10 Python security tools"
git remote add origin git@github.com:YOUR-USERNAME/python-security-
tools.git
git push -u origin main
```

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


# 06 File Integrity Monitor

Raw code, terminal commands, sample output, and monospaced templates extracted from the PDF text layer. Page wraps and teaching-snippet indentation are preserved as closely as possible. Use the cleaned scripts in `../tools/` for runnable versions.

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


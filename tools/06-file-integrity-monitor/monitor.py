# monitor.py
# File integrity monitor using SHA256 cryptographic hashing

import datetime
import hashlib
import json
import os

BASELINE_FILE = "baseline.json"
TARGET_DIR = os.path.dirname(os.path.abspath(__file__))
EXCLUDED_DIRS = {"venv", ".venv", ".git", "__pycache__"}


def hash_file(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as file:
            chunks = iter(
                lambda: file.read(65536), b""
            )
            for chunk in chunks:
                sha256.update(chunk)
        return sha256.hexdigest()
    except OSError:
        return None


def scan_directory(directory):
    hashes = {}

    for root, dirs, files in os.walk(directory):
        dirs[:] = [
            name
            for name in dirs
            if name not in EXCLUDED_DIRS
        ]

        for name in files:
            filepath = os.path.join(root, name)
            relative_path = os.path.relpath(filepath, directory)

            if relative_path == BASELINE_FILE:
                continue

            file_hash = hash_file(filepath)
            if file_hash:
                hashes[relative_path] = file_hash

    return hashes


def create_baseline():
    baseline = scan_directory(TARGET_DIR)
    baseline_path = os.path.join(TARGET_DIR, BASELINE_FILE)

    with open(baseline_path, "w", encoding="utf-8") as file:
        json.dump(baseline, file, indent=4, sort_keys=True)

    print(f"Baseline created with {len(baseline)} files.")


def check_integrity():
    baseline_path = os.path.join(TARGET_DIR, BASELINE_FILE)

    if not os.path.exists(baseline_path):
        print("No baseline found. Create one first.")
        return

    with open(baseline_path, "r", encoding="utf-8") as file:
        old = json.load(file)

    current = scan_directory(TARGET_DIR)
    old_files = set(old)
    current_files = set(current)

    added = sorted(current_files - old_files)
    deleted = sorted(old_files - current_files)
    modified = sorted(
        path
        for path in old_files & current_files
        if old[path] != current[path]
    )

    print(
        "Integrity check:",
        datetime.datetime.now().isoformat(timespec="seconds"),
    )

    for path in added:
        print(f"ADDED: {path}")
    for path in deleted:
        print(f"DELETED: {path}")
    for path in modified:
        print(f"MODIFIED: {path}")

    if not added and not deleted and not modified:
        print("No changes detected.")


def main():
    choice = input(
        "Create baseline or check integrity? (create/check): "
    ).lower().strip()

    if choice == "create":
        create_baseline()
    elif choice == "check":
        check_integrity()
    else:
        print("Please choose create or check.")


if __name__ == "__main__":
    main()

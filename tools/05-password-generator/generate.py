# generate.py
# Secure password generator

import argparse
import secrets
import string


SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?"


def generate_password(length, upper, digits, symbols):
    required = []
    available = string.ascii_lowercase

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

# generate.py
# Cryptographically secure password generator

import argparse
import secrets
import string

SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?"


def generate_password(length, upper, digits, symbols):
    if length < 1:
        raise ValueError("Length must be at least 1.")

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
        raise ValueError(
            f"Length must be at least {len(required)} "
            "for the selected character types."
        )

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
        "-l", "--length", type=int, default=16
    )
    parser.add_argument("-c", "--count", type=int, default=1)
    parser.add_argument(
        "--no-upper", action="store_true"
    )
    parser.add_argument(
        "--no-digits", action="store_true"
    )
    parser.add_argument(
        "--no-symbols", action="store_true"
    )
    parser.add_argument(
        "--save",
        help="Save passwords to a text file",
    )
    args = parser.parse_args()

    if args.count < 1:
        parser.error("Count must be at least 1.")

    try:
        passwords = [
            generate_password(
                args.length,
                not args.no_upper,
                not args.no_digits,
                not args.no_symbols,
            )
            for _ in range(args.count)
        ]
    except ValueError as error:
        parser.error(str(error))

    for password in passwords:
        print(password)

    if args.save:
        with open(args.save, "w", encoding="utf-8") as file:
            file.write("\n".join(passwords) + "\n")
        print(f"Passwords saved to {args.save}.")


if __name__ == "__main__":
    main()

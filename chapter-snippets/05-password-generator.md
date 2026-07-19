# 05 Password Generator

Raw code, terminal commands, sample output, and monospaced templates extracted from the PDF text layer. Page wraps and teaching-snippet indentation are preserved as closely as possible. Use the cleaned scripts in `../tools/` for runnable versions.

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


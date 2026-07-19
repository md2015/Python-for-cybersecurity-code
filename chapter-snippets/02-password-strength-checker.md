# 02 Password Strength Checker

Raw code, terminal commands, sample output, and monospaced templates extracted from the PDF text layer. Page wraps and teaching-snippet indentation are preserved as closely as possible. Use the cleaned scripts in `../tools/` for runnable versions.

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


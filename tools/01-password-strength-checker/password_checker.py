# password_checker.py
# Scores any password out of 5 and explains every weakness found


def check_password(password):
    score = 0
    issues = []

    if len(password) >= 8:
        score += 1
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

while True:
    password = input("Enter a password: ")

    if password.lower() == "quit":
        print("Goodbye.")
        break

    score, issues = check_password(password)
    print_results(score, issues)

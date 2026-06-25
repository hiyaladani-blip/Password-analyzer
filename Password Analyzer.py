import re

common_passwords = {
    "123456",
    "password",
    "123456789",
    "qwerty",
    "abc123",
    "admin",
    "welcome",
    "letmein",
    "password123",
    "123123"
}

def check_password_strength(password):
    score = 0
    suggestions = []

    # Check common passwords first
    if password.lower() in common_passwords:
        return (
            "Very Weak",
            ["This password is very common and can be guessed easily."]
        )

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Strength rating
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, suggestions


# Main Program
password = input("Enter your password: ")

strength, suggestions = check_password_strength(password)

print("\nPassword Strength:", strength)

if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("\nGreat! Your password meets all recommended criteria.")
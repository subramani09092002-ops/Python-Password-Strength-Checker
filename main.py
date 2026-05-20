password = input("Enter your password: ")

# Special characters list
special_chars = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"

# Check conditions
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in special_chars for char in password)

score = 0

# Length check
if len(password) >= 8:
    score += 1

# Other checks
if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1

# Display missing requirements
print("\nPassword Analysis:")

if not has_upper:
    print("- Add at least one uppercase letter")

if not has_lower:
    print("- Add at least one lowercase letter")

if not has_digit:
    print("- Add at least one number")

if not has_special:
    print("- Add at least one special character")

if len(password) < 8:
    print("- Password should be at least 8 characters long")

# Final strength result
print("\nPassword Strength:")

if len(password) == 0:
    print("No password entered")

elif score <= 2:
    print("Weak Password")

elif score <= 4:
    print("Medium Password")

else:
    print("Strong Password")
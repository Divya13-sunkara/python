password = input("Enter password: ")
has_digit = False

for ch in password:
    if ch.isdigit():
        has_digit = True

if has_digit:
    print("Password contains a digit")
else:
    print("Password must contain at least one digit")
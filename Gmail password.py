password = input("Enter your password: ")
l = len(password)

# List of special characters
special_chars = ['@', '#', '$', '%', '&', '!', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', ':', ';', '<', '>', '?', '/', '|', '\\', '^', '~']

# Check minimum length
if l < 8:
    print("invalid password")
else:
    digit = False
    upper = False
    lower = False
    special = False

    for i in password:
        if i.isdigit():
            digit = True
        elif i.isupper():
            upper = True
        elif i.islower():
            lower = True
        elif i in special_chars:  # Check if character is in the list
            special = True

    # Validate password conditions
    if digit and upper and lower and special:
        print("valid password")
    else:
        print("invalid password")

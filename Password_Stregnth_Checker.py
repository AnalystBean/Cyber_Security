import re

def password_checker(password):
    if len(password) < 8:
        return "Too short"
    elif re.search('[0-9]', password) is None:
        return "No numbers"
    elif re.search('[A-Z]', password) is None:
        return "No uppercase letters"
    elif re.search('[a-z]', password) is None:
        return "No lowercase letters"
    else:
        return "Strong password"

password = input("Enter your password: ")
result = password_checker(password)
print(result)
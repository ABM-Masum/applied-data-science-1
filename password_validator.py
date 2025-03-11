password = input("Your password:")

if "password" in password or "123456" in password:
    print("The password may not contain the keywords “password” or “123456”.")
elif password.startswith("qwerty"):
    print("The password may not start with the keyword “qwerty” but it may contain it.")
elif password.isalpha():
    print("The password must contain at least one non-alphabetic character.")
elif password.isdigit():
    print("The password must contain at least one non-digit character.")
elif "$" not in password and "@" not in password and "!" not in password:
    print("The password must contain at least one of the following special characters: $, @ or !.")
elif password.isupper() or password.islower():
    print("The password must have both uppercase and lowercase letters.")
else:
    print("The password is valid!")

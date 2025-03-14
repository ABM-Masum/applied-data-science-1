maximum = None
minimum = None

while True:
    user_input = input("Input: ")

    if user_input.isdigit():
        number = int(user_input)

        if maximum is None or number > maximum:
            maximum = number

        if minimum is None or number < minimum:
            minimum = number
    else:
        if maximum is None:
            print("No integer given.")
        break

print("Maximum:", maximum)
print("Minimum:", minimum)
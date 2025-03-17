def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":

    user_input = input("Non-negative integer: ")

    if user_input.isdigit():
        user_input = int(user_input)
        print(factorial(user_input))
    else:
        print("Please input.")
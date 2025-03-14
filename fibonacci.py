def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b


if __name__ == "__main__":
    user_input = input("Number of Fibonacci Sequence numbers: ")

    if user_input.isdigit():
        n = int(user_input)
        fibonacci(n)
    else:
        print("Please input a non-negative integer.")

    pass

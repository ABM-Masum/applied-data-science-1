def factorial(n):
    i = 1
    for x in range(1,n+1):
        i *= x

    return i

if __name__ == "__main__":

    n =input("Non-negative integer: ")

    if n.isdigit():

        n = int(n)

        print(factorial(n))

    else:
        print("Please input a non-negative integer.")
pass
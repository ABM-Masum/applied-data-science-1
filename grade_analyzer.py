def inputted_numbers():
    numbers = []
    while True:
        user_input = input("Input: ")

        if user_input.isdigit():
            numbers.append(int(user_input))
        else:
            break
    if not numbers:
        print("No Integer given.")
    return numbers

# Manual implementation of min and max functions

# def minimum(numbers):
#     min_num = None
#     for number in numbers:
#         if min_num is None or number < min_num:
#             min_num = number
#     return min_num
#
# def maximum(numbers):
#     max_num = None
#     for number in numbers:
#         if max_num is None or number > max_num:
#             max_num = number
#     return max_num

def average(numbers):
    # cal = 0
    # for number in numbers:
    #     cal += number
    # average_num = cal/len(numbers)
    # return average_num
    return sum(numbers) / len(numbers)

def standard_deviation(numbers):
    avg = average(numbers)
    summation = 0
    for number in numbers:
        summation += (number - avg) ** 2
    return (summation / len(numbers)) ** 0.5

def main():
    numbers = inputted_numbers()
    if numbers:
        min_num = min(numbers)
        max_num = max(numbers)
        avg_num = average(numbers)
        std_dev = standard_deviation(numbers)

        print("Minimum:", min_num)
        print("Maximum:", max_num)
        print("Average:", avg_num)
        print("SD:", std_dev)

if __name__ == '__main__':
    main()

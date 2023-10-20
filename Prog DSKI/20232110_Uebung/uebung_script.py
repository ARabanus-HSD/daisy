my_numbers = [2, -1, 56, 2, 7, -1, 4]

def low_plus_high(numbers):
    numbers.sort()
    return numbers[0] + numbers[-1]

print(low_plus_high(my_numbers))
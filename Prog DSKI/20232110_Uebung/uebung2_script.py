# Q1: b)

# C1

def war_of_numbers(numbers):
    """
    Sums the odd and even values in numbers and prints if Odds or
    Evens win (have higher sum), and also by which margin.
    Example:
    war_of_summer([4, 5, 6, 9]) => Odd numbers win by margin of 4!
    Args:
    -----
    numbers: list
    List of integers.
    """
    
    def is_even(number: int or float) -> bool:
        """returns True for even, False for odd
        """
        return number % 2== 0
    
    # even and odd starting values
    sum_even = 0
    sum_odd = 0
    
    for i in numbers:
        # add number to either even or odd sum
        if is_even(i):
            sum_even = sum_even + i
        else:
            sum_odd = sum_odd + i
    
    delta = abs(sum_even - sum_odd)
    
    if delta > 0:
        result = "Even numbers "
    elif delta < 0:
        result = "Odd numbers "
    else:
        result = "Nobody"
    
    final_statement = f"{result} wins by a delta of {delta}" 
    print(final_statement)
    return sum_even, sum_odd, final_statement
        

war_of_numbers([4, 5, 6, 9]) # => Odd numbers win by margin of 4!
war_of_numbers([4, 5, 6, 9, 10]) # => Even numbers win by margin of 6!
war_of_numbers([3, 3, 4, 2]) # => The sums are equal: There is no winne

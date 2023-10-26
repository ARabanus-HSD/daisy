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
    def is_even(number):
        if (number % 2) == 0:
            # print(f"{number} is EVEN!")
            return True
        elif (number %2) == 1:
            # print(f"{number} is ODD")
            return False

    even_or_odd_numbers = list(map(is_even, numbers))
    print(even_or_odd_numbers)
    
    if even_or_odd_numbers == True:
        even_sum = 
    
      
    
    # final_statement = f"{winner} wins by a margin of {winner_margin}"
    #return even_sum, odd_sum # final_statement

war_of_numbers([1, 2, 3, 4])
# # ------------ PT 1 ------------ 

# def low_plus_high(numbers: list) -> int:
#     '''
#     Hier ist ne nice erklärung für die Funktion!
#     :param numbers: list
#     :return: sum of low and high
#     '''
#     numbers.sort()
#     return numbers[0] + numbers[-1]

# # ------------ PT 2 ------------ 

# def low_plus_high(numbers: list, min: int=0) -> int:
    # '''
    # Es soll ein Mindestwert mit default-Wert gesetzt gegeben und gesetzt werden
    # Ist der kleinste Wert in der Liste kleiner als der Mindestwert, wird der Mindeswert benutzt
    # :param numbers: list
    # :param min: int
    # :return: sum of (min or low) + high
    # '''
    # numbers.sort()
    # if min >= numbers[0]:
        # return numbers[-1] + min
    # else:
        # return numbers[-1] + numbers[0]

# ------------ PT 2 ------------ 

def low_plus_high(numbers: list) -> int:
    '''
    Es soll ein Mindestwert mit default-Wert gesetzt gegeben und gesetzt werden
    Ist der kleinste Wert in der Liste kleiner als der Mindestwert, wird der Mindeswert benutzt
    :param numbers: list
    :param min: int
    :return: sum of (min or low) + high
    '''
    numbers.sort()
    def set_to_min(value: int=numbers[0],min: int=0) -> int:
        """
        Overkill function to return either lowest value in list or min value given
        :param value: int lowest in list
        :param min: int low threshold
        """
        if value < min:
            value = min           
        return value
    summe = set_to_min() + numbers[-1]
    return summe

my_numbers = [2, -1, 15, 2, 7, -1, 4]
print(low_plus_high(my_numbers))

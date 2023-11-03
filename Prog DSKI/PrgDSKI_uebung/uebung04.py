# C1
def caesar_encode(text, shift, alphabet="abcdefghijklmnopqrstuvwxyz"):
    """
    This is a Caesar cipher.
     Each letter in a message is shifted by *shift*
    characters in the alphabet, and returned.
    text:
    A string you would like to encode or decode.
     Must consist of
    lowercase letters and spaces.
    shift:
    An integer, indicating how many positions in the alphabet each
    letter in the text will be shifted.
    alphabet:
    A string with all characters that should be shifted.
    """
    # make a dictionary with letters a-z corresponding to 0-25 and vice versa
    dict_alphabet_to_index = {}
    dict_index_to_alphabet = {}
    for index, letter in enumerate(alphabet):
        dict_alphabet_to_index.__setitem__(letter, index)     
    # print(dict_alphabet_to_index)
    for index, letter in enumerate(alphabet):
        dict_index_to_alphabet.__setitem__(index, letter)     
    # print(dict_index_to_alphabet)
    
    # go though input string, make a list with numbers 0-25 for each letter
    input_string_to_numbers = [dict_alphabet_to_index[letter] for letter in text if letter in dict_alphabet_to_index]
    # print(input_string_to_numbers)
    
    # add shift offset using modulo
    for i in range(len(input_string_to_numbers)):
        input_string_to_numbers[i] = (input_string_to_numbers[i] + shift) % 26
    # print(input_string_to_numbers)
    
    # make a new string from number list
    encoded_string_list = [dict_index_to_alphabet[index] for index in input_string_to_numbers if index in dict_index_to_alphabet]
    encoded_string = ''.join(encoded_string_list)

    # add special characters back into the string!
    
    
    return encoded_string

print(caesar_encode("mein text!", shift=15)) # -> btxc itmi!
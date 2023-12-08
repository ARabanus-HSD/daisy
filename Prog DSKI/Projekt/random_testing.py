import numpy as np
import random

def keep_cross(input_array, n_row, n_col):
    """
    - makes a mask filled with zeros, except for chosen n_row and n_col
    - multiplies mask with input array 

    Args:
        input_array (_type_): numpy array
        n_row (_type_): starts with 0!
        n_col (_type_): starts with 0!
    """
    
    mask = np.ones((input_array.shape[0], input_array.shape[1]), dtype=float)
    row_and_col = [n_row, n_col]
    for i in row_and_col:
        mask[:, i] = 0
        mask[i, :] = 0
        
    output_array = input_array * mask
    
    return output_array

def search_horizontal(array, k):
    # go through rows in array
    # if there is a k-long line of 0s:
        # palce marker at either left or right most (random)
    pass

def search_vertical(array, k):
    
    pass

def search_diagonal(array, k):
    # go
    pass

def make_move(arr):
    print(arr)
    if not np.any(arr):
        move = (random.randint(board.shape))
    else:
        print("something else")
    pass

arr = np.zeros((6, 7), dtype=int)

pattern_arr = keep_cross(arr, 3, 4)

make_move(arr)
make_move(pattern_arr)
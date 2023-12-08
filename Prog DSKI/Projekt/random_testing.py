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
    
    mask = np.zeros((input_array.shape[0], input_array.shape[1]), dtype=float)
    row_and_col = [n_row, n_col]
    for i in row_and_col:
        mask[:, i] = 1
        mask[i, :] = 1
        
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


arr = np.ones((6, 7), dtype=int)

pattern_arr = keep_cross(arr, 3, 4)

def search_horizontal():

    pass

def search_vertical():
    
    pass

def search_diagonal():
    
    pass
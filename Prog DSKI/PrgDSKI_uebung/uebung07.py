import numpy as np

# A1
def square_array(size):
    if size < 2:
        raise ValueError("array size must be >= 2")
    else:
        # make n x n matrix filled with zeros
        array = np.matrix(np.zeros((size, size), dtype=float))
        first_and_last = [0, -1]
        for i in first_and_last:
            array[:, i] = 1
            array[i, :] = 1
        return array

# A2
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
        
        
# Anwendung
# A1
# print(square_array(8))

# A2
my_array = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12],
                     [13, 14, 15, 16]])

print(keep_cross(my_array, 2, 2))
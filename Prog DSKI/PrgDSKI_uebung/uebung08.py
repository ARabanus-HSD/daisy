import numpy as np
# import random

# A1
def random129(n_row, n_col):
    random_numbers = [1, 2, 9]
    array = np.random.choice((random_numbers), (n_row, n_col))
    return array

# A2
def brownian_motion(n, num_time_steps):
    """Simple Brownian motion simulation.
    """
    # Start with n particles (startposition inside square)
    # Shape (n, 2) --> n particles with coordinates x, y
    particles = np.sqrt(n) * (np.random.random((n, 2)) - 0.5)
    # Simulate movement over num_time_steps
    pass    

# A1
print(random129(5, 10))
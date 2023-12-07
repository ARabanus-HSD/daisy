import numpy as np
import math

# import random

# A1
def random129(n_row, n_col):
    random_numbers = [1, 2, 9]
    array = np.random.choice((random_numbers), (n_row, n_col))
    return array

# A2
def brownian_motion(n, num_time_step=0):
    """Simple Brownian motion simulation.
    """
    def euklidische_norm(vector):
        """
        """
        squared_sum = sum(x ** 2 for x in vector)
        result = math.sqrt(squared_sum)
        return result
        
    # Start with n particles (startposition inside square)
    # Shape (n, 2) --> n particles with coordinates x, y
    particles = np.sqrt(n) * (np.random.random((n, 2)) - 0.5)

    # 3rd dim in particles_over_time is time:
    particles_over_time = np.zeros((particles.shape[0], particles.shape[1], num_time_step))

    for i in range(num_time_step):
        x = 2 * np.random.random() - 1
        y = 2 * np.random.random() - 1
        particles[:, 0] += x
        particles[:, 1] += y

        particles_over_time[:, :, i] = particles.copy()
        # print(f"iterations num {i}: ", particles)
    return particles_over_time

# A1
# print(random129(5, 10))

# A2
print(brownian_motion(1, 25))
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as plt_patches

# A1
def random129(n_row, n_col):
    random_numbers = [1, 2, 9]
    array = np.random.choice((random_numbers), (n_row, n_col))
    return array

# A2
def improvised_liveplot(particles, num_time_step, delta):
    
    # mean for x and y
    mean_x = np.mean(particles.T[0])
    mean_y = np.mean(particles.T[1])

    max_distance = max(np.linalg.norm(particles, axis=1))
    max_delta = np.amax(np.absolute(delta.T)) 
    min_delta = np.amin(np.absolute(delta.T))   
    mean_delta = np.mean(np.absolute(delta.T))

    # plt.plt()
    plt.scatter(particles.T[0], particles.T[1], marker='o')
    plt.scatter(mean_x, mean_y, marker="+", s=500)
    plt_patches.Circle((0, 0), radius=max_distance, linewidth=20)
    circle = plt_patches.Circle((0, 0), radius=max_distance, edgecolor='b', facecolor='none', linewidth=0.5)


    #    Add the circle to the current axis
    plt.gca().add_patch(circle)

    # Set labels and title
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.title(f'Scatter Plot after {num_time_step} iterations\napprox largest distance from origin: {round(max_distance, 3)}\nmax, min, mean change in position {round(max_delta,3), round(min_delta,3), round(mean_delta,3)}')
    plt.legend()
    # Show the colorbar to represent time
    plt.axis([-10, 10, -10, 10]) 
    plt.gca().set_aspect('equal', adjustable='box')

    # print(f"iterations num {i}: ", particles)
    plt.show()
    plt.close()

def brownian_motion(n, num_time_step=0):
    """Simple Brownian motion simulation.
    """
    
    # Start with n particles (startposition inside square)
    # Shape (n, 2) --> n particles with coordinates x, y
    particles = np.sqrt(n) * (np.random.random((n, 2)) - 0.5)

    for i in range(num_time_step):
        particles_next_iter = particles + 2 * np.random.random((n, 2)) - 1
        delta = particles - particles_next_iter

        improvised_liveplot(particles_next_iter, i, delta)
        particles = particles_next_iter

    return particles


# A1
print(random129(5, 10))

# A2
num_time_step = 15
motion = brownian_motion(15, num_time_step)

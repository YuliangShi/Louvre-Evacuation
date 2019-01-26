import numpy as np


def get_density(individual, surrounders): #p/m^2
    density = surrounders
    return density


def get_velocity(density, max_v=1.34, gamma=1.913, max_d=5.4):
    if 0 <= density < max_d:
        velocity = max_v * (1 - np.exp(-gamma * ((1/density) - (1/max_d))))
    elif density >= max_d:
        velocity = 0
    return velocity

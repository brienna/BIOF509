"""Module to calculate best path between multiple points, using simulated annealing algorithm

Functions:
distance -- cost function that calculates distance as the cost of a path
new_path -- path altering function that creates a new path
new_path_modified -- same as new_path but slightly modified
simulated_annealing_optimizer -- objective function that implements the simulated annealing algorithm
"""

import random
import numpy as np


def distance(coords):
    """Calculate the distance of a path between multiple points

    Arguments received:
    coords — list of coordinates, e.g. [(0,0), (10, 5), (10, 10)], representing a path

    Arguments returned:
    distance -- total distance as a float
    """
    distance = 0
    for p1, p2 in zip(coords[:-1], coords[1:]):
        distance += ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    return distance


def new_path(existing_path):
    """Switch two random consecutive points on a path

    Arguments received:
    existing_path -- list of coordinates representing a path

    Arguments returned:
    path -- list of coordinates representing the mutated path
    """
    path = existing_path[:]
    point = random.randint(0, len(path)-2)  # randomly choose a point between 1st and 2nd-to-last points on path
    path[point+1], path[point] = path[point], path[point+1]  # switch this point with the next point
    return path

# Our simulated annealing function generated a reasonable solution but there were signs that the approach was
# limited by our function for creating new paths. Create a new function to generate paths in a different way.
# Does this improve the performance of the simulated annealing function? Answer in workspace.py, along with timer.


def new_path_modified(existing_path):
    """Switch two random points on a path

    Arguments received:
    existing_path -- list of coordinates representing a path

    Arguments returned:
    path -- list of coordinates representing the mutated path
    """
    path = existing_path[:]
    point = random.randint(0, len(path)-1)  # randomly choose any point on path
    point2 = random.randint(0, len(path)-1)  # randomly choose any other point on path
    while point2 == point:
        point2 = random.randint(0, len(path)-1)
    temp = path[point]  # temporary placeholder for 1st point
    path[point], path[point2] = path[point2], temp  # switch 1st point with 2nd point
    return path


def simulated_annealing_optimizer(starting_path, cost_func, new_path_func, start_temp, min_temp, steps):
    """Calculate the best path between multiple points using a simulated annealing algorithm

    The simulated annealing algorithm begins with a given path and calculates its cost.
    Each iteration generates a new path with two random consecutive points switched.
    If the new path has a lower cost, it is better and will replace the current path.
    If it has a higher cost, it is a worse path and may replace the current path, as
    decided by comparing a random number with an acceptance probability that depends on
    the temperature. The temperature decreases a bit in each iteration, giving worse paths
    a lesser chance of replacing the current path. Allowing worse paths at the beginning
    helps to avoid converging to a local minimum rather than the global minimum.

    Arugments received:
    starting_path -- list of coordinates representing a path
    cost_func -- function to calculate cost of a path
    new_path_func -- function to generate a new path with two random consecutive points switched
    start_temp -- maximum temperature
    min_temp -- minimum temperature
    steps -- number of iterations

    Arguments returned:
    current_path -- list of coordinates representing the best path
    current_cost -- cost of the best path
    history -- an array of objects, each object containing information about each tested path
    """
    current_path = starting_path[:]
    current_cost = cost_func(current_path)
    temp_factor = -np.log(start_temp / min_temp)
    history = []
    for s in range(0, steps):
        temp = start_temp * np.exp(temp_factor * s / steps)
        new_path = new_path_func(current_path)
        new_cost = cost_func(new_path)
        if (new_cost < current_cost) or (random.random() <= np.exp(-(new_cost - current_cost)/temp)):
            current_path = new_path
            current_cost = new_cost
        record = {'step': s, 'temperature': temp, 'current_cost': current_cost, }
        history.append(record)
    return (current_path, current_cost, history)

"""Module to calculate best path between multiple points, using genetic algorithm

Functions:
new_path -- path altering function that creates a new path
distance -- cost function that calculates distance as the cost of a path
select_best -- function that selects the best paths in a population
recombine -- path altering function that returns a child path recombined from two parent paths
genetic_algorithm_optimizer -- objective function that implements the genetic algorithm
"""

import random


def new_path(existing_path):
    """Switch two random consecutive points on a path

    Arguments received:
    existing_path -- list of coordinates, e.g. [(0, 0), (10, 5), (10, 10)], representing a path

    Arguments returned:
    path -- list of coordinates representing the mutated path
    """
    path = existing_path[:]
    point = random.randint(0, len(path)-2)  # randomly choose a point between 1st and 2nd-to-last points on path
    path[point+1], path[point] = path[point], path[point+1]  # switch this point with the next point
    return path


def distance(coords):
    """Calculate the distance of a path between multiple points

    Arguments received:
    coords — list of coordinates representing a path

    Arguments returned:
    distance -- total distance as a float
    """
    distance = 0
    for p1, p2 in zip(coords[:-1], coords[1:]):
        distance += ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    return distance


def select_best(population, cost_func, num_to_keep):
    """Select a given number of paths with the lowest cost (the best paths)

    Arguments received:
    population -- an array of lists of coordinates representing paths
    cost_func -- function to calculate cost of a path
    num_to_keep -- number of paths to select

    Arguments returned:
    [i[0] for i in scored_population[:num_to_keep]] -- an array of lists of coordinates representing the best paths
    """
    scored_population = [(i, cost_func(i)) for i in population]  # create a list of tuples: (path, cost)
    scored_population.sort(key=lambda x: x[1])  # sort list by cost, lowest to highest
    return [i[0] for i in scored_population[:num_to_keep]]  # return num_to_keep paths with the lowest cost


def recombine(population):
    """Cross over two parent paths and return the resulting child path

    Arguments received:
    population -- an array of lists of coordinates representing paths

    Arguments returned:
    child -- list of coordinates representing a recombined child path
    """
    # Randomly choose two parents
    options = list(range(len(population)))  # from 1 to 125
    random.shuffle(options)
    partner1 = options[0]
    partner2 = options[1]
    # Choose a split point, take the first parent's order to that split point,
    # then the second parent's order for all remaining points
    split_point = random.randint(0, len(population[0])-1)
    child = population[partner1][:split_point]
    for point in population[partner2]:
        if point not in child:
            child.append(point)
    return child


# Our genetic algorithm function currently only uses recombination. As we saw from the simulated
# annealing approach mutation is also a powerful tool in locating the optimal solution.
# Add mutation to the genetic algorithm function using the new_path function we created.

def genetic_algorithm_optimizer(starting_path, cost_func, new_path_func, pop_size, generations):
    """Calculate the best path between multiple points using a genetic algorithm

    The genetic algorithm begins with a given path, which it shuffles to create a starting population of a given
    size. Once the population is generated, the cost of each path is evaluated. The top 25 percent then are sent
    through recombination, then mutation -- to hopefully generate 'better' paths -- to form a new population.

    Arugments received:
    starting_path -- list of coordinates representing a path
    cost_func -- function to calculate cost of a path
    new_path_func -- function to generate a new path with two random consecutive points switched
    pop_size -- population size, or amount of paths in one generation
    generations -- number of iterations

    Arguments returned:
    population[0] -- list of coordinates representing the best path
    cost_func(population[0]) -- cost of the best path
    history -- an array of objects, each object containing information about each tested path
    """
    # Create a starting population of 500 paths by randomly shuffling the points
    population = []
    for i in range(pop_size):
        new_path = starting_path[:]
        random.shuffle(new_path)
        population.append(new_path)
    history = []
    # Take the top 25% of routes and recombine to create new routes, repeating for generations
    for i in range(generations):
        pop_best = select_best(population, cost_func, int(pop_size / 4))
        new_population = []
        mutated_population = []
        for i in range(pop_size):
            new_population.append(recombine(pop_best))
            if (random.random() <= 1/len(new_population[i])):  # mutation probability, 1/path length
                mutated_population.append(new_path_func(new_population[i]))  # mutate
            else:
                mutated_population.append(new_population[i])  # don't mutate
        population = mutated_population
        record = {'generation': i, 'current_cost': cost_func(population[0]), }
        history.append(record)
    return (population[0], cost_func(population[0]), history)

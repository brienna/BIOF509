"""Module to find the shortest path connecting a set of points
    
    find_best_route accepts a set of coordinates and will return the shortest
    route."""
import itertools


def distance(coords):
    """Calculates the distance of a path between multiple points
    
    Arguments:
    coords -- List of coordinates, e.g. [(0,0), (1,1)]
    
    Returns: Total distance as a float
    """
    distance = 0
    for p1, p2 in zip(coords[:-1], coords[1:]):
        distance += ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    return distance


def find_best_route(coords):
    """Find the shortest path between a set of points
    
    Arguments:
    coords -- List of coordinates, e.g. [(0,0), (1,1)]
    
    Returns: Tuple of shortest distance and the route
    """
    best_distance = distance(coords)
    best = coords
    for option in itertools.permutations(coords, len(coords)):
        option_distance = distance(option)
        if option_distance < best_distance:
            best = option
            best_distance = option_distance
    return (best_distance, best)

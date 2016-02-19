import itertools


def distance(coords):
    distance = 0
    for p1, p2 in zip(coords[:-1], coords[1:]):
        distance += ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    return distance


def find_best_route(coords):
    best_distance = distance(coords)
    best = coords
    for option in itertools.permutations(coords, len(coords)):
        option_distance = distance(option)
        if option_distance < best_distance:
            best = option
            best_distance = option_distance
    return (best_distance, best)


import timeit
import matplotlib.pyplot as plt
from simulated_annealing_optimizer import distance, new_path, new_path_modified, simulated_annealing_optimizer
from genetic_algorithm_optimizer import new_path, distance, genetic_algorithm_optimizer, recombine, select_best


coords = [(0,0), (10,5), (10,10), (5,10), (3,3), (3,7), (12,3), (10,11)]

###################################
#  simulated annealing algorithm  #
###################################
best_path, best_cost, history = simulated_annealing_optimizer(coords, distance, new_path_modified, 1000, 0.01, 1000)
print('simulated annealing algorithm best cost: ', best_cost)

## plot cost for each path tested with simulated annealing algorithm
plt.plot([i['current_cost'] for i in history])
plt.show()

# plot coordinates of best path calculated with simulated annealing algorithm
plt.plot([i[0] for i in best_path], [i[1] for i in best_path])
plt.show()


# test to determine if new_path_modified improves performance of simulated annealing algorithm
# there is not a significant difference, new_path_modified may even be worse
def wrapper(func, *args, **kwargs):
	def wrapped():
		return func(*args, **kwargs)
	return wrapped

new_path_modified_test = wrapper(simulated_annealing_optimizer, coords, distance, new_path_modified, 1000, 0.01, 1000)
new_path_test = wrapper(simulated_annealing_optimizer, coords, distance, new_path, 1000, 0.01, 1000)

time_npm = timeit.timeit(new_path_modified_test, number = 100)
time_np = timeit.timeit(new_path_test, number = 100)
print('new_path_modified time: ', time_npm)
print('new_path time: ', time_np)


#######################
#  genetic algorithm  #
#######################
best_path, best_cost, history = genetic_algorithm_optimizer(coords, distance, new_path, 500, 100)
print('genetic algorithm best cost: ', best_cost)

# plot cost for each path tested with genetic algorithm
plt.plot([i['current_cost'] for i in history])
plt.show()

# plot coordinates of best path calculated with genetic algorithm
plt.plot([i[0] for i in best_path], [i[1] for i in best_path])
plt.show()


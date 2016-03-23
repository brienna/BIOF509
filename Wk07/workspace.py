import matplotlib.pyplot as plt
from model_and_algorithms import Model, RCT, EpsilonGreedy, EpsilonDecrease


# plot RCT algorithm
model = Model(RCT, {'n_arms': 2, 'epsilon':0.05}, weights=[0.1, 0.2])
model.repeat_simulation()

fig, axes = plt.subplots(1,3, figsize=(18,6))
plt.suptitle("Performance of RCT and EpsilonGreedy algorithms", fontsize=20)

model.plot_arm_frequency(ax=axes[0])
model.plot_reward(ax=axes[1])
model.plot_cumulative_reward(ax=axes[2])


# plot EpsilonGreedy algorithm on same plots as RCT algorithm
model = Model(EpsilonGreedy, {'n_arms': 2, 'epsilon':0.05}, weights=[0.1, 0.2])
model.repeat_simulation()

model.plot_arm_frequency(ax=axes[0], colour='red')
model.plot_reward(ax=axes[1], colour='red')
model.plot_cumulative_reward(ax=axes[2], colour='red')




# plot different Epsilon values
fig, axes = plt.subplots(1, 3, figsize=(18,6))
plt.suptitle("Performance of EpsilonGreedy algorithm with different epsilon values", fontsize=20)

colors = ['red', 'orange', 'yellow', 'blue', 'purple', 'black']
epsilon_values = [1, 0.9, 0.6, 0.4, 0.2, 0.01]
for color, value in zip(colors, epsilon_values):
	model = Model(EpsilonGreedy, {'n_arms': 2, 'epsilon':value}, weights=[0.1, 0.2])
	model.repeat_simulation()
	model.plot_arm_frequency(ax=axes[0], colour=color)
	model.plot_reward(ax=axes[1], colour=color)
	model.plot_cumulative_reward(ax=axes[2], colour=color)




# plot EpsilonDecrease algorithm
fig, axes = plt.subplots(1, 3, figsize=(18,6))
plt.suptitle("Performance of EpsilonGreedy algorithm, reducing epsilon value over time", fontsize=20)

model = Model(EpsilonDecrease, {'n_arms': 2, 'epsilon':1}, weights=[0.1, 0.2])
model.repeat_simulation()

model.plot_arm_frequency(ax=axes[0])
model.plot_reward(ax=axes[1])
model.plot_cumulative_reward(ax=axes[2])

plt.show()





import matplotlib.pyplot as plt
from model_and_algorithms import Model, RCT, EpsilonGreedy


# plot RCT algorithm
model = Model(RCT, {'n_arms': 2, 'epsilon':0.05}, weights=[0.1, 0.2])
model.repeat_simulation()

fig, axes = plt.subplots(1,3, figsize=(18,6))
model.plot_arm_frequency(ax=axes[0])
model.plot_reward(ax=axes[1])
model.plot_cumulative_reward(ax=axes[2])




# plot EpsilonGreedy algorithm
model = Model(EpsilonGreedy, {'n_arms': 2, 'epsilon':0.05}, weights=[0.1, 0.2])
model.repeat_simulation()

model.plot_arm_frequency(ax=axes[0], colour='red')
model.plot_reward(ax=axes[1], colour='red')
model.plot_cumulative_reward(ax=axes[2], colour='red')

plt.show()
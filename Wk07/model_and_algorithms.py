import numpy as np

class Model(object):
    def __init__(self, algo, algo_kwargs, weights=[0.1, 0.1], size=100, repeats=200):
        self.algo = algo
        self.algo_kwargs = algo_kwargs
        self.weights = weights
        self.size = size
        self.repeats = repeats
        
    def run_simulation(self):
        """Run a single simulation, recording the performance"""
        algo = self.algo(**self.algo_kwargs)
        arm_choice_record = []
        reward_record = []
        for i in range(self.size):
            arm = algo.choose_arm()
            arm_choice_record.append(arm)
            reward = np.random.random() < self.weights[arm]
            reward_record.append(reward)
            algo.update(arm, reward)
        return arm_choice_record, reward_record
    
    def repeat_simulation(self):
        """Run multiple simulations, recording the performance of each"""
        arm_choice = []
        reward = []
        for i in range(self.repeats):
            arm_choice_record, reward_record = self.run_simulation()
            arm_choice.append(arm_choice_record)
            reward.append(reward_record)
        self.arm_choice = np.array(arm_choice)
        self.reward = np.array(reward)
        
    def plot_arm_frequency(self, ax, colour='black'):
        """Plot the frequency with which the second arm is chosen
        NOTE: Currently only works for two arms"""
        ax.plot(self.arm_choice.mean(axis=0), 'k.', color=colour)
        ax.set_title('Frequency of arm choice')
        ax.set_xlabel('Trial')
        ax.set_ylabel('Frequency')
        return ax
    
    def plot_reward(self, ax, colour='black'):
        """Plot the average reward for each trial across all simulations"""
        ax.plot(self.reward.mean(axis=0), 'k.', color=colour)
        ax.set_title('Reward')
        ax.set_xlabel('Trial')
        ax.set_ylabel('Reward')
        return ax
    
    def plot_cumulative_reward(self, ax, colour='black'):
        """Plot the cumulative reward across all simulations"""
        ax.plot(np.cumsum(self.reward, axis=1).mean(axis=0), 'k.', color=colour)
        ax.set_title('Cumulative Reward')
        ax.set_xlabel('Trial')
        ax.set_ylabel('Cumulative Reward')
        return ax


class RCT(object):
    def __init__(self, n_arms, epsilon):
        self._epsilon = epsilon
        self.counts = [0] * n_arms
        self.values = [0] * n_arms
        self.n_arms = n_arms
    
    def choose_arm(self):
        """Choose an arm"""
        if np.random.random() > self.epsilon:
            weights = np.array(self.values)
            weights = weights == weights.max()
            weights = weights / weights.sum()
            return np.random.choice(np.arange(self.n_arms), p=weights)
        else:
            return np.random.randint(self.n_arms)
        
    
    def update(self, arm, reward):
        """Update an arm with the reward"""
        self.counts[arm] = self.counts[arm] + 1
        n = self.counts[arm]
        value = self.values[arm]
        # Running product
        self.values[arm] = ((n - 1) / n) * self.values[arm] + (1/n) * reward
    
    @property
    def epsilon(self):
        if sum(self.counts) < 100:
            return 1
        else:
            return 0


class EpsilonGreedy(RCT):
    
    @property
    def epsilon(self):
        return self._epsilon



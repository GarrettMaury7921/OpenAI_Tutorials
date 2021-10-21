import math
import random
import time
from typing import Tuple
import numpy as np
from sklearn.preprocessing import KBinsDiscretizer

# import gym
import gym

env = gym.make('CartPole-v1')


def policy(state: tuple):
    """Choosing action based on epsilon-greedy policy"""
    return np.argmax(Q_table[state])


def new_q_value(reward: float, new_state: tuple, discount_factor=1) -> float:
    """Temporal difference for updating Q-value of state-action pair"""
    future_optimal_value = np.max(Q_table[new_state])
    learned_value = reward + discount_factor * future_optimal_value
    return learned_value


def convert_to_discrete(_, __, angle, pole_velocity) -> Tuple[int, ...]:
    """Convert continuous state intro a discrete state"""
    est = KBinsDiscretizer(n_bins=n_bins, encode='ordinal', strategy='uniform')
    est.fit([lower_bounds, upper_bounds])
    return tuple(map(int, est.transform([[angle, pole_velocity]])[0]))


# Adaptive learning of Learning Rate
def learning_rate(n: int, min_rate = 0.01) -> float:
    """Decaying learning rate"""
    return max(min_rate, min(1.0, 1.0 - math.log10((n + 1) / 25)))


def exploration_rate(n: int, min_rate=0.1) -> float:
    """Decaying exploration rate"""
    return max(min_rate, min(1, 1.0 - math.log10((n + 1) / 25)))


n_bins = (6, 12)
lower_bounds = [env.observation_space.low[2], -math.radians(50)]
upper_bounds = [env.observation_space.high[2], math.radians(50)]


# Initialize the Q value table with zeros.
Q_table = np.zeros(n_bins + (env.action_space.n,))
Q_table.shape


# TRAINING
num_episodes = 1000
for e in range(num_episodes):

    # Discrete-ize state into buckets
    current_state, done = convert_to_discrete(*env.reset()), False

    while not done:

        # policy action
        action = policy(current_state)

        # insert random action
        if np.random.random() < exploration_rate(e):
            action = env.action_space.sample()  # explore

        # increment environment
        obs, reward, done, _ = env.step(action)
        new_state = convert_to_discrete(*obs)

        # Update Q-Table
        lr = learning_rate(e)
        learnt_value = new_q_value(reward, new_state)
        old_value = Q_table[current_state][action]
        Q_table[current_state][action] = (1 - lr) * old_value + lr * learnt_value

        current_state = new_state

        # Render the cartpole environment
        env.render()
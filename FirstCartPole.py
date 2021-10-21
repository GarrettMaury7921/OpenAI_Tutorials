import gym
import random
import numpy as np
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from statistics import mean, median
from collections import Counter

env_name = "CartPole-v1"
environment = gym.make(env_name)


class Agent:
    def __init__(self, env):
        self.action_size = env.action_space.n
        print("Action size:", self.action_size)

    def get_action(self, state):
        # action = random.choice(range(self.action_size))
        pole_angle = state[2]
        if pole_angle < 0:
            action_num = 0
        else:
            action_num = 1
        return action_num


agent = Agent(environment)
state = environment.reset()

for _ in range(500):
    #     action = env.action_space.sample()
    action = agent.get_action(state)
    # Seeing if the environment is done, if so, reset
    # STATE = OBSERVATION
    state, reward, done, info = environment.step(action)
    environment.render()
    if done:
        state = environment.reset()

environment.close()

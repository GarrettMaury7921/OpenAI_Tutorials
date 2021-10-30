import gym
from gym import Env
from gym.spaces import Discrete, Box, Dict, Tuple, MultiBinary, MultiDiscrete
import numpy as np
import random
import os
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3.common.evaluation import evaluate_policy


class ShowerEnv(Env):
    def __init__(self):
        pass

    def step(self, action):
        pass

    def render(self):
        pass

    def reset(self):
        pass

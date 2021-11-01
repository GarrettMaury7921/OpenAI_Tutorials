import gym
from gym import Env
from gym.spaces import Discrete, Box, Dict, Tuple, MultiBinary, MultiDiscrete
import numpy as np
import random
import os
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3.common.evaluation import evaluate_policy


class ShowerEnv(Env):
    def __init__(self):
        # Actions we can take, down, stay, up
        self.action_space = Discrete(3)
        # Temperature array
        self.observation_space = Box(low=np.array([0]), high=np.array([100]))
        # Set start temp
        self.state = 38 + random.randint(-3, 3)
        # Set shower length (episode length)
        self.shower_length = 60

    def step(self, action):
        # Apply action
        # 0 -1 = -1 temperature
        # 1 -1 = 0
        # 2 -1 = 1 temperature
        self.state += action - 1
        # Reduce shower length by 1 second
        self.shower_length -= 1

        # Calculate reward
        if 37 <= self.state <= 39:
            reward = 1
        else:
            reward = -1

            # Check if shower is done
        if self.shower_length <= 0:
            done = True
        else:
            done = False

        # Apply temperature noise
        # self.state += random.randint(-1,1)
        # Set placeholder for info
        info = {}

        # Return step information
        return self.state, reward, done, info

    def render(self):
        pass

    def reset(self):
        # Reset shower temperature
        self.state = np.array([38 + random.randint(-3, 3)]).astype(float)
        # Reset shower time
        self.shower_length = 60
        return self.state


# Custom Env
env = ShowerEnv()
PPO_Shower = os.path.join('Training', 'Saved Models', 'PPO_Shower')

# LOAD MODEL
model = PPO.load(PPO_Shower, env)

# Train Model
log_path = os.path.join('Training', 'Logs')
model = PPO("MlpPolicy", env, verbose=1, tensorboard_log=log_path)
# model.learn(total_timesteps=400000)

# Save Model
# model.save('PPO_Shower')


# TEST ENVIRONMENT
# evaluate_policy(model, env, n_eval_episodes=10)
episodes = 5
for episode in range(1, episodes + 1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        action = env.action_space.sample()
        n_state, reward, done, info = env.step(action)
        score += reward
    print('Episode:{} Score:{}'.format(episode, score))
env.close()


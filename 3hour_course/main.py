import os
import gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy

environment_name = 'CartPole-v0'
log_path = os.path.join('training', 'Logs')

env = gym.make(environment_name)
env = DummyVecEnv([lambda: env])
# USING GPU, importing algorithm PPO
model = PPO('MlpPolicy', env, verbose=1)

# Training
model.learn(total_timesteps=20000)
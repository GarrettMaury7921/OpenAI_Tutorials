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

PPO_PATH = os.path.join('Training', 'Saved Models', 'PPO_MODEL_CartPole')

# Delete it from here
# del model

# Load it from the folder
model = PPO.load(PPO_PATH, env=env)

# Training
# model.learn(total_timesteps=50000)

# Save the model into a folder
model.save(PPO_PATH)

# Evaluate our policy
evaluate_policy(model, env, n_eval_episodes=10, render=True)

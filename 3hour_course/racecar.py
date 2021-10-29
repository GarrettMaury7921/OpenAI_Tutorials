import gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import VecFrameStack, DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
import os

# ENVIRONMENT
environment_name = "CarRacing-v0"
env = gym.make(environment_name)
env = DummyVecEnv([lambda: env])

# PATHS
ppo_path = os.path.join('Training', 'Saved Models', 'PPO_Driving_model')
log_path = os.path.join('Training', 'Logs')

# MODEL
model = PPO('CnnPolicy', env, verbose=1, tensorboard_log=log_path)

# LOAD MODEL
model = PPO.load(ppo_path, env)

# LEARN
# model.learn(total_timesteps=1000)

# SAVE MODEL
# model.save(ppo_path)

# TEST AND EVALUATE
evaluate_policy(model, env, n_eval_episodes=10, render=True)
env.close()

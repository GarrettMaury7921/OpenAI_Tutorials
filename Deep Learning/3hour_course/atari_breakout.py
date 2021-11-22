import gym
from stable_baselines3 import A2C
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_atari_env
import os

# PATHS OF FILES
log_path = os.path.join('Training', 'Logs')
a2c_path = os.path.join('Training', 'Saved Models', 'A2C_model')
a2c_2m_path = os.path.join('Training', 'Saved Models', 'A2C_2M_model')
a2c_2more_path = os.path.join('Training', 'Saved Models', 'A2C_2M+_model')

# TESTING
env = make_atari_env('Breakout-v0', n_envs=1, seed=0)
env = VecFrameStack(env, n_stack=4)

# TRAINING
# env = make_atari_env('Breakout-v0', n_envs=4, seed=0)
# env = VecFrameStack(env, n_stack=4)

# Model
# model = A2C("CnnPolicy", env, verbose=1, tensorboard_log=log_path)
# Without logging
model = A2C("CnnPolicy", env, verbose=1)

# LEARNING
# model.learn(total_timesteps=400000)

# SAVE MODEL OR DELETE
# model.save(a2c_path)
# del model

# LOAD MODEL
# model = A2C.load(a2c_path, env)
# 2 Million Tries Model
model = A2C.load(a2c_2more_path, env)

# LEARN A LOADED MODEL
# model.learn(total_timesteps=20000)
# SAVE MODEL
# model.save(a2c_2more_path)

# EVALUATE AND TEST
# evaluate_policy(model, env, n_eval_episodes=5, render=True)
obs = env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
env.close()

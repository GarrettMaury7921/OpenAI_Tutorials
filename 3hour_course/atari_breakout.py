import gym
from stable_baselines3 import A2C
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_atari_env
import os

log_path = os.path.join('Training', 'Logs')
a2c_path = os.path.join('Training', 'Saved Models', 'A2C_model')

# TESTING
env = make_atari_env('Breakout-v0', n_envs=1, seed=0)
env = VecFrameStack(env, n_stack=4)

# TRAINING
# env = make_atari_env('Breakout-v0', n_envs=4, seed=0)
# env = VecFrameStack(env, n_stack=4)

# Model
model = A2C("CnnPolicy", env, verbose=1, tensorboard_log=log_path)

# LEARNING
# model.learn(total_timesteps=500)

# SAVE MODEL OR DELETE
# model.save(a2c_path)
del model

# LOAD MODEL
model = A2C.load(a2c_path, env)

# EVALUATE AND TEST
evaluate_policy(model, env, n_eval_episodes=10, render=True)
# obs = env.reset()
# while True:
#     action, _states = model.predict(obs)
#     obs, rewards, dones, info = env.step(action)
#     env.render()
# env.close()

import os
import gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.callbacks import EvalCallback, StopTrainingOnRewardThreshold
from stable_baselines3.common.evaluation import evaluate_policy

# VARIABLES
environment_name = 'CartPole-v0'
log_path = os.path.join('training', 'Logs')
PPO_PATH = os.path.join('Training', 'Saved Models', 'PPO_MODEL_CartPole')

env = gym.make(environment_name)
env = DummyVecEnv([lambda: env])
# USING GPU, importing algorithm PPO
model = PPO('MlpPolicy', env, verbose=1)

# Delete the model
# del model

# Load it from the folder
# model = PPO.load(PPO_PATH, env=env)

# Callbacks - Stop training once it reaches 200 average, verbose is for logging
save_path = os.path.join('Training', 'Saved Models')
stop_callback = StopTrainingOnRewardThreshold(reward_threshold=200, verbose=1)
# Every 1000 episodes it checks if the average is 200 or more, then stops the training,
# then save the best model to the save path
eval_callback = EvalCallback(env,
                             callback_on_new_best=stop_callback,
                             eval_freq=10000,
                             best_model_save_path=save_path,
                             verbose=1)
# With callbacks
# model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=log_path)

# Changing Policies
net_arch = [dict(pi=[128, 128, 128, 128], vf=[128, 128, 128, 128])]
# model = PPO('MlpPolicy', env, verbose=1, policy_kwargs={'net_arch': net_arch})
# model.learn(total_timesteps=200, callback=eval_callback)

# Training
# model.learn(total_timesteps=50000)
# Training with Callbacks
# model.learn(total_timesteps=20000, callback=eval_callback)

# Evaluate our policy
evaluate_policy(model, env, n_eval_episodes=100, render=True)

# TEST
# episodes = 5
# for episode in range(1, episodes+1):
#     obs = env.reset()
#     done = False
#     score = 0
#
#     while not done:
#         env.render()
#         action, _ = model.predict(obs)  # Using Model Here
#         obs, reward, done, info = env.step(action)
#         score += reward
#     print('Episode:{} Score:{}'.format(episode, score))
# env.close()

# Save the model into a folder
# model.save(PPO_PATH)

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
# LAYERS ERROR, INSTALL TENSORFLOW 2.5
from tensorflow.keras.layers import Dense, Flatten, Convolution2D
from tensorflow.keras.optimizers import Adam
from rl.agents import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import LinearAnnealedPolicy, EpsGreedyQPolicy
import gym
import random


def build_model(height, width, channels, actions):
    model = Sequential()
    model.add(Convolution2D(32, (8, 8), strides=(4, 4), activation='relu', input_shape=(3, height, width, channels)))
    model.add(Convolution2D(64, (4, 4), strides=(2, 2), activation='relu'))
    model.add(Convolution2D(64, (3, 3), activation='relu'))
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dense(256, activation='relu'))
    model.add(Dense(actions, activation='linear'))
    return model


def build_agent(model, actions):
    policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1., value_min=.1, value_test=.2,
                                  nb_steps=10000)
    memory = SequentialMemory(limit=1000, window_length=3)
    dqn = DQNAgent(model=model, memory=memory, policy=policy,
                   enable_dueling_network=True, dueling_type='avg',
                   nb_actions=actions, nb_steps_warmup=1000
                   )
    return dqn


env = gym.make('SpaceInvaders-v0')
height, width, channels = env.observation_space.shape
actions = env.action_space.n

model = build_model(height, width, channels, actions)

dqn = build_agent(model, actions)
dqn.compile(Adam(lr=1e-4))

# LOAD MODEL
# dqn.load_weights('SavedWeights/SpaceInvaders1/dqn_weights.h5f')

# TRAINING
# dqn.fit(env, nb_steps=10000, visualize=False, verbose=2)

# TESTING
scores = dqn.test(env, nb_episodes=10, visualize=True)
print(np.mean(scores.history['episode_reward']))

# SAVE
# dqn.save_weights('SavedWeights/SpaceInvaders1/dqn_weights.h5f', overwrite=True)

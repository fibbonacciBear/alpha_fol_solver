import gymnasium as gym
from gymnasium.spaces import Box
import numpy as np
import string

MAX_OBSERVATION_LENGTH = 1000


class TextToBoxWrapper(gym.ObservationWrapper):

    def __init__(self, env):
        super().__init__(env)

        self.vocab = (
            string.ascii_letters + string.digits + string.punctuation + " " + "\n"
        )
        self.observation_space = Box(low=0, high=len(self.vocab), shape=(MAX_OBSERVATION_LENGTH,), dtype=np.int32)

    def observation(self, obs):
        assert len(obs) <= MAX_OBSERVATION_LENGTH
        obs = obs.ljust(MAX_OBSERVATION_LENGTH, " ")
        return np.array([self.vocab.index(char) for char in obs])

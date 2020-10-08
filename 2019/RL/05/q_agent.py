from collections import defaultdict
import numpy as np
import random

class QLearningAgent:
    def __init__(self, alpha, epsilon, gamma, get_legal_actions):
        self.get_legal_actions = get_legal_actions
        self._q_values = defaultdict(lambda: defaultdict(lambda: 0))  # when called, non-existent values appear as zeros
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma

    def get_q_value(self, state, action):
        """
          Returns Q(state,action)
        """
        return self._q_values[state][action]

    def set_q_value(self, state, action, value):
        """
          Sets the Qvalue for [state,action] to the given value
        """
        self._q_values[state][action] = value

    def get_value(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.
        """

        possible_actions = self.get_legal_actions(state)
        # If there are no legal actions, return 0.0
        if len(possible_actions) == 0:
            return 0.0

        value = max([self.get_q_value(state, action) for action in possible_actions])
        return value

    def get_policy(self, state):
        """
          Compute the best action to take in a state.

        """
        possible_actions = self.get_legal_actions(state)

        # If there are no legal actions, return None
        if len(possible_actions) == 0:
            return None

        best_action = None

        for action in possible_actions:
            if best_action is None:
                best_action = action
            elif self.get_q_value(state, action) > self.get_q_value(state, best_action):
                best_action = action

        return best_action

    def get_action(self, state):
        """
          Compute the action to take in the current state, including exploration.

          With probability self.epsilon, we should take a random action.
          otherwise - the best policy action (self.getPolicy).

        """

        #
        possible_actions = self.get_legal_actions(state)

        # если в текущей ситуации нет возможных действий - возвращаем None
        if len(possible_actions) == 0:
            return None

        if np.random.random() < self.epsilon:
            action = random.choice(possible_actions)
        else:
            action = self.get_policy(state)
        return action

    def update(self, state, action, next_state, reward):
        t = self.alpha * (reward + self.gamma * self.get_value(next_state) - self.get_q_value(state, action))
        reference_qvalue = self.get_q_value(state, action) + t
        self.set_q_value(state, action, reference_qvalue)

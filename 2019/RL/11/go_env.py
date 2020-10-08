import sys

import pachi_py
import numpy as np
import gym


class KoState:
    def __init__(self, state):
        self.state = state

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return self.state.__hash__()


class GoEnv(gym.Env):
    def render(self, mode='ansi'):
        sys.stdout.write(self.board.__repr__().decode().replace("O", "W").replace("X", "B") + '\n')

    def step(self, action):

        if not self.done:
            if action not in self.get_possible_actions():
                raise KeyError("Wrong action")
            self.board = self.board.play(action, self.current_player)

        self.current_player = 1 if self.current_player == 2 else 2

        if (self.opponent_pass and action == -1) or self.board.is_terminal:
            self.done = True
        if not self.done:
            self.opponent_pass = action == -1
        self.game_states.add(KoState(state=self.board))
        return self.get_state(), self.get_reward() if self.done else 0, self.done, None

    def reset(self):
        self.game_states = set()
        self.current_player = 1
        self.board = pachi_py.CreateBoard(self.size)
        self.opponent_pass = False
        self.done = False
        self.game_states = set()
        self.game_states.add(KoState(state=self.board))
        return self.get_state()

    def __init__(self, size=5):
        self.size = size
        self.done = None
        self.current_player = None
        self.board = None
        self.opponent_pass = None
        self.game_states = None

    def get_possible_actions(self):
        legal_moves = self.board.get_legal_coords(color=self.current_player, filter_suicides=True)
        result = set()
        result.add(-1)
        for move in legal_moves:
            if move == -1:
                continue

            new_board = self.board.clone()
            new_board = new_board.play(move, self.current_player)
            if KoState(new_board) not in self.game_states:
                result.add(move)
        return list(result)

    def get_state(self):
        black = tuple(map(tuple, self.board.black_stones.tolist()))
        white = tuple(map(tuple, self.board.white_stones.tolist()))
        return black, white, self.opponent_pass, self.done, self.current_player

    def __eq__(self, other):
        return self.get_state() == other.get_state()

    def __hash__(self):
        return self.board.__hash__()

    def get_reward(self):
        result = 0.5
        if self.board.official_score > 0:
            result = 1
        if self.board.official_score < 0:
            result = 0
        return result if self.current_player == 1 else 1 - result


def main():
    g = GoEnv()
    g.reset()
    while not g.done:
        state, reward, done, _ = g.step(np.random.choice(g.get_possible_actions()))
        print("player:", g.current_player, "reward:", reward)
    g.render()


if __name__ == '__main__':
    main()

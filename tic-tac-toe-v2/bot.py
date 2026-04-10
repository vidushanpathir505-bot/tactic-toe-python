'''This is bot class'''
import random
from player import Player

class Bot(Player):

    def __init__(self, symbol, name='player'):
        super().__init__(symbol, name)

    def choose_move(self, board):
# make bot move
        empty_positions = [p for p in range(9) if board[p] == '_']

        if not empty_positions:
            return None

        elif 4 in empty_positions:
            return 4

        else:
            return random.choice(empty_positions)
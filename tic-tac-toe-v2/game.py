'''This is game class it control the game'''

from player import Player
from bot import Bot

class Game:

    def __init__(self, name1, name2, mode):
       
        self.board = ['_','_','_',
                     '_','_','_',
                     '_','_','_',]
       
        self.win_patterns = [
                            (0,1,2), (3,4,5), (6,7,8),   
                            (0,3,6), (1,4,7), (2,5,8),   
                            (0,4,8), (2,4,6)             
                            ]
       
        if mode == 'pvp':
           self.player1 = Player('X', name=name1)
           self.player2 = Player('O', name=name2)

        if mode == 'bot':
           self.player1 = Player('X', name=name1)
           self.player2 = Bot('O', name='Bot')

        self.current_player = self.player1
       
    def make_move(self, position, symbol):
#checking is the move valid or not

        if symbol not in ('X', 'O'):
            return False
        
        elif not 0 <= position <= 8:
            return False
        
        elif not self.board[position] == '_':
            return False
        
        else:
            self.board[position] = symbol
            return True
        
    def check_winner(self):
# check player win or lose

        for a, b, c in self.win_patterns:
            if self.board[a] == self.board[b] == self.board[c] != '_':
                return self.board[a]
        return None

    def is_draw(self):
# check the draw situation
        
        if '_' not in  self.board:
            return True
        return False
    
    def reset_board(self):           
# clean the board after round

        self.board = ['_','_','_',
                     '_','_','_',
                     '_','_','_',]

    def switch_player(self):
# use to switch player 

        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def play_turn(self, position):
# handle the game

        if self.make_move(position=position, symbol=self.current_player.symbol):
            
            winner = self.check_winner()

            if winner:
                return f'{winner} wins'
            
            draw = self.is_draw()

            if draw:
                return 'Draw'
            
            self.switch_player()

            if isinstance(self.current_player, Bot):
                return self.bot_play()

            return 'Continue'
        
        return 'Invalid Move'

    def bot_play(self):
# handle the bot turn
            
        position = self.current_player.choose_move(self.board)

        return self.play_turn(position)



 
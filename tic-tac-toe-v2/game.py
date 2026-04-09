'''This is game class it control the game'''

class Game:

    def __init__(self):
       self.board = ['_','_','_',
                     '_','_','_',
                     '_','_','_',]
       
    def make_move(self, position, symbol):
#checking is the move valid or not

        if symbol not in ('X', 'O'):
            return 'Invalid Symbol'
        
        elif not 0 <= position <= 8:
            return 'Out of Range'
        
        elif not self.board[position] == '_':
            return 'Place is taken'
        
        else:
            self.board[position] = symbol
            return True
        



game = Game()
print(game.make_move(position=5, symbol='X'))
print(game.make_move(position=5, symbol='X'))

 
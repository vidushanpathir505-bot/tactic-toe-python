'''This is player class'''

class Player:

    def __init__(self, symbol, name='player'):

        if symbol not in ('X', 'O'):           #check symbol is right or wrong
            raise ValueError("Symbol must be 'X' or 'Y'")
        
        self.symbol = symbol
        self.name = name
        
        
print(Player('X')   )    
        


#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.

class Player:
    def __init__(self, checker):
        self.checker = checker
        self.num_moves = 0 
        assert(checker == 'X' or checker == 'O')
    

    def __repr__(self):
        return 'Player' + ' ' + str(self.checker)
    
    def opponent_checker(self):
        opponentschecker = ''
        if self.checker == 'X':
            opponentschecker += 'O'
        elif self.checker == 'O':
            opponentschecker += 'X'
            
        return opponentschecker
    
    def next_move(self, b):
        self.num_moves += 1
        col = int(input('Enter a column: '))
        while True:
            if b.can_add_to(col):
                if col in range(b.width):
                    return col
            else:
                print('Try again!')
                col = int(input('Enter a column: '))

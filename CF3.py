#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b

def process_move(p,b):
    print(str(p) + "'s" + " " + "turn")
    print()
    col = p.next_move(b)
    b.add_checker(p.checker, col)
    print()
    print(b)
    print()    
    if b.is_win_for(p.checker):
        print('Player' + " " + p.checker + " " + 'wins in' + " " + str(p.num_moves) + " " + 'moves')
        print('Congratulations!')
        return True
    elif b.is_full():
        print("It's a tie!")
        return True
    return False
        
class RandomPlayer(Player):
    
    def next_move(self, b):
        randomlist = []
        for col in range(b.width):
            if b.can_add_to(col) == True:
                randomlist += [col]
        return random.choice(randomlist)
    
    
    
    
    
    

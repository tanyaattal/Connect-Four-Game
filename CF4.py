#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player): 
    def __init__(self, checker, tiebreak, lookahead):
        
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        
        self.tiebreak = tiebreak 
        self.lookahead = lookahead
        self.num_moves = 0
        
    def __repr__(self):
        tie = self.tiebreak 
        look = self.lookahead
        
        checker = super().__repr__() 
        
        return checker + ' ' + '(' + str(tie) + ',' + ' ' + str(look) + ')'
    
    def max_score_column(self, scores):
        maximum = max(scores)
        randommax = []
        for i in range(len(scores)):
            if scores[i] == maximum:
                randommax += [i]
        if self.tiebreak == 'LEFT':
            return randommax[0]
        elif self.tiebreak == 'RIGHT':
            return randommax[-1]
        elif self.tiebreak == 'RANDOM':
            return random.choice(randommax)

    def scores_for(self, b):
        scores = [50] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead -1 )
                opp_scores = opponent.scores_for(b)
                if max(opp_scores) == 100:
                    scores[col] = 0
                elif max(opp_scores) == 0:
                    scores[col] = 100
                else:
                    scores[col] = 50
                b.remove_checker(col) 
        return scores                 
        
    def next_move(self, b):
        self.num_moves += 1
        x = self.scores_for(b)
        return self.max_score_column(x)
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
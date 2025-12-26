class Board:  
    ### add your constructor here ###
    def  __init__(self, height, width):
        
        self.height = height
        self.width = width 
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        for col in range(self.width):
            s += 2 * '-'
        s += '-'
        
        s += '\n'
        
        for col in range(self.width):
            s += ' ' + str(col % 10)
        
        s + '\n'
        return s

    def add_checker(self, checker, col):
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        row = -1
        while self.slots[row][col] != ' ':
            row -= 1 
        self.slots[row][col] = checker
        
    ### add your reset method here ###
    def reset(self):
        self.slots = [[' '] * self.width for row in range(self.height)]
        
    def add_checkers(self, colnums):
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    def can_add_to(self, col):
        for row in range(self.height):
            if col in range(self.width):
                if self.slots[row][col] == ' ':
                    return True
        return False
            
    def is_full(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.slots[row][col] == ' ':
                    return False
        
        return True
    
    def remove_checker(self, col):
        for row in range(self.height):
            if self.slots[row][col] == 'X' or self.slots[row][col] == 'O':
                self.slots[row][col] = ' '
                break 
        self.slots[row][col] = ' '
        
    def is_horizontal_win(self, checker):
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                       return True

        # if we make it here, there were no horizontal wins
        return False
    def is_vertical_win(self, checker):
        assert(checker == 'X' or checker == 'O')
        for row in range(self.height-3):
            for col in range(self.width):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col] == checker and \
                   self.slots[row+2][col] == checker and \
                   self.slots[row+3][col] == checker:
                       return True

        # if we make it here, there were no horizontal wins
        return False
    
    def is_down_diagonal_win(self, checker):
        assert(checker == 'X' or checker == 'O')
        for row in range(self.height-3):
            for col in range(self.width-3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col+1] == checker and \
                   self.slots[row+2][col+2] == checker and \
                   self.slots[row+3][col+3] == checker:
                       return True

        # if we make it here, there were no horizontal wins
        return False
    
    def is_up_diagonal_win(self, checker):
        assert(checker == 'X' or checker == 'O')
        for row in range(3, self.height):
            for col in range(self.width-3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row-1][col+1] == checker and \
                   self.slots[row-2][col+2] == checker and \
                   self.slots[row-3][col+3] == checker:
                       return True

        # if we make it here, there were no horizontal wins
        return False
       
    def is_win_for(self, checker):
        assert(checker == 'X' or checker == 'O')

        if self.is_horizontal_win(checker):
            return True
        if self.is_vertical_win(checker):
            return True
        if self.is_down_diagonal_win(checker):
            return True
        if self.is_up_diagonal_win(checker):
            return True
        else:
            return False 
        
import time

class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = []
        for i in range(3):
            self.current_state.append(['.' for c in range(3)])


        # Player X always plays first
        self.player_turn = 'X'

    def draw_current_state(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()
    
    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '.':
            return False
        else:
            return True
    
        
    # Checks if the game has ended and returns the winner in each case
    def is_end(self):
        # Vertical win
        for i in range(0, 3):
            if (self.current_state[0][i] != '.' and
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

        # Horizontal win
        for row in self.current_state:
            if len(set(row))==1:
                if row[0] != '.':
                    return row[0]


        # Main diagonal win
        if len(set([self.current_state[i][i] for i in range(len(self.current_state))]))==1:
            if self.current_state[0][0] != '.':
                return self.current_state[0][0]

        # Second diagonal win
        if len(set([self.current_state[i][len(self.current_state)-i-1] for i in range(len(self.current_state))]))==1:
            if self.current_state[0][len(self.current_state)-1] != '.':
                return self.current_state[0][len(self.current_state)-1]

        # Is whole current_state full?
        sumElemnts = 0
        for i in range(3):
            sumElemnts+=self.current_state[i].count('.')
        if sumElemnts > 1:
            return None

        # It's a tie!
        return '.'
    
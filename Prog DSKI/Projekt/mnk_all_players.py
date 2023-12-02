import numpy as np
import random


class Player():

    def __init__(self, player_number, name) -> None: # player number 1 or 2 
        self.name = name
        self.player_number = player_number
        pass

    def make_move(self): # -> (row, col)

        #### REMOVE THIS! ####
        move = (1, 1)# (x, y) tuple where move is placed
        return move
    
    def is_valid(self, m, n):
        valid_row = 0 <= m < self.m
        valid_col = 0 <= n < self.n
        empty_cell = self.board[m][n] == 0
        
        return valid_row and valid_col and empty_cell


class Bot_radom(Player):

    def __init__(self, player_number, name="random bot") -> None:
        super().__init__(player_number, name)

    def make_move(self, board): # -> (row, col)
        """_summary_k > n or self.k < self.n
        Args:
            board (_type_): _description_
        """
        while True:
            x = random.randint(0, self.m - 1)
            y = random.randint(0, self.n - 1)
            if self.is_valid(x, y):
                self.board[x][y] = Player() #da bin ich mir noch nicht sicher
            return x, y


class Bot_not_random(Player):

    def __init__(self, player_number, name="non random bot") -> None:
        super().__init__(player_number, name)

    def make_move(self, board): # -> (row, col)

        #### REMOVE THIS! ####
        move = (1, 1)# (x, y) tuple where move is placed
        return move


class Bot_comples(Player):

    def __init__(self, player_number, name="complex bot") -> None:
        super().__init__(player_number, name)

    def make_move(self, board): # -> (row, col)
        
        #### REMOVE THIS! ####
        move = (1, 1)# (x, y) tuple where move is placed
        return move


if __name__ == "__main__":
    # hier kommt zeug zum testen hin
    pass
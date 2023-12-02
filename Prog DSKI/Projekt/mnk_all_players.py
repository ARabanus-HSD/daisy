import numpy as np
import random as rdm


class Player():

    def __init__(self, player_number, name) -> None: # player number 1 or 2 
        self.name = name
        self.player_number = player_number
        pass

    def make_move(self): # -> (row, col)

        #### REMOVE THIS! ####
        move = (1, 1)# (x, y) tuple where move is placed
        return move


class Bot_radom(Player):

    def __init__(self, player_number, name="random bot") -> None:
        super().__init__(player_number, name)

    def make_move(self, board): # -> (row, col)
        
        #### REMOVE THIS! ####
        move = (1, 1)# (x, y) tuple where move is placed
        return move


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
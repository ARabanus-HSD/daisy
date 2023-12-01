import numpy as np
import random as rdm


class Player():

    def __init__(self, name, player_number) -> None: # player number 1 or 2 
        self.name = name
        self.player_number = player_number
        pass

    def make_move(self): # -> (row, col)
        pass


class Bot_radom(Player):

    def __init__(self, name, player_number) -> None:
        super().__init__(name, player_number)

    def make_move(self, board): # -> (row, col)
        pass


class Bot_not_random(Player):

    def __init__(self, name, player_number) -> None:
        super().__init__(name, player_number)

    def make_move(self, board): # -> (row, col)
        pass


class Bot_comples(Player):

    def __init__(self, name, player_number) -> None:
        super().__init__(name, player_number)

    def make_move(self, board): # -> (row, col)
        pass
    
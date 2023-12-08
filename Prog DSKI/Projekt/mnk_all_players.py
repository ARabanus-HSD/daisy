import numpy as np
import mnk_board as board
import random


class Player():

    def __init__(self, player_number, name) -> None: # player number 1 or 2 
        self.name = name
        self.player_number = player_number
        pass

    def make_move(self, player): # -> (row, col)
        #### REMOVE THIS! ####
        player_move = (int(input("Please make a move: ")), int(input("")))
        return player_move

    #Dalia
    def is_valid(self, moves:tuple, board):
        '''
        erhält ein tuple von moves
        prüft ob moves in valid raum ist
        gibt true or false wieder
        '''
        valid_row = 0 <= moves[0] < self.m
        valid_col = 0 <= moves[1] < self.n
        empty_cell = board[moves[0]][moves[1]] == 0
        if valid_row and valid_col and empty_cell:
            return True
        return False


class Bot_random(Player):

    def __init__(self, player_number, name="random bot") -> None:
        super().__init__(player_number, name)
        
    def make_move(self): # -> (row, col)
        """_summary_k > n or self.k < self.n
        made by Dalia
        Args:
            board (_type_): _description_
        """
        moves = (1, 1)
        while True:
            moves[0] = random.randint(0, self.board.shape[0] - 1)
            moves[1] = random.randint(0, self.board.shape[1] - 1)
            if self.is_valid(moves):
                self.board[moves[0]][moves[1]] = Player() #da bin ich mir noch nicht sicher - I think it's false
            return moves


class Bot_simple(Player):

    def __init__(self, player_number, name="non random bot") -> None:
        super().__init__(player_number, name)

    def make_move(self): # -> (row, col)

        #### REMOVE THIS! ####
        move = (1, 1)# (x, y) tuple where move is placed
        return move


class Bot_complex(Player):

    def __init__(self, player_number, name="complex bot") -> None:
        super().__init__(player_number, name)

    def make_move(self): # -> (row, col)
        
        #### REMOVE THIS! ####
        move = (1, 1)# (x, y) tuple where move is placed
        return move


if __name__ == "__main__":
    # hier kommt zeug zum testen hin
    pass
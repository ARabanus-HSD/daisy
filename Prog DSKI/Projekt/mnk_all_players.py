import numpy as np
import mnk_board as board
import random


class Player():

    def __init__(self, player_number, name, board) -> None: # player number 1 or 2
        self.name = name
        self.player_number = player_number
        self.board = board
        pass

    def make_move(self): # -> (row, col)
        player_move = (int(input("Please make a move: ")), int(input("")))
        return player_move

    def is_valid(self, moves:tuple, board):
        '''
        erhält ein tuple von moves
        prüft ob moves in valid raum ist
        gibt true or false wieder
        made by Dalia
        '''
        valid_row = 0 <= moves[0] < self.board.shape[0]
        valid_col = 0 <= moves[1] < self.board.shape[1]
        empty_cell = board[moves[0]][moves[1]] == 0
        if valid_row and valid_col and empty_cell:
            return True
        return False


class Bot_random(Player):

    def __init__(self, player_number, name, board) -> None:
        super().__init__(player_number, name, board)
        pass
        
    def make_move(self): # -> (row, col)
        """erzeugt random move und fragt ab ob random move valid ist 
        made by Dalia
        """
        moves = (1, 1)
        while True:
            moves[0] = random.randint(0, self.board.shape[0] - 1)
            moves[1] = random.randint(0, self.board.shape[1] - 1)
            if self.is_valid(moves, self.board):
                self.board[moves[0]][moves[1]] = Player() #da bin ich mir noch nicht sicher - I think it's false
            return moves


class Bot_simple(Player):

    def __init__(self, player_number, name, board) -> None:
        super().__init__(player_number, name, board)
        pass

    def make_move(self): # -> (row, col)
        if not np.any(self.board):
            move = (random.randint(self.board.shape[0]),
                    random.randint(self.board.shape[1]))
    
        else:
            move = (1, 1)
        # "look" at board
        # start at center of board
        # search for row/col/diagonal with at least k free slots
        # place on move on first slot that fulfills criteria

        # return move
        return move


class Bot_complex(Player):

    def __init__(self, player_number, name, board) -> None:
        super().__init__(player_number, name, board)

    def make_move(self): # -> (row, col)
        
        #### REMOVE THIS! ####
        move = (1, 1)# (x, y) tuple where move is placed
        return move


if __name__ == "__main__":
    # hier kommt zeug zum testen hin
    pass
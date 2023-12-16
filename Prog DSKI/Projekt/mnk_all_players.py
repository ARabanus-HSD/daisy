import numpy as np
import mnk_board
import random


class Player():

    def __init__(self, player_number, name, board) -> None: # player number 1 or 2
        self.name = name
        self.player_number = player_number
        self.board = board
        pass

    def is_valid(self, move:tuple):
        '''
        erhält ein tuple von moves
        prüft ob moves in valid raum ist
        gibt true or false wieder
        made by Dalia
        '''
        # valid_row = 0 <= move[0] < self.board.shape[0]
        # valid_col = 0 <= move[1] < self.board.shape[1]
        # empty_cell = self.board[move[0]][move[1]] == 0
        # if valid_row and valid_col and empty_cell:
            # return True
        # return False
        """
        alternative von Anton
        """
        # checks im move is in range of the size of the board
        if move[0] < self.board.shape[0] and move[1] < self.board.shape[1]:
            if self.board[move] == 0:
                return True
        else:
            return False
        # checks the cell that is to be changed is == 0

    
    def make_move(self): # -> (row, col)
        """
        fragt spielerzug ab und returned tuple mit zwei koordinaten
        prüft mit is_valid ob der spielzug valid ist
        """
        print(f"make move between 0 and {self.board.shape[0]} \nand 0 and {self.board.shape[1]}")
        move = (int(input("Please make a move: ")), int(input("")))
        if self.is_valid(move):
                return move
        else:
            raise ValueError("incoreect random number! Try again mister AI!!!") # ? müsste eig. an den anfang von make move springen!
            

class Bot_random(Player):

    def __init__(self, player_number, name, board) -> None:
        super().__init__(player_number, name, board)
        pass
        
    def make_move(self): # -> (row, col)
        """erzeugt random move und fragt ab ob random move valid ist 
        made by Dalia
        """
        move = (1, 1)
        while True:
            move[0] = random.randint(0, self.board.shape[0] - 1)
            move[1] = random.randint(0, self.board.shape[1] - 1)
            if self.is_valid(move, self.board):
                self.board[move[0]][move[1]] = Player() #da bin ich mir noch nicht sicher - I think it's false
            return move


class Bot_simple(Player):

    def __init__(self, player_number, name, board) -> None:
        super().__init__(player_number, name, board)
        pass

    def make_move(self): # -> (row, col)
        print(self.board)
        
        # when all slots are empty, choose a random point on the grid
        if not np.any(self.board):
            move = (random.randint(0, self.board.shape[0]-1),
                    random.randint(0, self.board.shape[1]-1))
        # if the move is valid, return the move
            if self.is_valid(move):
                print(f"the move to be made is {move}")
                return move
            else:
                raise ValueError("incorrect random number! Try again mister AI!!!") # ? müsste eig. an den anfang von make move springen!

            

        # "look" at board
        # start at center of board
        # search for row/col/diagonal with at least k free slots
        # place on move on first slot that fulfills criteria



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
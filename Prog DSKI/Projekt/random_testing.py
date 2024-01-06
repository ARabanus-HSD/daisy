import numpy as np
import time
import random


def keep_cross(input_array, n_row, n_col):
    """
    - makes a mask filled with zeros, except for chosen n_row and n_col
    - multiplies mask with input array 

    Args:
        input_array (_type_): numpy array
        n_row (_type_): starts with 0!
        n_col (_type_): starts with 0!
    """
    
    mask = np.ones((input_array.shape[0], input_array.shape[1]), dtype=float)
    row_and_col = [n_row, n_col]
    for i in row_and_col:
        mask[:, i] = 0
        mask[i, :] = 0
        
    output_array = input_array * mask
    
    return output_array

def search_horizontal(array, k):
    # go through rows in array
    # if there is a k-long line of 0s:
        # palce marker at either left or right most (random)
    pass

def search_vertical(array, k):
    
    pass

def search_diagonal(array, k):
    # go
    pass

def make_move(arr):
    print(arr)
    if not np.any(arr):
        move = (random.randint(board.shape))
    else:
        print("something else")
    pass

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
        valid_row = 0 <= move[0] < self.board.shape[0]
        valid_col = 0 <= move[1] < self.board.shape[1]
        empty_cell = self.board[move[0]][move[1]] == 0
        if valid_row and valid_col and empty_cell:
            return True
        return False
    
    def make_move(self): # -> (row, col)
        move = (int(input("Please make a move: ")), int(input("")))
        print(move)
        print(type(move))
        if self.is_valid(move):
                return move
        else:
            raise ValueError("incoreect random number! Try again mister AI!!!") # ? müsste eig. an den anfang von make move springen!


class Bot_simple(Player):

    def __init__(self, player_number, name, board) -> None:
        super().__init__(player_number, name, board)
        pass

    def make_move(self): # -> (row, col)
        # when all slots are empty, choose a random point on the grid
        #if not np.any(self.board):
        move = (random.randint(0, self.board.shape[0]-1),
                random.randint(0, self.board.shape[1]-1))
        # i the move is valid, return the move
        if self.is_valid(move):
            print(f"the move to be made is {move}")
            return move
        else:
            raise ValueError("incoreect random number! Try again mister AI!!!") # ? müsste eig. an den anfang von make move springen!

            
class Game():
    
    def __init__(self, m=6, n=7, k=4) -> None:
        self.m = m
        self.n = n
        self.k = k  
        pass

    def game_loop(self):
        arr = np.zeros((6, 7), dtype=int)
        while True:
            
            print(arr)

            arr[Player(1, "testing", arr).make_move()] = 1       

            print(arr)
            time.sleep(0)
        pass


current_game = Game()
current_game.game_loop()

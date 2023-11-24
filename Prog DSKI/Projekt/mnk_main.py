# imports
import numpy as np

class Game:
    
    def __init__(self, m, n, k, board, player1, player2):
        """_summary_:
        Board is filled with zeros
        player1 places 1
        player2 places 2

        Args:
            m (_type_): _description_
            n (_type_): _description_
            k (_type_): _description_
            board (_type_): _description_
            player1 (_type_): _description_
            player2 (_type_): _description_
        """
        self.m = m
        self.n = n
        self.k = k
        self.board = board
        self.player1 = player1
        self.player2 = player2

    def start():
        """_summary_
        """
        pass
    
    def has_won():
        """_summary_
        playerX has won when there is a k-long Pattern on the m x n board
        start checking for winning pattern after k moves
        
        checking process:
        - pick a placed move of the player that just went
        - check if surrounding 8 array cells have the same label
        - if not, next player
        - if there is an entry in a neighbor cell, follow the direction k times. if the
              
        """
        pass
    
    def game_loop(): #eigentliches gameplay
        """_summary_
        """
        pass


class Board:
    
    def __init__(self, m, n, k):
        """_summary_

        Args:
            m (_type_): _description_
            n (_type_): _description_
            k (_type_): _description_
        """
        self.m = m
        self.n = n
        self.k = k
        self.board = np.zeros(self.m, self.n)
        pass
    
    
    
    def display():
        """_summary_
        
        """
        pass
    
class Player:
    
    def __init__(self, name, player_number):
        """_summary_
        """
        self.name = name
        self.player_number = player_number 
        
    def make_move(self, board):
        """_summary_
        """
        
    
    def __init__(self, name, player_number):
        """_summary_

        Args:
            name (_type_): _description_
            player_number (_type_): _description_
        """
        self.name = name
        self.player_number = player_number
        
    def make_move(self, board):
        """_summary_

        Args:
            board (_type_): _description_
        """
        pass
        pass
    
class MyBot(Player):
    
    def __init__(self):
        """_summary_
        """
        pass
        
    def make_move(self, board): #überarbeiten im vergleich zu player
        """_summary_

        Args:
            board (_type_): _description_
        """
        pass
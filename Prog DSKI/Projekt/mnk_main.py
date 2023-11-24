# imports

class Game:
    
    def __init__(self, m, n, k, board, player1, player2):
        """_summary_

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
        pass
    
    def has_won():
        """_summary_
        """
        pass
    
    def display():
        """_summary_
        """
        pass
    
class Player:
    
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
    
    

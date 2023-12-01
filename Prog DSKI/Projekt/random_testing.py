import numpy as np


class Board():

    def __init__(self, m, n, k) -> None:
        self.m = m
        self.n = n
        self.k = k
        
        if self.m < self.k:
            raise ValueError("k can't be larger than n or m")
        elif self.n < self.k:
            raise ValueError("k can't be larger than n or m")
        else:
            self.array = np.zeros(shape=(self.m, self.n), dtype=int)
            return

    def display(self):
        print(self.array)
        pass

    def has_won(self): # -> 0, 1 oder 2
        pass

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
    


class Game():
    
    def __init__(self, m, n, k, player1="guest_1", player2="guest_2") -> None:
      self.m = m
      self.n = n
      self.k = k
      self.player1 = player1
      self.player2 = player2

      pass

    def start(self):
        # "Menü abfrage"
        # > choose player 1 -> player, bot_random, bot_not_random, bot_complex
        # > choose board size
        
        self.board = Board(self.m, self.n, self.k)

        pass
    
    def game_loop(self):
        self.board.display()
        

        pass


game_m = int(input())
game_n = int(input())
game_k = int(input())

current_game = Game(game_m, game_n, game_k)

current_game.start()
current_game.game_loop()
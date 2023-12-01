import numpy as np
import mnk_all_players as players
import mnk_board as brd

class Game():
    
    def __init__(self, m=6, n=7, k=4, player1="guest_1", player2="guest_2") -> None:
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
        
        self.board = brd.Board(self.m, self.n, self.k)

        pass
    
    def game_loop(self):
        self.board.display()
        

        pass


# game_m = int(input())
# game_n = int(input())
# game_k = int(input())
# current_game = Game(game_m, game_n, game_k)

current_game = Game()

current_game.start()
current_game.game_loop()
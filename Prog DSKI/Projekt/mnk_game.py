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

    def choose_player(p_number, p_name, choice):
        """"""
        if choice == 1:
            player = players.Player(p_number, p_name)
            print("player is human")
            print(20*"-")
            return player
        elif choice == 2:
            player = players.Bot_radom(p_number, p_name)
            print("player is a random bot")
            print(20*"-")
            return player
        elif choice == 3:
            player = players.Bot_not_random(p_number, p_name)
            print("player is not a random bot")
            print(20*"-")
            return player
        elif choice == 4:
            player = players.Bot_comples(p_number, p_name)
            print("player is a complex bot")
            print(20*"-")
            return player
        else:
            raise ValueError("input number out of range, please retry!")
    
    
    def start(self):
        # "Menü abfrage"

        # > choose board size
        self.m = int(input("gameboard height: "))
        self.n = int(input("gameboard width: "))
        self.k = int(input("winning lenght: "))
        print(20*"-")
        self.board = brd.Board(self.m, self.n, self.k)

        # > choose player 1 -> player, bot_random, bot_not_random, bot_complex
        print("\nplayer 1:")
        p1_name = str(input("input name: "))
        p1_choice = int(input("1 for human player | 2, 3, 4 for increasing bot difficulty: "))

        self.player1 = Game.choose_player(1, p1_name, p1_choice)

        p2_name = str(input("input name: "))
        p2_choice = int(input("1 for human player | 2, 3, 4 for increasing bot difficulty: "))

        self.player2 = Game.choose_player(2, p2_name, p2_choice)   
        pass
    
    def game_loop(self):
        self.board.display()
        

        pass

if __name__ == "__main__":
    # game_m = int(input())
    # game_n = int(input())
    # game_k = int(input())
    # current_game = Game(game_m, game_n, game_k)
    
    current_game = Game()
    
    current_game.start()
    current_game.game_loop()
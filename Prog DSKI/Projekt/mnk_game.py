import numpy as np
import mnk_all_players as players
import mnk_board as board
import random

class Game():
    
    def __init__(self, m=6, n=7, k=4, player1="guest_1", player2="guest_2") -> None:
      self.m = m
      self.n = n
      self.k = k
      self.player1 = player1
      self.player2 = player2

      pass

    def choose_player(p_number, p_name, choice):
        if choice == 1:
            player = players.Player(p_number, p_name, board)
            print("player is human")
            print(20*"-")
            return player
        elif choice == 2:
            player = players.Bot_random(p_number, p_name, board)
            print("player is a random bot")
            print(20*"-")
            return player
        elif choice == 3:
            player = players.Bot_simple(p_number, p_name, board)
            print("player is not a random bot")
            print(20*"-")
            return player
        elif choice == 4:
            player = players.Bot_complex(p_number, p_name, board)
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
        self.board = board.Board(self.m, self.n, self.k)

        # > choose player 1 -> player, bot_random, bot_not_random, bot_complex
        print("\nplayer 1:")
        p1_name = str(input("input name: "))
        p1_choice = int(input("1 for human player | 2, 3, 4 for increasing bot difficulty: "))

        self.player1 = Game.choose_player(1, p1_name, p1_choice)

        p2_name = str(input("input name: "))
        p2_choice = int(input("1 for human player | 2, 3, 4 for increasing bot difficulty: "))

        self.player2 = Game.choose_player(2, p2_name, p2_choice)   
        pass
    
    def full_board(self):
        # go through rows, check if values are 0 or not
        # if any are 0 return false
        # if not return True
        #made by Dalia
        print(self.board)
        # for row in enumerate(self.board):
            # for value in range(len(row)):

        # # for row in self.board:
            # # for value in row:
                # if value == 0:
                    # return False
        # return True  

    def game_loop(self):
        #made by Dalia
        current_player = random.choice([self.player1, self.player2])
        while not self.full_board() and not self.board.has_won(current_player):
            self.board.display() #oder irgendwas mit update oder so? 
            print(f"Player {current_player}'s turn")
            
            # problem! game loop weiss nicht welche class der current_player ist
            # synatx müsste sein: players.Player.make_move()
            # oder                players.Bot_random.make_move()
                # -> check which class player is
                # -> use its specific make_move
            # ALTERNATIVE? class make_move() an Player vererben (?)
        
            players.make_move(current_player)
            if current_player == self.player1:
                current_player = self.player2
            else:
                current_player = self.player1

        self.board.display()
        if self.board.has_won(self.player1):
            print("Player 1 wins!")
        elif self.board.has_won(self.player2):
            print("Player 2 wins!")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    # game_m = int(input())
    # game_n = int(input())
    # game_k = int(input())
    # current_game = Game(game_m, game_n, game_k)
    
    current_game = Game()
    
    current_game.start()
    current_game.game_loop()
import numpy as np
import random
import time


class Board():

    def __init__(self, m, n, k) -> None:
        self.m = m
        self.n = n
        self.k = k
        # check if zielgerade is larger than gameboard
        if self.m < self.k:
            raise ValueError("k can't be larger than n or m")
        elif self.n < self.k:
            raise ValueError("k can't be larger than n or m")
        else:
            self.board = np.zeros(shape=(self.m, self.n), dtype=int)
            return

    def display(self):
        print(self.board)
        pass

    def has_won(self, current_player):
        """_summary_
        playerX has won when there is a k-long Pattern on the m x n board
        start checking for winning pattern after k moves
        
        checking process:
        - pick a placed move of the player that just went
        - check if surrounding 8 array cells have the same label
        - if not, next player
        - if there is an entry in a neighbor cell, follow the direction k times. if the
              made by Dalia
        """
        self.current_player = current_player

        for x in self.board:
            count = 0
            for value in x:
                if value == self.current_player:
                    count += 1
                    if count == self.k:
                        return True
                else:
                    count = 0
        # und jetzt noch für columns und diagonal, könnte aber auch alles falsch sein, ich teste gerade nichts
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
                raise ValueError("incoreect random number! Try again mister AI!!!") # ? müsste eig. an den anfang von make move springen!

            

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


class Game():
    
    def __init__(self, m=6, n=7, k=4, player1="guest_1", player2="guest_2") -> None:
        self.m = m
        self.n = n
        self.k = k
        self.player1 = player1
        self.player2 = player2      
        pass

    def choose_player(self, p_number:int, p_name:str, choice:int):
        if choice == 1:
            player = Player(p_number, p_name, self.board)
            print("player is human")
            print(20*"-")
            return player
        elif choice == 2:
            player = Bot_random(p_number, p_name, self.board)
            print("player is a random bot")
            print(20*"-")
            return player
        elif choice == 3:
            player = Bot_simple(p_number, p_name, self.board)
            print("player is not a random bot")
            print(20*"-")
            return player
        elif choice == 4:
            player = Bot_complex(p_number, p_name, self.board)
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
        self.board = Board(self.m, self.n, self.k)
        print(20*"-")

        # > choose player 1 -> player, bot_random, bot_not_random, bot_complex
        print("player 1:")
        p1_name = str(input("input name: "))
        p1_choice = int(input("1 for human player | 2, 3, 4 for increasing bot difficulty: "))
        print(type(p1_name))
        print(type(p1_choice))
        self.player1 = Game.choose_player(self, 1, p1_name, p1_choice)

        p2_name = str(input("input name: "))
        p2_choice = int(input("1 for human player | 2, 3, 4 for increasing bot difficulty: "))

        self.player2 = Game.choose_player(self, 2, p2_name, p2_choice)   
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
            current_move = Bot_simple.make_move(current_player)
            # PROBLEM: ein hier muss eig. statt Player in player.Player.make_move()
            #          immer das stehen was für spieler 1 und 2 gewählt wurde
            #          ich weiss nicht wie man sowas macht. Mir fällt dazu auch nichts ein
            #          5
            
            print(current_move)

            self.board.board[current_move] = 1            
            
            if current_player == self.player1:
                current_player = self.player2
            else:
                current_player = self.player1
            
            time.sleep(5)

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
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

    def has_won(self, current_player, k):
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
        # check the rows
        for row in self.board:
            count = 0
        for cell in row:
            if cell == current_player:
                count += 1
                if count == k:
                    return True
            else:
                count = 0

        # check the columns
        for col in range(self.n):
            count = 0
            for row in self.board:
                if row[col] == current_player:
                    count += 1
                    if count == k:
                        return True
                else:
                    count = 0

        return False



class Player():

    def __init__(self, player_number, name, board) -> None: # player number 1 or 2
        self.name = name
        self.player_number = player_number
        self.board = board
    

    def is_valid(self, move:tuple):
        '''
        erhält ein tuple von moves
        prüft ob moves in valid raum ist
        gibt true or false wieder

        '''

        # checks if move is in range of the size of the board
        if move[0] < self.board.m and move[1] < self.board.n:
            print(self.board)
            # checks the cell that is to be changed is == 0
            if self.board.board[move[0]][move[1]] == 0:
                return True
        else:
            return False


    # !! man muss noch hinzufügen, dass wenn was anderes als ein int eingegeben wird man es nochmal machen soll. bisher kommt nur valueerror
    def make_move(self): # -> (row, col)
        print(f"make move between 0 and {self.board.m} \nand 0 and {self.board.n}")
        move = (int(input("Please make a move: ")), int(input("")))
        while not self.is_valid(move):
            print('Invalid move. Please try again')
            move = (int(input("Please make a move: ")), int(input("")))
        return move
            
            
class Bot_random(Player):

    def __init__(self, player_number, name, board) -> None:
        super().__init__(player_number, name, board)
        
        
    def make_move(self): # -> (row, col)
        """
        geht in eine schleife und wiederholt die erzeugung vom random move so lange bis es valid ist
        made by Dalia
        """
        
        realitycheck = True
        while realitycheck:
            move = (random.randint(0, self.board.m - 1), random.randint(0, self.board.n - 1))
            if self.is_valid(move):
                realitycheck = False
               # move = (random.randint(0, self.board.m - 1), random.randint(0, self.board.n - 1))
                self.board.board[move[0]][move[1]] = self.player_number
                return move
            else:
                print('Invalid move. Please try again')


class Bot_simple(Player):

    def __init__(self, player_number, name, board) -> None:
        super().__init__(player_number, name, board)
        
'''
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
'''
            

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

class Game():
    
    def __init__(self, m=6, n=7, k=4, player1=0, player2=0):
        self.m = m
        self.n = n
        self.k = k
        self.player1 = player1
        self.player2 = player2      


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
        self.k = int(input("winning length: "))
        self.board = Board(self.m, self.n, self.k)
        print(20*"-")

        # > choose player 1 -> player, bot_random, bot_not_random, bot_complex
        print("player 1:")
        p1_name = str(input("input name: "))
        p1_choice = int(input("1 for human player | 2, 3, 4 for increasing bot difficulty: "))
        self.player1 = Game.choose_player(self, 1, p1_name, p1_choice)

        p2_name = str(input("input name: "))
        p2_choice = int(input("1 for human player | 2, 3, 4 for increasing bot difficulty: "))
        self.player2 = Game.choose_player(self, 2, p2_name, p2_choice)   

    
    def full_board(self):
        #made by Dalia
        # goes through row and checks if value of every cell is 0
        for row in self.board.board:
            for value in row:
                if value == 0:
                    return False
        return True  

    def game_loop(self):
        #made by Dalia
        current_player = random.choice([self.player1, self.player2])
        while not self.full_board() and not self.board.has_won(current_player, self.k):
            self.board.display()
            print(f"Player {current_player.name}'s turn")
            # gets the current move the player inputed
            current_move = current_player.make_move()  
            print(current_move)
            
            # makes the move on the board
            self.board.board[current_move] = current_player.player_number
            
            # checks if someone has won and if the board is full
            if self.board.has_won(current_player.player_number, self.k):
                print(f"{current_player.player_number} wins!")
                break
            elif self.full_board():
                print('The board is full. Nobody won!')
                break
            
            # changes player 
            if current_player == self.player1:
                current_player = self.player2
            else:
                current_player = self.player1
                
            time.sleep(1)    
            
        self.board.display()

if __name__ == "__main__":
    # game_m = int(input())
    # game_n = int(input())
    # game_k = int(input())
    # current_game = Game(game_m, game_n, game_k)
    
    current_game = Game()
    
    current_game.start()
    current_game.game_loop()
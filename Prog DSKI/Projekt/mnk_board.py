import numpy as np


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
            self.array = np.zeros(shape=(self.m, self.n), dtype=int)
            return

    def display(self):
        print(self.array)
        pass

    def has_won(self):
        """_summary_
        playerX has won when there is a k-long Pattern on the m x n board
        start checking for winning pattern after k moves
        
        checking process:
        - pick a placed move of the player that just went
        - check if surrounding 8 array cells have the same label
        - if not, next player
        - if there is an entry in a neighbor cell, follow the direction k times. if the
              
        """
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


if __name__ == "__main__":
    # hier kommt zeug zum testen hin
    pass
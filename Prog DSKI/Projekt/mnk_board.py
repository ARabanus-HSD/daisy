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

    def has_won(self): # -> 0, 1 oder 2
        pass


if __name__ == "__main__":
    # hier kommt zeug zum testen hin
    pass
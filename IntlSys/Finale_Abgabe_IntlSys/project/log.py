import io
import os

class logToFile(io.IOBase):
    def __init__(self):
        pass

    def write(self, data):
        with open("logfile.txt", mode="a") as f:
            f.write(data)
        return len(data)

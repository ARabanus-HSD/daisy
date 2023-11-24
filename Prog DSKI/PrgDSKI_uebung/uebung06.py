import math
import random

# prep for A1
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, p):
        return (self.x == p.x) and (self.y == p.y)

class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, c):
        return self.radius == c.radius


# prep for A2

class Person:
    def __init__(self, name, mail, password):
        self.__name = name
        self.__mail = mail
        self.__check_password(password)
        self.__password = password
        self.__failed_attempts = 0
    
    def __check_password(self, password):
        assert len(password) >= 8, \
            "Password must have at least 8 characters"
    
    def get_name(self):
        return self.__name
    
    def get_mail(self, password):
        if self.__failed_attempts < 3:
            if self.__password == password:
                print(self.__mail)
                self.__failed_attempts = 0
            else:
                print("Password incorrect.")
                self.__failed_attempts += 1
        elif self.__failed_attempts > 2:
            print("Too many failes attempts :(")
        pass


######################################################################

# A1
a = Circle(5, -3, 2.5)
b = Circle(5, -3, 2.5)
print(a == b) # => True

a = Circle(5, -3, 2.5)
b = Circle(5, -3, 25.0)
print(a == b) # => False

# A2
p1 = Person("Monica", "m.thomson@gmail.com", "SuperSecret")

p1.get_mail("FirstGuess") # => Password incorrect.
p1.get_mail("SecondGuess") # => Password incorrect.
p1.get_mail("ThirdGuess") # => Password incorrect.
p1.get_mail("FourthGuess") # => Too many failed attempts.

p1 = Person("Monica", "m.thomson@gmail.com", "SuperSecret")

p1.get_mail("FirstGuess") # => Password incorrect.
p1.get_mail("SecondGuess") # => Password incorrect.
p1.get_mail("SuperSecret") # => m.thomson@gmail.com
p1.get_mail("FirstGuess") # => Password incorrect.
p1.get_mail("SecondGuess") # => Password incorrect.
p1.get_mail("ThirdGuess") # => Password incorrect.
p1.get_mail("SuperSecret") # => Too many failed attempts.

# commenting test
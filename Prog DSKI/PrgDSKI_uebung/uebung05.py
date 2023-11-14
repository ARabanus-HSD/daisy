# prep for A1

class SuperHero:
    def are_you_a_super_hero(self):
        print("No! I am just a regular person")
        pass

# prep for A2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other):
        if self.age < other.age:
            print(f"{other.name} is older than me")
        elif self.age > other.age:
            print(f"{other.name} is younger than me")
        else:
            print(f"{other.name} is the same age")

# prep for A3
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def position(self):
        print(self.x, self.y)
        return self.x, self.y

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.center = Point(x, y)


# A1
someone = SuperHero()
someone.are_you_a_super_hero() # => No! I am just a regular person
print()

# A2
person1 = Person("Sally", 77)
person2 = Person("Henry", 77)
person3 = Person("Pieter", 17)

person1.compare_age(person2) # => "Henry is the same age."
person1.compare_age(person3) # => "Pieter is younger than me."
person3.compare_age(person1) # => "Sally is older than me."
print()

# A3
circle_1 = Circle(x=2, y=3.5, radius=5.5)
print(circle_1.radius) # --> 5.5
circle_1.center.position() # --> 2 3.5
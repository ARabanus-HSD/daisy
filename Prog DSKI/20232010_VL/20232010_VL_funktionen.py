# # FUNCTIONS

# # EXAMPLE 1 ------------------------------------------------------------------

# def x_vs_y(x, y):
#     # compare two numbers
#     if x == y:
#         print(f"{x} = {y}")
#     elif x > y:
#         print(f"{x} > {y}")
#     else:
#         print(f"{x} < {y}")

# print(x_vs_y(5, 6))
# print(x_vs_y(5, 2))
# print(x_vs_y(5, 5))

# # EXAMPLE 2 ------------------------------------------------------------------

# def boxes_to_eggs(n_boxes, eggs_per_box=6): # default value defined in function parameters
    # return n_boxes * eggs_per_box

# # calling functions
# print(boxes_to_eggs(7)) # n_boxes, eggs_per_box
# print(boxes_to_eggs(5, eggs_per_box=12)) # select specific parameters that shouldn't be the default value

# EXAMPLE 3 ------------------------------------------------------------------

# name spaces
# lokaler geltungsbereich: innerhalb einer Funktion, kann von anderen lokalen namespaces nicht erreicht werden
# globaler geltungsbereich: können von jeder Funktion aufgerufen werden!
# 

# a=5
# b=9

# def something_to_do(a):
#     # global a # zieht sich aus dem global space in die lokale funktion, und verändert diesen
#     a = a * 2 # aus einem lokalen raum können globale variablen nicht verändert werden!
#     a = 1000 # diese variable überschreibt innerhalb der funktion den Wert für a, aber nicht global!
#     return a+b

# result = something_to_do(a)
# print(a, b, result)

# EXAMPLE 4 ------------------------------------------------------------------

# returns sind exit-punkte einer Funktion

def pick_smallest(a, b):
    if a > b:
        return b
    elif a < b:
        return a
    elif a == b: # das ist überflüssig, das macht python automatisch...
        return None


result = pick_smallest(7, 7)
print(result) # --> 6

# EXAMPLE 5 ------------------------------------------------------------------
# Special functions

# recursive Funktionen, meistens langsam, aber sollte man kenne

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
   
# lokale funkttionen (ähnlich wie lokale variablen) können nur innerhalb einer funktion aufgerufen werden

def greeting(name):
    def is_friend(name):
        friend_list = ["tom", "luis"]
        return name.lower() in friend_list
    
    if is_friend(name):
        print(f"HeyyyYYYasdkfjnsd {name}!, i got tea")
    else:
        print(f"Hello {name}")

greeting("Peter")
greeting("Tom")
# print(is_friend("Tom")) geht nicht, da is_friend eine lokale funktion
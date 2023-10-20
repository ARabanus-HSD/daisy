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

a=5
b=9

def something_to_do(a):
    # global a # zieht sich aus dem global space in die lokale funktion, und verändert diesen
    a = a * 2 # aus einem lokalen raum können globale variablen nicht verändert werden!
    a = 1000 # diese variable überschreibt innerhalb der funktion den Wert für a, aber nicht global!
    return a+b

result = something_to_do(a)
print(a, b, result)


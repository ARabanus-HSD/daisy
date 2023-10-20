# # functions

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

def boxes_to_eggs(n_boxes, eggs_per_box=6): # default value defined in function parameters
    return n_boxes * eggs_per_box

# calling functions
print(boxes_to_eggs(7)) # n_boxes, eggs_per_box
print(boxes_to_eggs(5, eggs_per_box=12)) # select specific parameters that shouldn't be the default value
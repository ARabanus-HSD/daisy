# # # ------------ PT 1 ------------ 

# # def low_plus_high(numbers: list) -> int:
# #     '''
# #     Hier ist ne nice erklärung für die Funktion!
# #     :param numbers: list
# #     :return: sum of low and high
# #     '''
# #     numbers.sort()
# #     return numbers[0] + numbers[-1]

# # # ------------ PT 2 ------------ 

# # def low_plus_high(numbers: list, min: int=0) -> int:
#     # '''
#     # Es soll ein Mindestwert mit default-Wert gesetzt gegeben und gesetzt werden
#     # Ist der kleinste Wert in der Liste kleiner als der Mindestwert, wird der Mindeswert benutzt
#     # :param numbers: list
#     # :param min: int
#     # :return: sum of (min or low) + high
#     # '''
#     # numbers.sort()
#     # if min >= numbers[0]:
#         # return numbers[-1] + min
#     # else:
#         # return numbers[-1] + numbers[0]

# # ------------ PT 2 ------------ 

# def low_plus_high(numbers: list, min: int=0) -> int:
#     '''
#     Es soll ein Mindestwert mit default-Wert gesetzt gegeben und gesetzt werden
#     Ist der kleinste Wert in der Liste kleiner als der Mindestwert, wird der Mindeswert benutzt
#     :param numbers: list
#     :param min: int
#     :return: sum of (min or low) + high
#     '''
#     numbers.sort()
#     def set_to_min(value, min):
#         """
#         Overkill function to return either lowest value in list or min value given
#         :param value: int lowest in list
#         """
#         print(value)
#         if value >= min:
#             print(value)
#             return value
#         else:
#             return min
        
#         # if value < min:
#         #     return min
#         # return value
        
#     high = numbers[-1]
#     summe = set_to_min(numbers[0], min) + high
#     return summe

# # my_numbers = [2, -1, 16, 2, 7]
# # print(low_plus_high(my_numbers, 10))

# # ------------ PT 3 ------------ 

# import random

# cards = ["Zehn", "Bube", "Dame", "Ass", "König"]

# print(random.choice(cards))
# random.shuffle(cards)
# print(cards)
# print(random.uniform(10, 20))

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Path to your PNG image
image_path = "berge.png"

# Load the PNG image using matplotlib.image.imread
img = mpimg.imread(image_path)

# Display the image using matplotlib.pyplot.imshow
plt.imshow(img)
plt.axis('off')  # Turn off axis numbers and ticks
plt.show()

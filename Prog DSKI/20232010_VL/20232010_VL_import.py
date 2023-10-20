# allgemeine benutztung von bibs
# Python Bibs sind einfache online verfügbarer Code
# Typischerweise enthalten Bibs nützliche Funktionen für bestimmte Zwecke

# EXTERNE BIBS --------------------------------------------------------------------------------------

# standart bibs aus python
# import math
# from math import pi as pie, sin as sinus_function

# print(pie)
# print(sinus_function(5))

# from random import randint

# x = randint(1, 10)
# print(x)

# INTERNE BIBS --------------------------------------------------------------------------------------

from interne_bib_dices import dices # diese .py datei muss im selben Ordner sein wie dieses Script

print(dices(100))
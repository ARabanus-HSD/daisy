# Anton Rabanus 954234

# gegeben/input
results_dice = [1, 5, 5, 2, 6, 2, 4, 2, 3, 6, 1, 2, 1, 6, 4, 5, 1, 1, 2, 6]
print("für 6.4: welche nth kleinste Zahl wird gesucht?")
nth_number_input = int(input())
# 6.1
# summiere wie oft eine 1 in der liste steht

anzahl_einsen = 0
# aus der vorlesung
for x in results_dice:
    if x == 1:
        anzahl_einsen = anzahl_einsen + 1

print(f"mit dem for loop wurden {anzahl_einsen} gewürfelte Einsen gefunden")

# alternativ...
alternative_zur_A1 = results_dice.count(1)

print(f"mit der .count funktion wurden {alternative_zur_A1} gewürfelte Einsen gefunden")

# 6.2
gesuchte_zahl = 3
a = results_dice.index(gesuchte_zahl)
a_offset = a + 1

print(f"Die erste {gesuchte_zahl} wurde an {a_offset}ter stelle gewürfelt, wenn man bei 1 anfängt zu zählen")

# 6.3
def multiply_two_largest(numbers):
    # sortiere die liste, und nehme die letzten 2 eintraete. multipliziere diese
    numbers.sort()
    largest_product = numbers[-1] * numbers[-2] # nehme letzte und vorletzte Zahl der Liste
    return numbers[-1], numbers[-2], largest_product # ausgabe ist ein tuple

multiplied = multiply_two_largest(results_dice)
print(f"Produkt der zwei groessten Zahlen: {multiplied[0]}, * {multiplied[1]} = {multiplied[2]}")

# 6.4
def nth_smallest(numbers, nth):
    numbers = list(set(numbers)) # Entfernt Duplikate aus der Liste 'numbers' durch Umwandlung in ein Set und zurück in eine Liste
    if nth <= len(numbers):
        return numbers[nth - 1]


x = nth_smallest(results_dice, nth_number_input)
print(f"die {nth_number_input} kleinste Zahlt ist {x}")
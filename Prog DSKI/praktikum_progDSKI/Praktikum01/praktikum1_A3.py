credit = 1000
debits = [1.1, 22.22, 333.333, 700] 
counter = 0

for i in debits:
    if i < credit:
        # siehe frage 2
        credit = credit - i
print(credit)
    
"""
Frage 1: Wenn wir mit credit = 1000 und debits = [1.1, 22.22, 333.333] starten, welchen
Wert hat credit nach beenden der for-Schleife?
> die Werte für Credit sind dann: 643.347

Frage 2: Wie können wir den Code verändern, so dass der Wert credit niemals kleiner Null wird?
> siehe for schleife
"""
# A2.1

credit = 1000
delta = 0.9999
counter = 0

while delta < credit:
    # ziehe delta von credit ab
    # solange bis kein delta aus credit gezogen werden kann
    # > hör auf bei | delta | > credit oder credit 
    # credit darf nicht negativ werden!
    credit = credit - delta
    
    # siehe dritte frage
    counter = counter + 1

print(f"remaining credit: {credit}, how often was delta subtracted: {counter}")

"""
Frage 1: Wenn wir mit credit = 1000 und delta = 0.9999 starten, welchen Wert hat credit nach
beenden der while-Schleife?
> console output: 0.09999999998206066

Frage 2: Bei welcher Art von Werten für credit und delta bekommen wir Probleme mit der
Ausführung des Programmes? (und: Warum?)
> für negative delta zahlen würde credit unendlich gross werden, die while Schleife läuft unendlich weiter.

Frage 3: Wie könnten wir die while-Schleife ergänzen, so dass wir zum Schluss auch ausgeben können
wie oft delta von credit entnommen wurde?
> siehe while schleife
"""

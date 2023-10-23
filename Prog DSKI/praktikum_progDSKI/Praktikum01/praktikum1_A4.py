"""
Du befindest dich in einem unbekannten, dunklen Raum...
Was machst du? a) Rufen b) Lichtschalter suchen c) Warten
>> b
Die Wände fühlen sind an wie aus Fels.
Nirgendwo ein Schalter!
Doch halt! Da ragt etwas aus der Wand heraus... ein metallischer Hebel.
a) Ich betätige den Hebel b) Ich suche lieber noch weiter
"""

import time
import random

# def funky_string(string):
#     for i in string:
#         time.sleep(0.1)
#         print(i, end="")

def fifty_fifty():
    return random.randrange(2)

def final_door():
    print("Du öffnest die Tür, spürst die Bergluft, fällst in den Bach und tauchst im Glanz des Wasserfalls.\n Am Ufer liegt ein versteckter Schatz, der deine Abenteuerlust belohnt.")
   
def line_split():
    for k in range(50):
        print("-", end="")
    print("\n")

my_break = False
    
# A4.1
# setting:
while True:
    if my_break:
        break
    line_split()
    print("Du befindest dich in einem unbekannten, dunklen Raum...")
    print("Was machst du? a) Rufen b) Lichtschalter suchen c) Warten")
    action_1 = input("")

    if action_1 == "a":
        line_split()
        print("Deine Stimme hallt im Raum, wie in einer Höhle. Es bleibt dunkel...")
        # wieder zu Schritt 1
    
    elif action_1 == "c":
        line_split()
        print("es bleibt dunkel, es herrscht totenstille...")
        for i in range(5):
            time.sleep(0.5) # eine sekunde pause
            print(".")
        print("da passiert wohl nichts...")
        # wieder zu Schritt 1

    while action_1 == "b":    
        line_split()
        print("""Die Wände fühlen sich an wie aus Fels. Nirgendwo ein Schalter! \n Doch halt! Da ragt etwas aus der Wand heraus... ein metallischer Hebel.""")
        print("a) Ich betätige den Hebel b) Ich suche lieber noch weiter")
        action_2 = input("")
        if action_2 == "a":
            line_split()
            print("Du sieht eine Fels Wand, mit einer eingelassenen Tür, und eine IKEA PLUTTIS Wanduhr an der rechten Wand.")
            print("Was machst du? a) Die Tür öffnen b) Erwartungsvoll auf die Uhr schauen")
            action_3 = input("")
            if action_3 == "a":
                final_door()
                my_break = True
                break
            elif action_3 == "b":
                line_split()
                print("Du siehst wie die Uhr tickt und tackt....")
                for j in range(5):
                    time.sleep(1)
                    print("tick")
                    time.sleep(1)
                    print("tack")
                print("Das Licht geht aus...")
                break
        elif action_2 == "b":
            chance = fifty_fifty()
            if chance == 0:
                line_split()
                print("Du hast leider nichts gefunden... vielleicht kannst du ja was anderes machen!")
            else:
                line_split()
                print("Du spürst eine eiserne Klinke einer schweren Tür")
                print("Was machst du? a) Die Türe öffnen b) Weitersuchen")
                action_4 = input("")
                if action_4 == "a":
                    final_door()
                    my_break = True
                    break
                elif action_4 == "b":
                    print("Leider findest du nichts...")
            
            

        
    # else:
    #     print("Ungültige Eingabe! Bitte nur a, b oder c eingeben ")

    
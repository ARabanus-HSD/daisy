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
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys


def reveal_string(input_string, delay=0.02):
    for char in input_string:
        sys.stdout.write(char)  # Write the character to the standard output
        sys.stdout.flush()  # Flush the output buffer to ensure immediate display
        time.sleep(delay)  # Introduce a delay before printing the next character
    print()

img_path = 'berge.png'

def fifty_fifty():
    return random.randrange(2)

def line_split():
    for k in range(50):
        print("-", end="")
    print("\n")

def image_shower():
    img = mpimg.imread(img_path)
    plt.figure(figsize=(1280, 720))
    plt.title("Du öffnest die Tür, spürst die Bergluft, fällst in den Bach und tauchst im Glanz des Wasserfalls.\n Am Ufer liegt ein versteckter Schatz, der deine Abenteuerlust belohnt.")
    plt.axis('off')  # Turn off axis numbers and ticks
    plt.imshow(img)


def final_door():

    line_split()
    reveal_string("Du drückst die Klinke, die Tür bleibt zu...")
    time.sleep(1)
    reveal_string("aus der Tür fährt ein kleines Numpad mit Display und folgender Schrift:")
    
    versuche = 3
    
    while versuche > 0:
        line_split()
        reveal_string(f"4 Stelligen Pin eingeben! NOCH {versuche} VERSUCHE")
        reveal_string("Was möchtest du tun? a) PIN eingeben b) Den Raum genauer anschauen")
        action_final_1 = input("")
    
        if action_final_1 == "a":
            code = input(f"4 Stelligen Pin eingeben! NOCH {versuche} VERSUCHE")
            if code == "1556":
                line_split()
                time.sleep(1)
                image_shower()
                break
            else:
                versuche = versuche - 1
        elif action_final_1 == "b":
            line_split()
            reveal_string("Was möchtest du dir genauer anschauen? a) die Wände b) die Uhr c) die Decke")
            action_final_2 = input("")
            if action_final_2 == "a":
                line_split()
                reveal_string("Du siehst an den Wänden 18846 kleine Löcher die du sofort alle perfekt gezählt hast")
                reveal_string("(auf einem kleinen Alu-Schild steht wie viele löcher es gibt)")
            elif action_final_2 == "b":
                line_split()
                reveal_string("es ist 4 minuten vor 4, Nachmittags")
            elif action_final_2 == "c":
                line_split()
                reveal_string("Du siehst an den Leuchtmittlen an der Decke viel zu viele Spinnen...")
                reveal_string("ekelhaft")
    line_split()
    reveal_string("GAME OVER")
    line_split()
    
    

my_break = False
    
# A4.1
# setting:
while True:
    if my_break:
        break
    line_split()
    reveal_string("Du befindest dich in einem unbekannten, dunklen Raum...")
    reveal_string("Was machst du? a) Rufen b) Lichtschalter suchen c) Warten")
    action_1 = input("")

    if action_1 == "a":
        line_split()
        reveal_string("Deine Stimme hallt im Raum, wie in einer Höhle. Es bleibt dunkel...")
        # wieder zu Schritt 1
    
    elif action_1 == "c":
        line_split()
        reveal_string("es bleibt dunkel, es herrscht totenstille...")
        for i in range(5):
            time.sleep(0.5) # eine sekunde pause
            print(".")
        reveal_string("da passiert wohl nichts...")
        # wieder zu Schritt 1

    while action_1 == "b":    
        line_split()
        reveal_string("""Die Wände fühlen sich an wie aus Fels. Nirgendwo ein Schalter! \n Doch halt! Da ragt etwas aus der Wand heraus... ein metallischer Hebel.""")
        reveal_string("a) Ich betätige den Hebel b) Ich suche lieber noch weiter")
        action_2 = input("")
        if action_2 == "a":
            line_split()
            reveal_string("Du sieht eine Fels Wand, mit einer eingelassenen Tür, und eine IKEA PLUTTIS Wanduhr an der rechten Wand.")
            reveal_string("Was machst du? a) Die Tür öffnen b) Erwartungsvoll auf die Uhr schauen")
            action_3 = input("")
            if action_3 == "a":
                final_door()
                my_break = True
                break
            elif action_3 == "b":
                line_split()
                reveal_string("Du siehst wie die Uhr, (5 Minuten vor 4, Nachmittags) tickt und tackt....")
                for j in range(5):
                    time.sleep(1)
                    print("tick")
                    time.sleep(1)
                    print("tack")
                reveal_string("Das Licht geht aus...")
                break
        elif action_2 == "b":
            chance = fifty_fifty()
            if chance == 0:
                line_split()
                reveal_string("Du hast leider nichts gefunden... vielleicht kannst du ja was anderes machen!")
            else:
                line_split()
                reveal_string("Du spürst eine eiserne Klinke einer schweren Tür")
                reveal_string("Was machst du? a) Die Türe öffnen b) Weitersuchen")
                action_4 = input("")
                if action_4 == "a":
                    final_door()
                    my_break = True
                    break
                elif action_4 == "b":
                    reveal_string("Leider findest du nichts...")
            
            

        
    # else:
    #     print("Ungültige Eingabe! Bitte nur a, b oder c eingeben ")

    
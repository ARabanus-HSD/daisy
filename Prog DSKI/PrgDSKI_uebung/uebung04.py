# es gibt die python lib 'duden', dafür braucht man Internet, das hab ich gerade nicht gehabt.
# deshalb hier ein Platzhalter dictionary 
mein_duden = ["apfel", "buch", "tisch", "haus", "stuhl", "auto", "fenster", "hund", "katze", "blume",
              "computer", "telefon", "wasser", "luft", "feuer", "erde", "sonne", "mond", "sterne", "regen",
              "schnee", "wind", "musik", "film", "schlecht", "farbe", "licht", "schatten", "wolke", "kaffee", "tee",
              "zucker", "salz", "brot", "käse", "messer", "gabel", "löffel", "teller", "topf", "pfanne",
              "kleid", "schuhe", "hut", "tasche", "uhr", "brille", "zahn", "auge", "ohr", "programm",
              "fernseher", "lampe", "telefon", "taschenlampe", "regenschirm", "tasse", "teppich", "sessel", "kissen", 
              "bett", "decke", "buchstabe", "zahl", "schlüssel", "schloss"]

# git push test

# C1
def caesar_encode(text: str, shift: int, alphabet="abcdefghijklmnopqrstuvwxyz") -> str:
    """
    This is a Caesar cipher.
     Each letter in a message is shifted by *shift*
    characters in the alphabet, and returned.
    text:
    A string you would like to encode or decode.
     Must consist of
    lowercase letters and spaces.
    shift:
    An integer, indicating how many positions in the alphabet each
    letter in the text will be shifted.
    alphabet:
    A string with all characters that should be shifted.
    """
    encoded_string = ""
    
    for char in text:
        if char in alphabet:
            shifted_char_index = (alphabet.index(char) + shift) % len(alphabet)
            shifted_char = alphabet[shifted_char_index ]
            encoded_string += shifted_char
        else:
            encoded_string += char
            pass
   
    return encoded_string


def decoding(encoded_text: str, alphabet="abcdefghijklmnopqrstuvwxyz") -> str:
    """
    iterate through length of alphabet for possible letter shifts to decode the message
    check if words are in duden, return string where words match!
    
    compares if words exsits, onlhy prints if they do
    """
    def real_word_check(word: str) -> bool:
        """
        Compares all "words" in decrypted string with german dictionary entries
        """
        try:
            
            if word in mein_duden:
                return True
            else:
                return False
        except Exception as e:
            print(f"Fehler beim Überprüfen des Worts '{word}': {e}")
            return False
    
    for i in range(len(alphabet)):
        decoded_text = caesar_encode(encoded_text, i, alphabet)
        decoded_words = decoded_text.split()
        for word in decoded_words:
            if real_word_check(word):
                return decoded_text
            else:
                pass

# A1 bis A3
if __name__ == "__main__":
    print(caesar_encode("mein text!", shift=15)) # -> btxc itmi!

    print(decoding("xri eztyk jtycvtyk wlvi uve rewrex.")) # -> gar nicht schlecht fuer den anfang.

    new_alphabet = "abcdefghijklmnopqrstuvwxyz .,!?äöü"
    print(decoding("k j?xebmj.btxww,nbvjwbxqwnby xp jvvbtj!vbn j,nwc", new_alphabet)) # -> bravo! das konnte man ohne programm kaum eraten.
import random as rnd

german_english_pairs = [("Name", "name"), 
                        ("Hochschule", "college"), 
                        ("Hörsaal", "lecture hall")]

# C1
# Dictionaries
ger_eng =  dict((ger, eng) for ger, eng in german_english_pairs)
eng_ger =  dict((eng, ger) for ger, eng in german_english_pairs)

print(ger_eng["Hörsaal"])
print(eng_ger["college"])

# C2

def roll_the_dice_v1(n_rolls: int):
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    
    result = [rnd.randint(1, 6) for x in range(n_rolls)]
    
    for i in range(len(result)):
        if result[i] == 1:
            ones = ones + 1
        elif result[i] == 2:
            twos = twos + 1
        elif result[i] == 3:
            threes = threes + 1
        elif result[i] == 4:
            fours = fours + 1
        elif result[i] == 5:
            fives = fives + 1
        elif result[i] == 6:
            sixes = sixes + 1
            
    roll_results_labels = [1, 2, 3, 4, 5, 6]
    roll_results = [ones, twos, threes, fours, fives, sixes]
    
    dice_roll_dict = dict(zip(roll_results_labels, roll_results))
    return dice_roll_dict

def roll_the_dice_v2(n_rolls: int):
    dice_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    
    for i in range(n_rolls):
        result = rnd.randint(1, 6)
        dice_dict[result] =+ 1
    
    return dice_dict

print(roll_the_dice_v1(1000))
print(roll_the_dice_v2(1000))


# C3

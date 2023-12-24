import random

# Rolls the dice
def roll_dices(amout_of_dices):
    dice_rolls = []
    for x in range(amout_of_dices):
        dice_roll = random.randint(1, 6)
        dice_rolls.append(dice_roll)
    return dice_rolls


# This runs every turn and determines how many dices are rolled and which are saved
def turn(dices):
    all_saved_dices = []

    for _ in range(3):
        dice_roll = roll_dices(dices - len(all_saved_dices))
        print(f'Your diceroll was {dice_roll}')
        saved_dices_list = save_dices(dice_roll)
        all_saved_dices += saved_dices_list

    print(f'All your saved dices were {all_saved_dices}')
    return all_saved_dices

# Saves dices selected by the player
def save_dices(dice_roll):
    saved_dices_list = []

    for value in dice_roll:
        while True:
            saved_dices = input(f"Do you want to save {value}? (y/n): ")

            if saved_dices.lower() == "y":
                saved_dices_list.append(value)
                break
            elif saved_dices.lower() == "n":
                break
            else:
                print("Invalid input")

    if not saved_dices_list:
        print("No dices were saved.")
    else:
        print(f"Dices {', '.join(map(str, saved_dices_list))} were saved")

    return saved_dices_list


# These check for conditions needed to write points to different slots

def check_ones(final_dices):
    count_of_ones = final_dices.count(1)
    ones_values = [item for item in final_dices if item == 1]
    return sum(ones_values)

def check_twos(final_dices):
    count_of_twos = final_dices.count(2)
    twos_values = [item for item in final_dices if item == 2]
    return sum(twos_values)

def check_threes(final_dices):
    count_of_threes = final_dices.count(3)
    threes_values = [item for item in final_dices if item == 3]
    return sum(threes_values)

def check_fours(final_dices):
    count_of_fours = final_dices.count(4)
    fours_values = [item for item in final_dices if item == 4]
    return sum(fours_values)

def check_fives(final_dices):
    count_of_fives = final_dices.count(5)
    fives_values = [item for item in final_dices if item == 5]
    return sum(fives_values)

def check_sixes(final_dices):
    count_of_sixes = final_dices.count(6)
    sixes_values = [item for item in final_dices if item == 6]
    return sum(sixes_values)

# Check for full house - 3 of same and 2 of same
def check_full_house(final_dices):
    for i in range(1, 7):
        if final_dices.count(i) == 3:
            for j in range(1, 7):
                if final_dices.count(j) == 2 and i != j:
                    return 25
    return 0
                    

# Check for three of a kind
def check_three_of_a_kind(final_dices):
    for i in range(1, 7):
        if final_dices.count(i) >= 3:
            return sum(dice for dice in final_dices if dice == i)
    return 0  

# Check for four of a kind
def check_four_of_a_kind(final_dices):
    for i in range(1, 7):
        if final_dices.count(i) >= 4:
            return sum(dice for dice in final_dices if dice == i)
    return 0  
    
# Check for chance
def check_chance(final_dices):
    return sum(final_dices)
    


# Check for small straight  - 4 consecuative values
def check_small_straight(final_dices):
    sorted_dices = sorted(set(final_dices))  
    valid_small_straights = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    
    for valid_sequence in valid_small_straights:
        if all(dice in sorted_dices for dice in valid_sequence):
            return 30  
    
    return 0  


# Check for large straight - 5 consecuative values 
def check_large_straight(final_dices):
    sorted_dices = sorted(set(final_dices))  
    valid_large_straights = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
    
    for valid_sequence in valid_large_straights:
        if all(dice in sorted_dices for dice in valid_sequence):
            return 40  
    
    return 0 

# Check for Yatzhee - All the same value
def check_yahtzee(final_dices):
    if len(final_dices) == 5 and all(item == final_dices[0] for item in final_dices[1:]):
        return 50 
    return 0

# This lets user choose which pointslot to fill out of those that fill the conditions
def update_score (final_dices):
        
    score = {
    "Ones" : 0,
    "Twos" : 0,
    "Threes" : 0,
    "Fours" : 0,
    "Fives" : 0,
    "Sixes" : 0,
    "Upper section bonus": 0,
    "Chance" : 0,
    "Three of a kind" : 0,
    "Four of a kind" : 0,
    "Full house" : 0,
    "Small straight" : 0,
    "Large straight" : 0,
    "Yatzhee" : 0
    }

    possible_score = {}


    if check_ones(final_dices) > 0 and score["Ones"] == 0:
        possible_score["Ones"] = check_ones(final_dices)

    if check_twos(final_dices) > 0 and score["Twos"] == 0:
        possible_score["Twos"] = check_twos(final_dices)

    if check_threes(final_dices) > 0 and score["Threes"] == 0:
        possible_score["Threes"] = check_threes(final_dices)

    if check_fours(final_dices) > 0 and score["Fours"] == 0:
        possible_score["Fours"] = check_fours(final_dices)

    if check_fives(final_dices) > 0 and score["Fives"] == 0:
        possible_score["Fives"] = check_fives(final_dices)

    if check_sixes(final_dices) > 0 and score["Sixes"] == 0:
        possible_score["Sixes"] = check_sixes(final_dices)

    if check_full_house(final_dices) > 0 and score["Full house"] == 0:
        possible_score["Full house"] = check_full_house(final_dices)

    if check_three_of_a_kind(final_dices) > 0 and score["Three of a kind"] == 0:
        possible_score["Three of a kind"] = check_three_of_a_kind(final_dices)

    if check_four_of_a_kind(final_dices) > 0 and score["Four of a kind"] == 0:
        possible_score["Four of a kind"] = check_four_of_a_kind(final_dices)

    if check_chance(final_dices) > 0 and score["Chance"] == 0:
        possible_score["Chance"] = check_chance(final_dices)

    if check_small_straight(final_dices) > 0 and score["Small straight"] == 0:
        possible_score["Small straight"] = check_small_straight(final_dices)
    
    if check_large_straight(final_dices) > 0 and score["Large straight"] == 0:
        possible_score["Large straight"] = check_large_straight(final_dices)

    if check_yahtzee(final_dices) > 0 and score["Yatzhee"] == 0:
        possible_score["Yatzhee"] = check_yahtzee(final_dices)

    while True:
        print(possible_score)
        get_user_choice = input("Choose which slot to fill: ")

        if get_user_choice in possible_score:
            score[get_user_choice] = possible_score[get_user_choice]
            break
        else:
            print("Invalid choice. Please choose a valid category.")

    return score

# Checks if 1-6 are all filled for bonus points - This is never going to happen when testing with 5 turns
def check_upper_section_bonus(score):
    if all(score[category] > 0 for category in ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]):
        score["Upper section bonus"] = 63
    return score

# prints to Highscore.txt - It needs to exist and will not be created by this because of time constraints 
def print_to_file(current_score):
    with open("Highscore.txt", "a") as file:
        highscore_name = input("Your name for the highscore? ")
        print(current_score)
        final_score = sum(current_score.values())
        file.write(f'{highscore_name}: {final_score}\n')

# This just prints the contents of the Highscore.txt file
def read_from_file():
    file_path = 'Highscore.txt'

    with open (file_path, 'r') as file:
        contents = file.read()
        print(contents)

# Main function and everything happens here
def main():
    turns = 5  # Number of turns in the game, tested with 5 but I think 13 is the real one
    dices = 5   # Number of dices in the game, don't touch scoring is not scaling based on these
    all_saved_dices = []

    current_score = {
    "Ones" : 0,
    "Twos" : 0,
    "Threes" : 0,
    "Fours" : 0,
    "Fives" : 0,
    "Sixes" : 0,
    "Upper section bonus": 0,
    "Chance" : 0,
    "Three of a kind" : 0,
    "Four of a kind" : 0,
    "Full house" : 0,
    "Small straight" : 0,
    "Large straight" : 0,
    "Yatzhee" : 0
    }

    # Turns happen in here
    for x in range(turns):
        x += 1
        all_saved_dices = turn(dices)
        updated_score = update_score(all_saved_dices)
        
        for category in current_score:
            current_score[category] += updated_score[category]
    
    # After the game is finished these run
    current_score = check_upper_section_bonus(current_score)
    print_to_file(current_score)
    print(25* "-")
    print("Highscore:")
    read_from_file()
    print(25* "-")
        
# Just calls the main function
main()

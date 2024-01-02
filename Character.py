
"""

Module containing the Character class

make equipment a subclass

"""

import mine_rescue_main as main
import text

class Character:
    
    def __init__(self, username, category, gender, hair_colour, hat, boots, equipment):
        
        self.username = username
        self.category = category
        self.gender = gender
        self.hair_colour = hair_colour
        self.hat = hat
        self.boots = boots
        self.equipment = equipment
        
        
    def __str__(self):
        return (f"\n{self.username},{self.category},{self.gender},{self.hair_colour},{self.hat},{self.boots},{self.equipment}")

    def create_character(username):
        text.Colour("\n\nYou'd better choose ya'll a character! Now let's see to that.\n").cyan()
        
        # Category selection
        while True:
            category_select = input(text.Colour('''Now, choose your type of character from the list:
Sherrif - "s"
Gunslinger - "g"
Cowgirl - "c"
Blacksmith - "b"
:''').input_cyan())

            category_select = category_select.lower().strip(" ")
            
            if category_select == "s":
                category = "sheriff"
                text.Colour("\n\nYou've chosen Sherrif!\n").cyan()
                break
            elif category_select == "g":
                category = "gunslinger"
                text.Colour("\n\nYou've chosen gunslinger!\n").cyan()
                break
            elif category_select == "b":
                category = "blacksmith"
                text.Colour("\n\nYou've chosen Blacksmith!\n").cyan()
                break
            elif category_select == "c":
                category = "cowgirl"
                text.Colour("\n\nYou've chosen Cowgirl!\n").cyan()
                break
            else:
                text.Colour("\n\nWhoa there, partner! That ain't somethin' y'all can pick.").red()

        # Gender selection
        while True:
            gender_select = input(text.Colour('''\nWhat gender are ya'll'?
Male - "m"
Female - "f"
Non-binary - "n"
Other - "o"
:''').input_cyan())

            gender_select = gender_select.lower().strip(" ")

            if gender_select == "m":
                gender = "male"
                text.Colour("\n\nDamn son!\n").cyan()
                break
            elif gender_select == "f":
                gender = "female"
                text.Colour("\n\nHowdy little lady!\n").cyan()
                break
            elif gender_select == "n":
                gender = "non-binary"
                text.Colour("\n\nWell, howdy partner!\n").cyan()
                break
            elif gender_select == "o":
                gender = "other"
                text.Colour("\n\nWell, howdy partner!\n").cyan()
                break
            else:
                text.Colour("\n\nWhoa there, partner! That ain't somethin' you can pick.\n").red()

        # Hair color selection
        while True:
            hair_colour_select = input(text.Colour(''''\nWhat's ya hair colour?
Brown - "br"
Blonde - "bl"
Black - "bk"
Red - "r"
Blue - "bu"
Purple - "p"
:''').input_cyan())
            
            hair_colour_select = hair_colour_select.lower().strip(" ")

            if hair_colour_select == "br":
                hair_colour = "brown"
                text.Colour("\n\nYa'll got brown hair!\n").cyan()
                break
            elif hair_colour_select == "bl":
                hair_colour = "blonde"
                text.Colour("\n\nYa'll got blonde hair!\n").cyan()
                break
            elif hair_colour_select == "bk":
                hair_colour = "black"
                text.Colour("\n\nYa'll got black hair!\n").cyan()
                break
            elif hair_colour_select == "r":
                hair_colour = "red"
                text.Colour("\n\nYa'll got red hair!\n").cyan()
                break
            elif hair_colour_select == "bu":
                hair_colour = "blue"
                text.Colour("\n\nYa'll got blue hair!\n").cyan()
                break
            elif hair_colour_select == "p":
                hair_colour = "purple"
                text.Colour("\n\nYa'll got purple hair!\n").cyan()
                break
            else:
                text.Colour("\n\nWhoa there, partner! That ain't somethin' you can pick.\n").red()

        # Hat selection
        while True:
            hat_select = input(text.Colour('''\nWhat colour hat it gon be?
Black hat - "bh"
Brown hat - "brh"
Cream hat - "ch"
Red hat - "rh"text.Colour
:''').input_cyan())
            
            hat_select = hat_select.lower().strip(" ")
            
            if hat_select == "bh":
                hat = "black hat"
                text.Colour("\n\nYa'll got a black hat!\n").cyan()
                break
            elif hat_select == "brh":
                hat = "brown hat"
                text.Colour("\n\nYa'll got a brown hat!\n").cyan()
                break
            elif hat_select == "ch":
                hat = "cream hat"
                text.Colour("\n\nYa'll got a cream hat!\n").cyan()
                break
            elif hat_select == "rh":
                hat = "red hat"
                text.Colour("\n\nYa'll got a red hat!\n").cyan()
                break
            else:
                text.Colour("\n\nWhoa there, partner! That ain't somethin' you can pick.\n").red()

        # Boots selection
        while True:
            boots_select = input(text.Colour('''\nWhat boots ya'll ride with?
Riding boots - "rb"
Work boots - "wb"
Fashion boots - "fb"
:''').input_cyan())
            
            boots_select = boots_select.lower().strip(" ")
            
            if boots_select == "rb":
                boots = "riding boots"
                text.Colour("\n\nYa'll got a riding boots!\n").cyan()
                break
            elif boots_select == "wb":
                boots = "work boots"
                text.Colour("\n\nYa'll got a work boots!\n").cyan()
                break
            elif boots_select == "fb":
                boots = "fashion boots"
                text.Colour("\n\nOoooh fancy! Ya'll got them fashion boots!\n").cyan()
                break
            else:
                text.Colour("\n\nWhoa there, partner! That ain't somethin' you can pick.\n").red()

        # Equipment selection
        while True:
            equipment_select = input(text.Colour('''\nWhat's ya choice of equipment?
Lasso - "l"
Notebook - "n"
Hammer - "h"
Mask - "m"
:''').input_cyan())
            
            equipment_select = equipment_select.lower().strip(" ")
            
            if equipment_select == "l":
                equipment = "lasso"
                text.Colour("\n\nNice choice fella! You picked the lasoo. I bet that'll come in handy.\n").cyan()
                break
            elif equipment_select == "g":
                equipment = "notebook"
                text.Colour("\n\nNice choice fella! You picked the notebook. I bet that'll come in handy.\n").cyan()
                break
            elif equipment_select == "h":
                equipment = "hammer"
                text.Colour("\n\nNice choice fella! You picked the hammer. I bet that'll come in handy.\n").cyan()
                break
            elif equipment_select == "m":
                equipment = "mask"
                text.Colour("\n\nNice choice fella! You picked the mask. I bet that'll come in handy.\n").cyan()
                break
            else:
                text.Colour("\n\nWhoa there, partner! That ain't somethin' you can pick.\n").red()
        
        # Create a new character instance
        new_character = Character(username, category, gender, hair_colour, hat, boots, equipment)
        
        # Write the character's information to file.
        
        with open('characters.txt', 'a') as char_file:
            
            char_file.write(f"{Character.__str__(new_character)},puzzle_one")
            char_file.close()
        
        # add custom message here!!
        text.Colour(f"\nCharacter created successfully! Welcome to the game, {username}. You're a {gender} {category} with {hair_colour} hair, a {hat}, {boots} and a {equipment}\n\n").cyan()
        
        
        main.load_progress(username)
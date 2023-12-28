
"""

Module containing the Character class

make equipment a subclass

"""

import mine_rescue_main as main

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
        return (f"{self.username},{self.category},{self.gender},{self.hair_colour},{self.hat},{self.boots},{self.equipment}")

    def create_character(username):
        print("\nYou'd better choose ya'll a character! Now let's see to that.\n")
        
        # Category selection
        while True:
            category_select = input('''Now, choose your type of character from the list:
Sherrif - "s"
Gunslinger - "g"
Cowgirl - "c"
Blacksmith - "b"
:
''')
            category_select = category_select.lower().strip(" ")
            
            if category_select == "s":
                category = "sheriff"
                print("\nYou've chosen Sherrif!\n")
                break
            elif category_select == "g":
                category = "gunslinger"
                print("\nYou've chosen gunslinger!\n")
                break
            elif category_select == "b":
                category = "blacksmith"
                print("\nYou've chosen Blacksmith!\n")
                break
            elif category_select == "c":
                category = "cowgirl"
                print("\nYou've chosen Cowgirl!\n")
                break
            else:
                print("Whoa there, partner! That ain't somethin' y'all can pick.")

        # Gender selection
        while True:
            gender_select = input('''\nWhat gender are ya'll'?
    Male - "m"
    Female - "f"
    Non-binary - "n"
    Other - "o"
    :
    ''')

            gender_select = gender_select.lower().strip(" ")

            if gender_select == "m":
                gender = "male"
                print("\nDamn son!\n")
                break
            elif gender_select == "f":
                gender = "female"
                print("\nHowdy little lady!\n")
                break
            elif gender_select == "n":
                gender = "non-binary"
                print("\nWell, howdy partner!\n")
                break
            elif gender_select == "o":
                gender = "other"
                print("\nWell, howdy partner!\n")
                break
            else:
                print("\nWhoa there, partner! That ain't somethin' you can pick.\n")

        # Hair color selection
        while True:
            hair_colour_select = input(''''\nWhat's ya hair colour?
    Brown - "br"
    Blonde - "bl"
    Black - "bk"
    Red - "r"
    Blue - "bu"
    Purple - "p"
    ''')
            
            hair_colour_select = hair_colour_select.lower().strip(" ")

            if hair_colour_select == "br":
                hair_colour = "brown"
                print("\nYa'll got brown hair!\n")
                break
            elif hair_colour_select == "bl":
                hair_colour = "blonde"
                print("\nYa'll got blonde hair!\n")
                break
            elif hair_colour_select == "bk":
                hair_colour = "black"
                print("\nYa'll got black hair!\n")
                break
            elif hair_colour_select == "r":
                hair_colour = "red"
                print("\nYa'll got red hair!\n")
                break
            elif hair_colour_select == "bu":
                hair_colour = "blue"
                print("\nYa'll got blue hair!\n")
                break
            elif hair_colour_select == "p":
                hair_colour = "purple"
                print("\nYa'll got purple hair!\n")
                break
            else:
                print("\nWhoa there, partner! That ain't somethin' you can pick.\n")

        # Hat selection
        while True:
            hat_select = input('''\nWhat colour hat it gon be?
    Black hat - "bh"
    Brown hat - "brh"
    Cream hat - "ch"
    Red hat - "rh"
    ''')
            
            hat_select = hat_select.lower().strip(" ")
            
            if hat_select == "bh":
                hat = "black hat"
                print("\nYa'll got a black hat!\n")
                break
            elif hat_select == "brh":
                hat = "brown hat"
                print("\nYa'll got a brown hat!\n")
                break
            elif hat_select == "ch":
                hat = "cream hat"
                print("\nYa'll got a cream hat!\n")
                break
            elif hat_select == "rh":
                hat = "red hat"
                print("\nYa'll got a red hat!\n")
                break
            else:
                print("\nWhoa there, partner! That ain't somethin' you can pick.\n")

        # Boots selection
        while True:
            boots_select = input('''\nWhat boots ya'll ride with?
    Riding boots - "rb"
    Work boots - "wb"
    Fashion boots - "fb"
    ''')
            
            boots_select = boots_select.lower().strip(" ")
            
            if boots_select == "rb":
                boots = "riding boots"
                print("\nYa'll got a riding boots!\n")
                break
            elif boots_select == "wb":
                boots = "work boots"
                print("\nYa'll got a work boots!\n")
                break
            elif boots_select == "fb":
                boots = "fashion boots"
                print("\nOoooh fancy! Ya'll got them fashion boots!\n")
                break
            else:
                print("\nWhoa there, partner! That ain't somethin' you can pick.\n")

        # Equipment selection
        while True:
            equipment_select = input('''\nWhat's ya choice of equipment?
    Lasso - "l"
    Notebook - "n"
    Hammer - "h"
    Mask - "m"
    ''')
            
            equipment_select = equipment_select.lower().strip(" ")
            
            if equipment_select == "l":
                equipment = "lasso"
                print("\nNice choice fella! You picked the lasoo. I bet that'll come in handy.\n")
                break
            elif equipment_select == "g":
                equipment = "notebook"
                print("\nNice choice fella! You picked the notebook. I bet that'll come in handy.\n")
                break
            elif equipment_select == "h":
                equipment = "hammer"
                print("\nNice choice fella! You picked the hammer. I bet that'll come in handy.\n")
                break
            elif equipment_select == "m":
                equipment = "mask"
                print("\nNice choice fella! You picked the mask. I bet that'll come in handy.\n")
                break
            else:
                print("\nWhoa there, partner! That ain't somethin' you can pick.\n")
        
        # Create a new character instance
        new_character = Character(username, category, gender, hair_colour, hat, boots, equipment)
        
        # Write the character's information to file.
        
        with open('characters.txt', 'a') as char_file:
            
            char_file.write(f"{Character.__str__(new_character)},puzzle_one\n")
            char_file.close()
        
        # add custom message here!!
        print(f"\nCharacter created successfully! Welcome to the game, {username}. You're a {gender} {category} with {hair_colour} hair, a {hat}, {boots} and a {equipment}\n\n")
        
        
        main.load_progress(username)
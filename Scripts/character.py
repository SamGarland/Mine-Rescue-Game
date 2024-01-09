'''
This is the character module with the Character class and methods.
These are used to create and save a character to: "characters.txt" in Resources.

'''
#==== Imports ====#

import mine_rescue_main as main
import text

#==== Class and methods ====#

class Character:
    
    # Constructor
    def __init__(self, username, category, gender, hair_colour, hat, boots, equipment):
        
        self.username = username
        self.category = category
        self.gender = gender
        self.hair_colour = hair_colour
        self.hat = hat
        self.boots = boots
        self.equipment = equipment
    
    # Self string.
    def __str__(self):
        return (f"{self.username},{self.category},{self.gender},{self.hair_colour},{self.hat},{self.boots},{self.equipment}")
    
    # Method for creating and saving character.
    def create_character(username):
        text.Typed.typed_text("\n\nYou'd better choose ya'll a character! Now let's see to that.\n")
        
        # Category selection.
        while True:
            category_select = input('''Now, choose your type of character from the list:
Sherrif - s
Gunslinger - g
Cowgirl - c
Blacksmith - b
:''')

            category_select = category_select.lower().strip(" ")
            
            if category_select == "s":
                category = "sheriff"
                text.Typed.typed_text("\n\nYou've chosen Sherrif!\n")
                break
            elif category_select == "g":
                category = "gunslinger"
                text.Typed.typed_text("\n\nYou've chosen gunslinger!\n")
                break
            elif category_select == "b":
                category = "blacksmith"
                text.Typed.typed_text("\n\nYou've chosen Blacksmith!\n")
                break
            elif category_select == "c":
                category = "cowgirl"
                text.Typed.typed_text("\n\nYou've chosen Cowgirl!\n")
                break
            else:
                text.Colour("\n\nWhoa there, partner! That ain't somethin' y'all can pick.").red()

        # Gender selection.
        while True:
            gender_select = input('''\nWhat gender are ya'll?
Male - m
Female - f
Non-binary - n
Other - o
:''')

            gender_select = gender_select.lower().strip(" ")

            if gender_select == "m":
                gender = "male"
                text.Typed.typed_text("\n\nDamn son!\n")
                break
            elif gender_select == "f":
                gender = "female"
                text.Typed.typed_text("\n\nHowdy mam!\n")
                break
            elif gender_select == "n":
                gender = "non-binary"
                text.Typed.typed_text("\n\nWell, howdy partner!\n")
                break
            elif gender_select == "o":
                gender = "other"
                text.Typed.typed_text("\n\nWell, howdy partner!\n")
                break
            else:
                text.Colour("\n\nWhoa there, partner! That ain't somethin' you can pick.\n").red()

        # Hair color selection.
        while True:
            hair_colour_select = input('''\nWhat's ya hair colour?
Brown - br
Blonde - bl
Black - bk
Red - r
Blue - bu
Purple - p
:''')
            
            hair_colour_select = hair_colour_select.lower().strip(" ")

            if hair_colour_select == "br":
                hair_colour = "brown"
                text.Typed.typed_text("\n\nYa'll got brown hair!\n")
                break
            elif hair_colour_select == "bl":
                hair_colour = "blonde"
                text.Typed.typed_text("\n\nYa'll got blonde hair!\n")
                break
            elif hair_colour_select == "bk":
                hair_colour = "black"
                text.Typed.typed_text("\n\nYa'll got black hair!\n")
                break
            elif hair_colour_select == "r":
                hair_colour = "red"
                text.Typed.typed_text("\n\nYa'll got red hair!\n")
                break
            elif hair_colour_select == "bu":
                hair_colour = "blue"
                text.Typed.typed_text("\n\nYa'll got blue hair!\n")
                break
            elif hair_colour_select == "p":
                hair_colour = "purple"
                text.Typed.typed_text("\n\nYa'll got purple hair!\n")
                break
            else:
                text.Colour("\n\nWhoa there, partner! That ain't somethin' you can pick.\n").red()

        # Hat selection.
        while True:
            hat_select = input('''\nWhat colour hat it gon be?
Black hat - b
Brown hat - br
Cream hat - c
Red hat - r
:''')
            
            hat_select = hat_select.lower().strip(" ")
            
            if hat_select == "b":
                hat = "black hat"
                text.Typed.typed_text("\n\nYa'll got a black hat!\n")
                break
            elif hat_select == "br":
                hat = "brown hat"
                text.Typed.typed_text("\n\nYa'll got a brown hat!\n")
                break
            elif hat_select == "c":
                hat = "cream hat"
                text.Typed.typed_text("\n\nYa'll got a cream hat!\n")
                break
            elif hat_select == "r":
                hat = "red hat"
                text.Typed.typed_text("\n\nYa'll got a red hat!\n")
                break
            else:
                text.Colour("\n\nWhoa there, partner! That ain't somethin' you can pick.\n").red()

        # Boots selection.
        while True:
            boots_select = input('''\nWhat boots ya'll ride with?
Riding boots - r
Work boots - w
Fashion boots - f
:''')
            
            boots_select = boots_select.lower().strip(" ")
            
            if boots_select == "r":
                boots = "riding boots"
                text.Typed.typed_text("\n\nYa'll got riding boots!\n")
                break
            elif boots_select == "w":
                boots = "work boots"
                text.Typed.typed_text("\n\nYa'll got work boots!\n")
                break
            elif boots_select == "f":
                boots = "fashion boots"
                text.Typed.typed_text("\n\nOoooh fancy! Ya'll got them fashion boots!\n")
                break
            else:
                text.Colour("\n\nWhoa there, partner! That ain't somethin' you can pick.\n").red()

        # Equipment selection.
        while True:
            equipment_select = input('''\nWhat's ya choice of equipment? Remember, you can swap equipment for hints, so look around in the game to pick up more equipment!
Lasso - l
Notebook - n
Hammer - h 
Mask - m
:''')
            
            equipment_select = equipment_select.lower().strip(" ")
            
            if equipment_select == "l":
                equipment = "lasso"
                text.Typed.typed_text("\n\nNice choice fella! You picked the lasso. I bet that'll come in handy.\n")
                break
            elif equipment_select == "n":
                equipment = "notebook"
                text.Typed.typed_text("\n\nNice choice fella! You picked the notebook. I bet that'll come in handy.\n")
                break
            elif equipment_select == "h":
                equipment = "hammer"
                text.Typed.typed_text("\n\nNice choice fella! You picked the hammer. I bet that'll come in handy.\n")
                break
            elif equipment_select == "m":
                equipment = "mask"
                text.Typed.typed_text("\n\nNice choice fella! You picked the mask. I bet that'll come in handy.\n")
                break
            else:
                text.Colour("\n\nWhoa there, partner! That ain't somethin' you can pick.\n").red()
        
        # Create a new character instance.
        new_character = Character(username, category, gender, hair_colour, hat, boots, equipment)
        
        # Write the character's information to file.
        with open("../Resources/characters.txt", "a") as char_file:
            
            char_file.write(f"{Character.__str__(new_character)},puzzle_one\n")
            char_file.close()
        
        # Gameplay message.
        text.Typed.typed_text(f"\nCharacter created successfully! Welcome to the game, {username}. You're a {gender} {category} with {hair_colour} hair, a {hat}, {boots} and a {equipment}.\n\n")
        # Load game with new character.
        main.load_progress(username)
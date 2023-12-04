'''
 ===== This programme is for MUD Game CW 2 APP PROG sem 1 =====

FILES REQUIRED :
    - "users.txt" - this takes and saves username and password as: username, password per line.
    - "characters.txt" - this takes username, character info and equipment.
    - "leaderboard.txt" - this takes username and puzzle timestamps (positions and timestamp aggregations can be worked out later)
    
CLASSES:
    
    -character:
        
        -self.name
        -self.category
        -self.gender
        -self.hair_colour
        -self.hat
        -self.boots
        -self.equipment
        
        a bunch of methods:
            - load_progress()
            - save_progress()
            - character_stats()

FUNCTIONS:
    
    -register_user(username, password)
    -login(username, password)
    -load_progress(username)
    -create_character(username)
    -save_progress(username)
    -show_leaderboard()
    -puzzle_one()
    -puzzle_two()
    -puzzle_three()
    -puzzle_four()
    -puzzle_five()
    
'''

#===== CLASSES =====#

class Character():
    
    def __init__(self, name, category, gender, hair_colour, hat, boots, equipment):
        
        self._name = name
        self._category = category
        self._gender = gender
        self._hair_colour = hair_colour
        self._hat = hat
        self._boots = boots
        self._equipment = equipment
        
        
    def __str__(self):
        return (f"{self._name},{self._category},{self._gender},{self._hair_colour},{self._hat},{self._boots},{self._equipment}")

    
    

#===== FUNCTIONS =====#


def register_user():
    
    # This function allows the user to register by entering a username and password into
    # "user.txt".
    
    with open("users.txt", "r+") as f:
         
         new_username = ""
         usernames = []
         user_exists = True
         
         for line in f:
             line = line.split(", ")
             if line:
                 usernames.append(line[0])
         
         while user_exists:
              new_username = input("\nGive me your name of choice friend:\n")
              if new_username in usernames:
                 print("\nWell dang! That name is taken...Have another go.\n")
              else:
                  user_exists = False
                  continue
              
         while True:
              new_password = input("\nWhat password y'all gona use? Shhhh, keep this a secret!\n")
              confirm_password = input("\nTell me one more time:\n")
              if new_password != confirm_password:
                  print("\nSorry, no matcheroo...\n")
                  continue
              else:
                  print("\nWelcome partner! That's all been taken care of for you!\n")
                  f.write(f"{new_username}, {new_password}\n")
                  break
    f.close()
    
    print("\nNow have a go at logging-in and we'll make sure everything is hunky-dorey!\n")
    login()


def login():
    
    # This function allows the user to login by taking a username and password stored in "users.txt"  
    # and compares them with a username and password entered by the user.
    
    f = open("users.txt", "r")
    
    authenticated = False
    
    lines = f.readlines()
    
    while authenticated == False:
        
        username = input("\nHowdy! Enter your username partner:\n")
        username = username.lower().strip(" ")
        password = input("\nHowdy! Enter your password partner:\n")
        password = password.lower().strip(" ")
        
        
        for line in lines:
            
            line = line.strip("\n").split(", ")
            
            if username == line[0] and password == line[1]:
                authenticated = True
            else:
                continue
    
        if authenticated == True:
            print("\nThat's right my friend!\n\nWelcome to the game!")
        else:
            print("\nSorry partner! Have another go...")
                
    f.close()
    load_progress(username)
    
def load_progress(username):
    # Check for character
    with open('characters.txt', 'r') as char_file:
        lines = char_file.readlines()

    character_found = False
    for line in lines:
        if username == line.strip().split(',')[0]:
            character_found = True

            # If found, check for current puzzle
            current_puzzle = line.strip().split(',')[-1]
            print(f"Howdy {username.title()}! Time to get ya back to {current_puzzle}, the miners aint wait'n forever")

            # Redirect to respective puzzle based on current_puzzle value
            if current_puzzle == "puzzle_one":
                puzzle_one()
            elif current_puzzle == "puzzle_two":
                puzzle_two()
            # Add remaining puzzles
            break

    if not character_found:
        print("\nWell well, we ain't got no record of ya partner. Time to saddle up and create yer character!")
        create_character(username)


def create_character(new_username):
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
Lasso - 'l'
Gun - 'g'
Hammer - 'h'
Mask - 'm'
''')
        
        equipment_select = equipment_select.lower().strip(" ")
        
        if equipment_select == "l":
            equipment = "lasso"
            print("\nNice choice fella! You picked the lasoo. I bet that'll come in handy.\n")
            break
        elif equipment_select == "g":
            equipment = "gun"
            print("\nNice choice fella! You picked the gun. I bet that'll come in handy.\n")
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
    new_character = Character(new_username, category, gender, hair_colour, hat, boots, equipment)
    
    # Write the character's information to file.
    
    with open('characters.txt', 'a') as char_file:
        
        char_file.write(f"{new_character},puzzle_one")
        char_file.close()
    
    # add custom message here!!
    print(f"\nCharacter created successfully! Welcome to the game, {new_username, category, gender, hair_colour, hat, boots, equipment}")
    
    
    load_progress(new_username)
    

def puzzle_one():
    print("\nAlright, here's your first challenge:")
    answer = input("What is the capital of England? ").lower().strip()
    
    # Check if the answer is correct
    if answer == "london":
        print("Correct! London is the capital of itself. You're moving on to the next challenge!")
        return True
    else:
        print("Oops! That's not quite right. Try again!")
        return False

def puzzle_two():
    print("\nHere comes your second challenge:")
    answer = input("What is the capital of Japan? ").lower().strip()
    
    # Check if the answer is correct
    if answer == "tokyo":
        print("Correct! Tokyo is indeed the capital of Japan. You're doing great!")
        return True
    else:
        print("That's not the right answer. Give it another shot!")
        return False


#==== Main execution file =====

if __name__ == "__main__":

#===== Start Menu =====#

# This menu allows users to either register, login or exit the game. 
    
    while True:
        
        user_selection = input('''\nNow what are you wanting to do partner?
    Register - "r"
    Login - "l"\n''')
    
        user_selection = user_selection.lower().strip(" ")
        
        if user_selection == "r":
            
           register_user()
           break
        
        elif user_selection == "l": 
            
            login()
            break
            
        else:
            print("\nDo'ya know what? I don't understand a thang you just said... Have another go!\n")
            continue


#===== Gameplay Conditional =====#



'''- This function takes username and checks "character.txt" to find puzzle_no.

if username not in "character.txt"
    create_character(username)
    this uses the character class to create a new character and saves it to 
    "character.txt" with default puzzle_one
elif username in "character.txt":
    load_character(username)
    this loads character stats from "character.txt" in a readable way
    and takes user to saved puzzle. 
    it also loads timestamp progress. '''
 
'''
while True:
    
    if user_character[puzzle] == "puzzle_one":
    
        pass
        puzzle_one() 
        at the end of puzzle_one: 
            - save progress to character.txt as puzzle_two and 
            take away any equipment used
            - update "leaderboard.txt"
            - load_progress()
            
    elif user_character[puzzle] == "puzzle_two":
        
       puzzle_two() 
        at the end of puzzle_two: 
            - save progress to character.txt as puzzle_three and 
            take away any equipment used
            - update "leaderboard.txt"
            - load_progress()
    
    elif user_character[puzzle] == "puzzle_three":
    
       puzzle_three() 
        at the end of puzzle_three: 
            - save progress to character.txt as puzzle_four and 
            take away any equipment used
            - update "leaderboard.txt"
            - load_progress()
        
    elif user_character[puzzle] == "puzzle_four":
    
        puzzle_four() 
        at the end of puzzle_four: 
            - save progress to character.txt as puzzle_five and 
            take away any equipment used
            - update "leaderboard.txt"
            - load_progress()
    
    elif user_character[puzzle] == "puzzle_five":
    
       puzzle_five() 
        at the end of puzzle_five: 
            - save progress to character.txt as puzzles_finished and 
            take away any equipment used
            - update "leaderboard.txt"
            - load_leaderboard()
            break and print leaving statement
    
    elif user_character[puzzle] == "puzzles_finished":
        print("You've already finished the game partner. Want to try again?")
    
    else:
        print("My sincerest condolences partner, we are having trouble loading your progress. Let's try again.")
        load_progress(username)

'''

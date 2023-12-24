"""
This is the puzzle class.

"""
import random
import time
from Avatar import Avatar
import mine_rescue_main

class Puzzle:
    def __init__(self, username):
        self.username = username
        self.avatar = Avatar()

# Show player inventory to check for equipment
    def get_inventory_item(self):
        with open('characters.txt', 'r') as char_file:
            for line in char_file:
                line_parts = line.strip().split(',')
                if line_parts[0].strip() == self.username:
                    return line_parts[-2].strip()
        # Return a default message if no item is found
        return "No item found"
    
# Check if the user has the required item
    def has_required_epuipment(self, required_item):
           
           return required_item in self.get_inventory_item()

    # Set the equipment to default "None" once it's been used in a puzzle
    def update_equipment(self):
        new_lines = []
        user_found = False
    
        with open('characters.txt', 'r') as char_file:
            lines = char_file.readlines()
    
        # Update equipment
        for line in lines:
            parts = line.strip().split(',')
            if parts[0].strip() == self.username:
                parts[-2] = "None"  # Assumes equipment is second to last item in the list
                user_found = True
            new_lines.append(','.join(parts))
    
        # Write updated if user found
        if user_found:
            with open('characters.txt', 'w') as char_file:
                for line in new_lines:
                    char_file.write(line + '\n')
        else:
            print(f"'{self.username}' not found in file")


#Function for puzzle_one to shift text   
    def caesar_cipher(self, text, shift):
        result = ""
        lowercase = 'abcdefghijklmnopqrstuvwxyz'
        uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        for char in text:
            if char.islower():
                index = lowercase.index(char)
                shifted_index = (index + shift) % 26
                result += lowercase[shifted_index]
            elif char.isupper():
                index = uppercase.index(char)
                shifted_index = (index + shift) % 26
                result += uppercase[shifted_index]
            else:
                result += char
            
        return result

#First Puzzle - Decode the writing
    def puzzle_one(self):
        print(f"Whoa there, who's that fella running at you from the entrace of the mine {self.username.title()}?\n")
        time.sleep(2)
        print("A mine worker runs up to you speaking an unknown language.\n")
        # Use Avatar class for intro speech
        print(f"He babbles: '{self.avatar.get_intro('railwayman')}'\n")
        time.sleep(2)
        print("He then hand you a piece of paper with words on it and point towards the mine\n")
        time.sleep(2)
                
        original_sentence = "To make your way into the tunnel, you\'re going to need to get on a MINECART"
        answer = "minecart"

        while True:
            shift = random.randint(1, 25)  # Random shift value
            ciphered_text = self.caesar_cipher(original_sentence, shift)
            print(f"The writing says:'{ciphered_text}'\n")
            
            user_input = input("Looks like you gotta make some sense of this and figure out the key word\nEnter the key:").strip().lower()
            
            if user_input == answer:
                print(f"\nWell done {self.username.title()}! You found the way.\n")
                mine_rescue_main.save_progress(self.username)
                mine_rescue_main.load_progress(self.username)
                return True
            else:
                print("Oh dust!, the writing changed?!")

#Second Puzzle - Railway Expansion
    def puzzle_two(self):
        print("As you mosey along the rusty old railway, you hear someone shouting at you to stop. Who's that dusty man?\n")
        time.sleep(2)
        # Use Avatar class for intro speech
        print(f"A railwayman runs up to you and says:'{self.avatar.get_intro('railwayman_two')}'\n")
        time.sleep(2)
        
        # Set the required item for the puzzle
        puzzle_two_item = "hammer"
        
        # Pompting for a hint
        print(f"'{self.avatar.get_prompt('railwayman_two')}'\n")
        while True: 
            choice = input("yes = 'y', no = 'n', check inventory = 'ci'\n").lower().strip()
        
            if choice == "y":
                if self.has_required_epuipment(puzzle_two_item):
                    print(f"{self.avatar.get_hint('railwayman_two')}")
                    self.update_equipment()
                    break
                else:
                    print("Now now, No need to tell a lie my friend, I see you ain't got no hammer")
                    break
            elif choice == "n":
                print("Oh riddens, that hammer sure would've been handy\n")
                break
            elif choice == "ci":
                print(f"Your equipment: {self.get_inventory_item()}")
                continue
            else:
                print("That aint a choice, you gotta say yes = 'y', no = 'n', check inventory = 'ci'")
        
        #Puzzle Logic
        while True:
            answer = input("\nWhat's the height of the arch at the center of the railway track? Enter your answer in centimetres: ")

            try:
                answer = int(answer)
                if answer == 708 or answer == 709:
                    print(f"\nYou've only gone and done it {self.username.title()}, seems our cart is about a metre long so we'll make it over\n")
                    mine_rescue_main.save_progress(self.username)
                    mine_rescue_main.load_progress(self.username)
                    return True
                else:
                    print("\nHmm, that don't seem quite right, have another go eh?")
            except ValueError:
                print("\nNow now, enter a number, not some gibberish you fool!") #if input is not an integer prompt to retry


#Third Puzzle - Break the links
    def puzzle_three(self):
        print(f"Oh no {self.username.title()}! The tunnel ahead has collapsed, that's the end of this track.")
        time.sleep(2)
        print("There's just a narrow crawl space left, and on the other side, there's a miner hollerin' at ya")
        time.sleep(2)
        # Use Avatar class for intro speech
        print(f"A railwayman runs up to you and says:\n'{self.avatar.get_intro('miner_one')}'\n")
        time.sleep(2)

        puzzle_three_item = "lasso"
        
        # Pompting for a hint
        print(f"'{self.avatar.get_prompt('miner_one')}'\n")
        while True: 
            choice = input("yes = 'y', no = 'n', check inventory = 'ci'\n").lower().strip()
        
            if choice == "y":
                if self.has_required_epuipment(puzzle_three_item):
                    print(f"{self.avatar.get_hint('miner_one', self.username)}")
                    self.update_equipment()
                    break
                else:
                    print("Now now partner, don't ya go yankin my strings, I see no lasso in sight!")
                    break
            elif choice == "n":
                print("I sure could've given you a 'and if you had a lasso my friend\n")
                break
            elif choice == "ci":
                print(f"Your equipment: {self.get_inventory_item()}")
                continue
            else:
                print("That aint a choice, you gotta say yes = 'y', no = 'n', check inventory = 'ci'")
        
        #Puzzle Logic
        while True:
            try:
                user_input = input("\nThink hard and enter the minimum number of breaks needed to fix this chain: \n").strip()
                
                number_of_breaks = int(user_input)
                
                if number_of_breaks == 4:
                    print(f"\nAin't you a clever one {self.username.title()}! You're sharper than a prick on a cactus! Only 4 breaks are needed.")
                    print("The miner swiftly breaks the links, joins the chain, and pulls you through the space\n")
                    #Save progress and move to next puzzle
                    mine_rescue_main.save_progress(self.username)
                    mine_rescue_main.load_progress(self.username)
                    return True
                else:
                    print("\nNope, that ain't it. You gotta think like you're spendin' links, not silver dollars. Try again.")
            except ValueError as e:
                print(f"There was an error in the value: {e}")
            except Exception as e:
                print(f"There was an unknown error: {e}")

#Fourth Puzzle - Cross the lake
    def puzzle_four(self):
        print(f"Howdy {self.username.title()}! You've just gotten to an underground lake. That smells funny....")
        time.sleep(1)
        print("Is that gas?! Y'all gotta find a way out")
        time.sleep(1)
        print("There's a rickety old boat, a jittery old miner, some unstable dynamite, and a sneaky rat!")
        time.sleep(1)
        print("You gotta get em all across to the other side before the whole place floods!\n")        
        time.sleep(1)
        # Use Avatar class for intro speech
        print(f"The jittery miner stumbled to you and says:\n{self.avatar.get_intro('miner_two')}\n")
        time.sleep(1)
        
        puzzle_four_item = "mask"
        
        print("Your actions are:\n"
              "  A - Take Rat Across\n"
              "  B - Take Dynamite Across\n"
              "  C - Take Miner Across\n"
              "  D - Take Nothing Across\n")
        
        # Pompting for a hint
        print(f"'{self.avatar.get_prompt('miner_two')}'\n")
        while True: 
            choice = input("yes = 'y', no = 'n', check inventory = 'ci'\n").lower().strip()
        
            if choice == "y":
                if self.has_required_epuipment(puzzle_four_item):
                    print(f"{self.avatar.get_hint('miner_two', self.username)}")
                    self.update_equipment()
                    break
                else:
                    print("Tryna pull a fast one on me eh? Only mask i see's yar blatant lie!")
                    break
            elif choice == "n":
                print("No mask eh? Guess you gotta figure it out ya self\n")
                break
            elif choice == "ci":
                print(f"Your equipment: {self.get_inventory_item()}")
                continue
            else:
                print("That aint a choice, you gotta say yes = 'y', no = 'n', check inventory = 'ci'")
        

        # Puzzle Logic
        valid_choices = ['A', 'B', 'C', 'D']
        solution = "BDABCDB"  # The correct sequence of actions
        
        while True:
            try:
                player_input = input("\nChoose yer action in the right order: e.g. ABCABCD\n").upper().strip()
        
                # Validate each character
                input_valid = True
                for char in player_input:
                    if char not in valid_choices:
                        print("That ain't a valid choice, partner. Pick A, B, C, or D.")
                        input_valid = False
                        break
        
                if input_valid == False:
                    continue  # Get new input if any character is invalid
        
                # Check input length
                if len(player_input) != len(solution):
                    print("That don't sound quite right, we ain't got forever")
                    continue  # Get new input if length is incorrect
        
                # Check if the input is in the correct order
                if player_input == solution:
                    print(f"\nYeehaw! Ya did it {self.username.title()}! All safe and sound on t'other side")
                    # Save progress and move to next puzzle
                    mine_rescue_main.save_progress(self.username)
                    mine_rescue_main.load_progress(self.username)
                    break
                else:
                    print("\nThat's not quite it, The gas is risin' think fast!")
        
            except Exception as e:
                print(f"There was an unknown error: {e}")
        
    def puzzle_five(self):
        print("Intro To Puzzle")
        print(f"Avatar Speech:{self.avatar.get_intro('AVATAR_NAME')}\n")
        print(f"Avatar Hint:{self.avatar.get_hint('AVATAR_NAME', self.username)}")
        #Game Logic
        
        
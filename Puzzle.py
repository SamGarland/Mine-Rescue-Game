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
    
        for line in lines:
            parts = line.strip().split(',')
            if parts[0].strip() == self.username:
                parts[-2] = "None"
                user_found = True
            new_lines.append(','.join(parts))
    
        if user_found:
            with open('characters.txt', 'w') as char_file:
                for line in new_lines:
                    char_file.write(line + '\n')
            print(f"Equipment updated for '{self.username}'.")
        else:
            print(f"'{self.username}' not found in character.txt")

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
        print(f"He babbles '{self.avatar.get_intro('railwayman')}'\n")
        time.sleep(2)
        print("He then hand you a piece of paper with words on it and point towards the mine\n")
        time.sleep(2)
                
        original_sentence = "To make your way into the tunnel, you\'re going to need to get on a MINECART"
        answer = "minecart"

        while True:
            shift = random.randint(1, 25)  # Random shift value
            ciphered_text = self.caesar_cipher(original_sentence, shift)
            print(f"The writing says:'{ciphered_text}'")
            
            user_input = input("Looks like you gotta make some sense of this and figure out the key word\nEnter the key:").strip().lower()
            
            if user_input == answer:
                print(f"Well done {self.username.title()}! You found the way.")
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
        print(f"A railwayman runs up to you and says:{self.avatar.get_intro('railwayman_two')}\n")
        time.sleep(2)
        # Set the required item for the puzzle
        puzzle_two_item = "hammer"
        
        print("I might be able to give you a hand, Y'all got a hammer?\n")
        while True: 
            choice = input("yes = 'y', no = 'n', check inventory = 'ci'\n").lower().strip()
        
            if choice == "y":
                if self.has_required_epuipment(puzzle_two_item):
                    print(f"{self.avatar.get_hint('railwayman_two', self.username)}")
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

        while True:
            answer = input("\nWhat's the height of the arch at the center of the railway track? Enter your answer in centimetres: ")

            try:
                answer = int(answer)
                if answer == 708 or answer == 709:
                    print(f"You've only gone and done it {self.username.title()}, seems our cart is about a metre long so we'll make it over")
                    mine_rescue_main.save_progress(self.username)
                    mine_rescue_main.load_progress(self.username)
                    return True
                else:
                    print("\nHmm, that don't seem quite right, have another go eh?")
            except ValueError:
                print("\nNow now, enter a number, not some gibberish you fool!") #if input is not an integer prompt to retry


#Third Puzzle - Break the links
#When item not found:
#    Now now partner, don't ya go yankin my strings, I see no lasso in sight!


#Fourth Puzzle - Cross the lake
#When item not found:
#    Tryna pull a fast one on me eh? Only mask i see's yar blatant lie

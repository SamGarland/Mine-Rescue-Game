import text

#==== Class and methods ====#

class Inventory:
    
    # Constructor.
    def __init__(self, username):
        self.username = username

    # Method to return player inventory.

    def get_inventory_item(self):
        with open("../../resources/characters.txt", "r") as char_file:
            for line in char_file:
                line_parts = line.strip().split(',')
                if line_parts[0].strip() == self.username:
                    item_list = line_parts[6:-1]
                    return item_list
        char_file.close()
                           
        # Returns a default message if no item is found.
        return "No item found"
    
    # Method to check if the user has the required equipment.

    def has_required_equipment(self, required_item):
           
            if required_item in self.get_inventory_item():
                print(required_item)
            else:
                print(None)
    
    # Method to show equipmemnt from inventory to player in gameplay.

    def show_player_inventory(self):
        
        inventory = self.get_inventory_item()
            
        for item in inventory:
            text.Colour(f"\n{item}").green()
        print("\n\n")
            
    # Method to remove equipment or set the equipment to default "None" if all has been used.

    def update_equipment(self, item):
        new_lines = []
        user_found = False
        
        with open("../../resources/characters.txt", "r") as char_file:
            lines = char_file.readlines()

            for line in lines:
                line = line.strip().split(',')
                # Check for user.
                if line[0] != self.username:
                    new_lines.append(",".join(line))
                elif line[0] == self.username:
                    # Update equipment.
                    item_list = self.get_inventory_item()
                    if (len(item_list) == 1) and (item in item_list):
                        item_list = "None"
                        mod_line = f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]},{line[5]},{item_list},{line[-1]}"
                        new_lines.append(mod_line)
                        user_found = True
                    elif len(item_list) > 1 and item in item_list:
                        item_list.remove(item)
                        item_str = ",".join(item_list)
                        mod_line = f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]},{line[5]},{item_str},{line[-1]}"
                        new_lines.append(mod_line)
                        user_found = True
                
        # File updated if user found.
        if user_found:
            with open("../../resources/characters.txt", "w") as char_file:
                for line in new_lines:
                    char_file.write(line + '\n')
            
            char_file.close()

    # Method to add new equipment in the character file.

    def pickup_equipment(self, item):
        
        new_lines = []
        user_found = False
        
        with open("../../resources/characters.txt", "r") as char_file:
            lines = char_file.readlines()

            for line in lines:
                line = line.strip().split(',')
                #Check for user.
                if line[0] != self.username:
                    new_lines.append(",".join(line))
                elif line[0] == self.username:
                    # Add equipment
                    item_list = self.get_inventory_item()
                    item_list.append(item)
                    if "None" in item_list:
                        item_list.remove("None")
                    item_str = ",".join(item_list)
                    mod_line = f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]},{line[5]},{item_str},{line[-1]}"
                    new_lines.append(mod_line)
                    user_found = True
                
        # File updated if user found.
        if user_found:
            with open("../../resources/characters.txt", "w") as char_file:
                for line in new_lines:
                    char_file.write(line + '\n')
            
            char_file.close()

#Inventory("Demo").show_player_inventory()
#Inventory("Demo").pickup_equipment("notebook")



import time
import text
import inventory

#==== Class and methods ====#

class Location:
    
    # Constructor.
    def __init__(self, username, puzzle, gender, hair_colour, hat, boots):
        self.username = username
        self.puzzle = puzzle
        self.gender = gender
        self.hair_colour = hair_colour
        self.hat = hat
        self.boots = boots
    
    # Method to show location menu.
    
    def get_loc_info(self):
        
        while True:
            user_input = input(text.Colour('''\n\nGive me a description of where I'm at - w
Look right - r
Look left - l
Look up - u
Look down - d
Back to the puzzle - e
:''').input_cyan())
            user_input.strip()
            
            if user_input == "w":
                Location(self.username, self.puzzle, self.gender, self.hair_colour, self.hat, self.boots).description()
            elif user_input == "r":
                Location(self.username, self.puzzle, self.gender, self.hair_colour, self.hat, self.boots).look_right()
            elif user_input == "l":
                Location(self.username, self.puzzle, self.gender, self.hair_colour, self.hat, self.boots).look_left()
            elif user_input == "u":
                Location(self.username, self.puzzle, self.gender, self.hair_colour, self.hat, self.boots).look_up()
            elif user_input == "d":
                Location(self.username, self.puzzle, self.gender, self.hair_colour, self.hat, self.boots).look_down()
            elif user_input == "e":
                break
            else:
                text.Colour("\nI'm not sure what you entered there, but it aint one of the options!\n").red()
    
    def look_down(self):
        #try:
        if self.puzzle == "puzzle_one":
            text.Colour("\nNothing much around here on the floor. Just a bunch of dust bits of old oily rag...\n").cyan()
            time.sleep(1)
            text.Colour("\nOh my! Looks like someone dropped their notebook!\n").cyan()
            time.sleep(2)
            equip = input(text.Colour("\n\nYa'll wana add it to your inventory?\nYes - y\nNo - n\n:").input_cyan())
            time.sleep(2)
            equip = equip.lower().strip(" ")
            if equip == "y":
                # Check equipment for notebook.
                if inventory.Inventory(self.username).has_required_equipment("notebook"):
                    text.Colour("\nNow now, I see you already got a notebook!\n\nNo need for another one...\n").cyan()
                    time.sleep(1)
                else:
                    # Add notebook to inventory.
                    inventory.Inventory(self.username).pickup_equipment("notebook")
                    text.Colour("\nYa'll picked-up a notebook! Yeeehaaaww!\n").cyan()
                    time.sleep(1)
            elif equip == "n":
                # Reject equipment.
                text.Colour("\nWhy that could'a come in handy! Ah well, I guess we don't wana be carrying too much stuff around...\n\n").cyan()
            else:
                text.Colour("\nThat aint a choice my friend...Try again.\n\n").red()
        elif self.puzzle == "puzzle_two":
            text.Colour("\nThere's bits of track all over the place.\n").cyan()
            time.sleep(2)
            text.Colour("Amazing they don't get more accidents in here...\n").cyan()
            time.sleep(2)
        elif self.puzzle == "puzzle_three":
            # Use of the Player's Boots
            text.Colour(f"\nYep, jus my {self.boots}...\n").cyan() #TODO 3
            time.sleep(2)
            text.Colour("I can't see much in here.\n").cyan()
            time.sleep(2)
        elif self.puzzle == "puzzle_four":
            # Use of the Player's Boots
            text.Colour(f"\nAw man! My {self.boots} are all wet...\n").cyan() #TODO 4
            time.sleep(2)
        elif self.puzzle == "puzzle_five":
            text.Colour("\nThere's loads of bits of wire all over the floor... What in the name happened here?\n").cyan()
            time.sleep(2)
            text.Colour("I bet that panel will give us a clue or two. Better get over there!\n").cyan()
            time.sleep(2)
        else:
            text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()
       # except:
        #    text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()

Location("Demo","puzzle_one","non-binary","purple","red hat","fashion boots").look_down()
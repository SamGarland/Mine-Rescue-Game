'''
This is the inventory module with Inventory class and methods.
These are used to check "characters.txt" for equipment, and
updating the inventory by removing or adding equipment.

'''
#==== Imports ====#

import text

#==== Class and methods ====#

class Inventory:
    
    # Constructor.
    def __init__(self, username):
        self.username = username

    # Method to return player inventory.

    def get_inventory_item(self):
        with open("../resources/characters.txt", "r") as char_file:
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
                return required_item
    
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
        
        with open("../resources/characters.txt", "r") as char_file:
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
            with open("../resources/characters.txt", "w") as char_file:
                for line in new_lines:
                    char_file.write(line + '\n')

    # Method to add new equipment in the character file.

    def pickup_equipment(self, item):
        
        new_lines = []
        user_found = False
        
        with open("../resources/characters.txt", "r") as char_file:
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
            with open("../resources/characters.txt", "w") as char_file:
                for line in new_lines:
                    char_file.write(line + '\n')
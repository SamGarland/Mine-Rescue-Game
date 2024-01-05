"""
inventory module with inventory class and methods.

"""

class Inventory:
    
    def __init__(self, username):
        self.username = username

#==== Show player inventory to check for equipment ====#

    def get_inventory_item(self):
        with open('characters.txt', 'r') as char_file:
            for line in char_file:
                line_parts = line.strip().split(',')
                if line_parts[0].strip() == self.username:
                    item_list = line_parts[6:-1]
                    return item_list
                    
        # Return a default message if no item is found
        return "No item found"
    
#==== Check if the user has the required item ====#

    def has_required_epuipment(self, required_item):
           
            if required_item in self.get_inventory_item():
                return required_item
            

#==== Remove equipment or set the equipment to default "None" if all has been used ====#

    def update_equipment(self, item):
        new_lines = []
        user_found = False
        
        with open('characters.txt', 'r') as char_file:
            lines = char_file.readlines()
    
            # Update equipment
            for line in lines:
                line = line.strip().split(',')
                
                if line[0] != self.username:
                    new_lines.append(",".join(line))
                elif line[0] == self.username:
                    item_list = self.get_inventory_item()
                    if (len(item_list) == 1) and (item in item_list):
                        item_list = "None"  # Equipment is second to last item in the list
                        mod_line = f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]},{line[5]},{item_list},{line[-1]}"
                        new_lines.append(mod_line)
                        user_found = True
                    elif len(item_list) > 1 and item in item_list:
                        item_list.remove(item)
                        item_str = ",".join(item_list)
                        mod_line = f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]},{line[5]},{item_str},{line[-1]}"
                        new_lines.append(mod_line)
                        user_found = True
                
            # Write updated if user found
        if user_found:
            with open('characters.txt', 'w') as char_file:
                for line in new_lines:
                    char_file.write(line + '\n')

#==== Add new equipment in the character file ====#

    def pickup_equipment(self, item):
        
        new_lines = []
        user_found = False
        
        with open('characters.txt', 'r') as char_file:
            lines = char_file.readlines()
    
            # Update equipment
            for line in lines:
                line = line.strip().split(',')
                
                if line[0] != self.username:
                    new_lines.append(",".join(line))
                elif line[0] == self.username:
                    item_list = self.get_inventory_item()
                    item_list.append(item)
                    if "None" in item_list:
                        item_list.remove("None")
                    item_str = ",".join(item_list)
                    mod_line = f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]},{line[5]},{item_str},{line[-1]}"
                    new_lines.append(mod_line)
                    user_found = True
                
            # Write updated if user found
        if user_found:
            with open('characters.txt', 'w') as char_file:
                for line in new_lines:
                    char_file.write(line + '\n')
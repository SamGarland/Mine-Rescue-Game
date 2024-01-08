"""
This is the location module with Location class and methods.
These allow the player to 'look around' their environment. 
They also allow the player to collect extra equipment. 

"""
#==== Imports ====#

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
            user_input = input(text.Colour('''\n\nGive me a description of where I'm at - "w"
Look right - "r"
Look left - "l"
Look up - "u"
Look down - "d"
Back to the puzzle - "e"
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
    
    # Method to give general location description.
    
    def description(self):
        # This takes the puzzle name and returns a brief description of the location.
        try:
            if self.puzzle == "puzzle_one":
                # Use of the Player's Gender
                text.Colour(f"\nYa'll at the entrance to the Lower Creek Gold Mine. Heard they got a lot of {self.gender} folk work'n here. Damn, it's hot out here!\n").cyan() #TODO 1
                time.sleep(2)
                text.Colour("Have a looky around and see if there's anything that might come in handy...\n").cyan()
                time.sleep(2)
            elif self.puzzle == "puzzle_two":
                # Use of the Player's Hair Colour
                text.Colour(f"\nYou're inside the mine, heading down the railway track, hot air blowing at ya {self.hair_colour} hair. Boy, it's a loooong way!\n").cyan() #TODO 2
                time.sleep(2)
                text.Colour("There's someone approaching. Quickly, go see what they want. Maybe they can help figure out what's going on in here...\n").cyan()
                time.sleep(2)
            elif self.puzzle == "puzzle_three":
                text.Colour("\nIt's getting tight in here partner.\n").cyan()
                time.sleep(2)
                # Use of the Player's Hair Colour
                text.Colour(f"Damn, I can hardly breathe! My {self.hair_colour} hair is getting all sweaty\n").cyan() #TODO 3
                time.sleep(2)
                text.Colour("Cough! Cough!\n").cyan()
                time.sleep(2)
                text.Colour("Sorry, about that. Looks like there's a collapsed tunnel up ahead.\n").cyan()
                time.sleep(2)
                text.Colour("Hell, look! There's light on the other side!\nGo see if there's anyone there...\n").cyan()
            elif self.puzzle == "puzzle_four":
                text.Colour("\nIt's some kind of underground lake. Maybe it's a flooded cavern?\n").cyan()
                time.sleep(2)
                text.Colour("Oh my lord, it smells baaaad in here!\n").cyan()
                time.sleep(2)
                text.Colour("I think this tunnel is leaking gas partner. Better stick that mask on!\n").cyan()
                time.sleep(2)
                text.Colour("Hey look! There's a fella crouching over there in the shadows. Let's see what he wants...\n").cyan()
            elif self.puzzle == "puzzle_five":
                text.Colour("\nThis must be it! I can hear the miners!").cyan()
                time.sleep(2)
                text.Colour("They're trapped in the lift shaft. Go over to the panel and see if you can figure out how to get it up and running again...\n").cyan()
                time.sleep(2)
            else:
                text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()
        except:
            text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()
    
    # Method allowing player to look right.
    
    def look_right(self):
        try:
            if self.puzzle == "puzzle_one":
                text.Colour("\nThat big building is the pump house. That pumps all the water out of the mine, so it don't get too dangerous down there.\n").cyan()
                time.sleep(2)
            elif self.puzzle == "puzzle_two":
                text.Colour("\nThe tracks are mighty wide in here.\n").cyan()
                time.sleep(2)
                text.Colour(f"Looks like there are about six or seven different lines. I wonder which one I need to take?\n").cyan()
                time.sleep(2)
                # Use of the Player's Hat
                text.Colour(f"Maybe you can toss my {self.hat} and see where it goes!\n").cyan() #TODO 2
                time.sleep(2)
                text.Colour("\nHey look! There's a lasso there on the wall!\n").cyan()
                time.sleep(2)
                equip = input(text.Colour("\n\nYa'll wana add it to your inventory?\nYes - \"y\"\nNo - \"n\"\n:").input_cyan())
                time.sleep(2)
                equip = equip.lower().strip(" ")
                if equip == "y":
                    # Check equipment for lasso.
                    if inventory.Inventory(self.username).has_required_epuipment("lasso"):
                        text.Colour("\nNow now, I see you already got a lasso!\n\nNo need for another one...\n").cyan()
                        time.sleep(1)
                    else:
                        # Add lasso to inventory.
                        inventory.Inventory(self.username).pickup_equipment("lasso")
                        text.Colour("\nYa'll picked-up a lasso! Yeeehaaaww!\n").cyan()
                        time.sleep(1)
                elif equip == "n":
                    # Reject equipment.
                    text.Colour("\nWhy that could'a come in handy! Ah well, I guess we don't wana be carrying too much stuff around...\n\n").cyan()
            elif self.puzzle == "puzzle_three":
                text.Colour("\nI can't see much over there.\nJust a couple ol' oil lamps and some crates.\n").cyan()
                time.sleep(2)
            elif self.puzzle == "puzzle_four":
                text.Colour("\nWow! This place is huge!\n").cyan()
                time.sleep(2)
                text.Colour("I wonder what happens if I shout:\n").cyan()
                time.sleep(1)
                text.Colour("ECHO!\n").cyan()
                time.sleep(1)
                text.Colour("echo...\n").cyan()
                time.sleep(1)
                text.Colour("echo...\n").cyan()
                time.sleep(1)
            elif self.puzzle == "puzzle_five":
                text.Colour("\nThere's the panel! Looks kind of rusty and old, but maybe you can figure something out...\n").cyan()
                time.sleep(2)
                # Use of the Player's Hat
                text.Colour(f"Ahah! Take off that {self.hat} and look on the wall there!\n\n[Written on the wall] (98 - 7) ...+, -, 6, 5, 4, 3, 2, 1... = 100...?\n").cyan() #TODO 5
                time.sleep(2)
                text.Colour("Them must be the notes that they's talking bout!").cyan()
                time.sleep(2)
            else:
                text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()
        except:
            text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()
    
    # Method that allows player to look left.
    
    def look_left(self):
        try:
            if self.puzzle == "puzzle_one":
                text.Colour("\nThem mountains are mighty big off in the distance. Nothing between here and there but scorched desert...\n").cyan()
                time.sleep(2)
            elif self.puzzle == "puzzle_two":
                text.Colour("\nThe tracks are mighty wide in here.\n").cyan()
                time.sleep(2)
                text.Colour("Looks like there are about six or seven different lines. I wonder which one I need to take?\n").cyan()
                time.sleep(2)
            elif self.puzzle == "puzzle_three":
                text.Colour("\nJust plain ol' rock this way. Looks like a no-go.\n").cyan()
                time.sleep(2)
            elif self.puzzle == "puzzle_four":
                text.Colour("\nHow'd this place get so flooded?\n").cyan()
                time.sleep(2)
                text.Colour("Probably that pumping station out the front ain't working.\nMaybe that's why the miners are stuck?\n").cyan()
                time.sleep(2)
            elif self.puzzle == "puzzle_five":
                text.Colour("\nLooks like some sort of substation...\n").cyan()
                time.sleep(2)
                # Use of the Player's Boots
                text.Colour(f"Better not get too close in case it got flooded! Gotta make sure my {self.boots} don't slip over 'ere \n").cyan() #TODO 5
                time.sleep(2)
            else:
                text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()
        except:
            text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()
    
    # Method that allows player to look up.
    
    def look_up(self):
        try:
            if self.puzzle == "puzzle_one":
                # Use of the Player's Hair Colour
                text.Colour(f"\nBeautiful blue! Not a cloud in the sky! It's burning my {self.hair_colour} hair, gotta head in\n").cyan() #TODO 1
                time.sleep(2)
            elif self.puzzle == "puzzle_two":
                text.Colour("\nThey've sure put a lot of effort into holding up that ceiling!\nThose beams look mighty strong.\n").cyan()
                time.sleep(2)
            elif self.puzzle == "puzzle_three":
                text.Colour("\nI can't even tilt my head to look up. I hope ya'll aint clostrophobic or nothing...\n").cyan()
                time.sleep(1)
                text.Colour("\n[CLANG]\n").magenta()
                time.sleep(1)
                text.Colour("\nHey dang! I just darn banged my head on a mask!\n").cyan()
                time.sleep(2)
                equip = input(text.Colour("\n\nYa'll wana add it to your inventory?\nYes - \"y\"\nNo - \"n\"\n:").input_cyan())
                time.sleep(2)
                equip = equip.lower().strip(" ")
                if equip == "y":
                    # Check equipment for mask.
                    if inventory.Inventory(self.username).has_required_epuipment("mask"):
                        text.Colour("\nNow now, I see you already got a mask!\n\nNo need for another one...\n").cyan()
                        time.sleep(1)
                    else:
                        # Add mask to inventory.
                        inventory.Inventory(self.username).pickup_equipment("mask")
                        text.Colour("\nYa'll picked-up a mask! Yeeehaaaww!\n").cyan()
                        time.sleep(1)
                elif equip == "n":
                    # Reject equipment.
                    text.Colour("\nWhy that could'a come in handy! Ah well, I guess we don't wana be carrying too much stuff around...\n\n").cyan()
            elif self.puzzle == "puzzle_four":
                text.Colour("\nI can jus about see the roof of this thing.\n").cyan()
                time.sleep(2)
                # Use of the Player's Hat
                text.Colour(f"It's damn enormous in here! Gotta keep my {self.hat} dry\n").cyan() #TODO 4
                time.sleep(2)
            elif self.puzzle == "puzzle_five":
                text.Colour("\nJust a load of mesh I guess.\n").cyan()
                time.sleep(2)
            else:
                text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()
        except:
            text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()
    
    # Method that allows player to look down.
    
    def look_down(self):
        try:
            if self.puzzle == "puzzle_one":
                text.Colour("\nNothing much around here on the floor. Just a bunch of dust bits of old oily rag...\n").cyan()
                time.sleep(1)
                text.Colour("\nOh my! Looks like someone dropped their notebook!\n").cyan()
                time.sleep(2)
                equip = input(text.Colour("\n\nYa'll wana add it to your inventory?\nYes - \"y\"\nNo - \"n\"\n:").input_cyan())
                time.sleep(2)
                equip = equip.lower().strip(" ")
                if equip == "y":
                    # Check equipment for notebook.
                    if inventory.Inventory(self.username).has_required_epuipment("notebook"):
                        text.Colour("\nNow now, I see you already got a notebook!\n\nNo need for another one...\n").cyan()
                        time.sleep(1)
                    else:
                        # Add lasso to inventory.
                        inventory.Inventory(self.username).pickup_equipment("notebook")
                        text.Colour("\nYa'll picked-up a notebook! Yeeehaaaww!\n").cyan()
                        time.sleep(1)
                elif equip == "n":
                    # Reject equipment.
                    text.Colour("\nWhy that could'a come in handy! Ah well, I guess we don't wana be carrying too much stuff around...\n\n").cyan()
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
        except:
            text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()
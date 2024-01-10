'''
This is the puzzle module with Puzzle class and methods containing puzzles 1-5.
These puzzles form the bulk of the gameplay.

'''
#==== Imports ====#

import random
import time
import npc
import mine_rescue_main as main
import location
import leaderboard
import text
import inventory
import help

#==== Class and methods ====#

class Puzzle:
    
    # Constructor.
    def __init__(self, username, gender, hair_colour, hat, boots):
        self.username = username
        self.gender = gender
        self.hair_colour = hair_colour
        self.hat = hat
        self.boots = boots
        self.npc = npc.Npc()

    # Method for puzzle_one to shift text.

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

    # Method giving First Puzzle - Decode the Writing.

    def puzzle_one(self):
        
        # Game intro.
        text.Typed.intro()

        time.sleep(3)
        text.Colour(f"\n\nWhoa there, who's that fella running at you from the entrance of the mine {self.username.title()}?\n\n").cyan()
        time.sleep(2)
        text.Colour("[A mine worker runs up to you speaking an unknown language.]\n\n").magenta()
        # Use Npc class for intro speech.
        text.Colour(f"[He babbles:] {self.npc.get_intro('railwayman_one')}\n\n").magenta()
        time.sleep(3)
        text.Colour("[He then hands you a piece of paper with words on it and points towards the mine.]\n\n").magenta()
        time.sleep(2)
        text.Typed.image_one()
        time.sleep(3)
                
        original_sentence = "To make your way into the tunnel, you\'re gonna need to get on a MINECART"
        answer = "minecart"
        
        # Puzzle menu.
        while True:
                
                options = input(text.Colour('''\nI wonder what that was all about...Maybe there's a puzzle to solve?\n\n
Solve puzzle - 1
Hear again - 2
Look around - 3
See status - 4
Save and Exit - e                           
''').input_cyan())
                
                options = options.lower().strip(" ")
                
                # Puzzle logic.
                if options == "1":
                    # Start timer.
                    start_time = time.perf_counter()
                    # Initiates random shift outside loop - so that the puzzle remains same if going to help menu.
                    shift = random.randint(1, 25)  # Random shift value
                    ciphered_text = self.caesar_cipher(original_sentence, shift)
                    while True:
                        text.Colour(f"[The writing says:]'{ciphered_text}'\n\n\n").magenta()
                        time.sleep(2)
                        user_input = input(text.Colour("Looks like you gotta make some sense of this and figure out the key word\nEnter the key\n\n\nHelp Menu - h\n:").input_cyan()).strip().lower()
                        time.sleep(1)
                        
                        if user_input == answer:
                            # End timer.
                            end_time = time.perf_counter()
                            text.Colour(f"\nWell done {self.username.title()}! You found the way.\n\n\n").cyan()
                            # Count the time taken.
                            count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                            # Update leaderboard.
                            leaderboard.Leaderboard(self.username, "puzzle_two", count_time).update_leaderboard()
                            # Show leaderboard.
                            leaderboard.Leaderboard.show_Leaderboard()
                            # Save progress.
                            main.save_progress(self.username, "puzzle_two")
                            # Continue game menu.
                            options = input(text.Colour('''You did real well there partner!\n\nYa'll wana carry on into this here mine and rescue them miners?
Continue - c
Exit - e
:''').input_cyan())
                            options = options.lower().strip(" ")
                            
                            if options == "c":
                                # Go to next puzzle.
                                main.load_progress(self.username)
                                return True
                            
                            elif options == "e":
                                # Exit
                                time.sleep(2)
                                text.Colour("\nSorry to see you go partner! Mines aren't for the faint hearted...\n\n\n").cyan()
                                return False
                            
                            else:
                                time.sleep(2)
                                text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
                                continue
                        # Help Menu
                        elif user_input == 'h':
                            help.Help(self.username, "puzzle_one").get_help()
                        elif user_input != answer:
                            
                            text.Colour("Oh dust!, the writing changed?!\n\n\n").cyan()
                            time.sleep(2)
                            # Continue puzzle menu.
                            cont = input(text.Colour("Want to have another go fella?\n\nYes - y\nExit puzzle - e\n:").input_cyan())
                            cont = cont.lower().strip(" ")
                            
                            if cont == "y":
                                continue
                            elif cont == "e":
                                # End time.
                                end_time = time.perf_counter()
                                # Count time.
                                count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                # Update leaderboard.
                                leaderboard.Leaderboard(self.username, "puzzle_one", count_time).update_leaderboard()
                                break
                            
                            else:
                                text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
                                continue
                            
                        else:
                            text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
                            continue
                        
                # Rehear puzzle.
                elif options == "2":
                    
                    time.sleep(3)
                    text.Colour(f"\n\nWhoa there, who's that fella running at you from the entrace of the mine {self.username.title()}?\n\n").cyan()
                    time.sleep(2)
                    text.Colour("[A mine worker runs up to you speaking an unknown language.]\n\n").magenta()
                    text.Colour(f"[He babbles:] {self.npc.get_intro('railwayman_one')}\n\n").magenta()
                    time.sleep(2)
                    text.Colour("[He then hands you a piece of paper with words on it and points towards the mine.]\n\n").magenta()
                    time.sleep(2)
                    
                # Go to location menu.
                elif options == "3":
                    
                    location.Location(self.username, "puzzle_one", self.gender, self.hair_colour,self.hat, self.boots).get_loc_info()
                
                # Show status.
                elif options == "4":
                    
                    leaderboard.Leaderboard.status_bar("puzzle_one")
                
                # Save and exit to start menu.
                elif options == "e":
                    main.save_progress(self.username, "puzzle_one")
                    break
                else:
                    text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()

    # Method giving Second Puzzle - Railway Expansion.

    def puzzle_two(self):
        
        time.sleep(3)
        text.Colour("\n\n[As you mosey along the rusty old railway, you hear someone shouting at you to stop.]\n\n").magenta()
        text.Colour(f"Who's that dusty man?\nYou wipe the sweat off your {self.hair_colour} hair and squint to see.\n").cyan()
        time.sleep(2)
        # Use Npc class for intro speech.
        text.Colour(f"[A railwayman runs up to you and says:]\n\n{self.npc.get_intro('railwayman_two')}\n\n").magenta()
        time.sleep(2)
        
        # Set the required item for puzzle hint.
        puzzle_two_item = "hammer"
        
        # Prompting for a hint.
        text.Colour(f"{self.npc.get_prompt('railwayman_two')}\n").magenta()
        # Hint menu.
        while True: 
            choice = input(text.Colour('''How'd you wana respond partner?
Yes - y
No - n
Check inventory - c
''').input_cyan())
            choice = choice.lower().strip(" ")
        
            if choice == "y":
                # Checking player equipment.
                if inventory.Inventory(self.username).has_required_epuipment(puzzle_two_item):
                    time.sleep(2)
                    # Get hint.
                    text.Colour(f"\n\n{self.npc.get_hint('railwayman_two')}\n\n").magenta()
                    # Update equipment
                    inventory.Inventory(self.username).update_equipment(puzzle_two_item)
                    break
                else:
                    time.sleep(2)
                    text.Colour("\n\nNow now, No need to tell a lie my friend, I see you ain't got no hammer!\n\n").red()
                    break
            elif choice == "n":
                time.sleep(2)
                text.Colour("\n\nOh riddens, that hammer sure would've been handy\n\n").cyan()
                break
            # Player checks inventory.
            elif choice == "c":
                time.sleep(2)
                text.Colour(f"\n\nYour equipment: {inventory.Inventory(self.username).show_player_inventory()}\n\n").green()
                continue
            else:
                text.Colour("\nThat aint a choice my friend...Try again.\n\n").red()
                time.sleep(2)
                
        # Puzzle menu.       
        while True:
                
                options = input(text.Colour('''\nI wonder what that was all about...Maybe there's a puzzle to solve?\n\n
Solve puzzle - 1
Hear again - 2
Look around - 3
See status - 4
Save and Exit - e                           
\n''').input_cyan())
                
                options = options.lower().strip(" ")
                solution = ['7','7m','7 m','7 metres','7metres','7metre','7 metre','7 meter','7meter','7 meters','7meters',
                            'seven metres','seven meters']
                
                # Puzzle Logic.
                if options == "1":
                    # Start timer.
                    start_time = time.perf_counter()
                    
                    while True:
                        # Show text image two.
                        text.Typed.image_two()

                        answer = input(text.Colour("\nWhat's the height of the arch at the center of the railway track? Enter your answer to the nearest metre.\n\n\nHelp Menu - h\n:").input_cyan())
                        answer = answer.lower().strip(" ")
                        
                        try:
                            # Help Menu
                            if answer == 'h':
                                help.Help(self.username, "puzzle_two").get_help()
                                continue
                            elif answer in solution:
                                # End timer.
                                end_time = time.perf_counter()
                                time.sleep(2)
                                text.Colour(f"\nYou've only gone and done it {self.username.title()}, seems our cart is about a metre long so we should make it over.\n").cyan()
                                # Count the time taken.
                                count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                # Update leaderboard.
                                leaderboard.Leaderboard(self.username, "puzzle_three", count_time).update_leaderboard()
                                # Show leaderboard.
                                leaderboard.Leaderboard.show_Leaderboard()
                                # Save progress.
                                main.save_progress(self.username, "puzzle_three")
                                # Continue game menu.
                                options = input(text.Colour('''You did real well there partner!\n\nYa'll wana carry on into this here mine and rescue them miners?
Continue - c
Exit - e
:''').input_cyan())
                                options = options.lower().strip(" ")
                                
                                if options == "c":
                                    # Go to next puzzle.
                                    main.load_progress(self.username)
                                    return False
                                
                                elif options == "e":
                                    # Exit
                                    time.sleep(2)
                                    text.Colour("\nSorry to see you go partner! Mines aren't for the faint hearted...\n\n\n").cyan()
                                    return False
                                
                                else:
                                    time.sleep(2)
                                    text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
                                    continue
                            elif answer not in solution:
                                
                                time.sleep(2)
                                # Continue puzzle menu.
                                cont = input(text.Colour("Want to have another go fella?\n\nYes - y\nExit puzzle - e\n:").input_cyan())
                                cont = cont.lower().strip(" ")
                                
                                if cont == "y":
                                    continue
                                elif cont == "e":
                                    # End time.
                                    end_time = time.perf_counter()
                                    # Count time.
                                    count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                    # Update leaderboard.
                                    leaderboard.Leaderboard(self.username, "puzzle_two", count_time).update_leaderboard()
                                    break
                                
                                else:
                                    time.sleep(2)
                                    text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
                                    continue
                            else:
                                time.sleep(1)
                                text.Colour("\nHmm, that don't seem quite right, have another go eh?\n\n").red()
                        except:
                            time.sleep(1)
                            text.Colour("\nNow now, enter a number, not some gibberish you fool!\n\n").red()
                       
                # Rehear puzzle.
                elif options == "2":
                    
                    time.sleep(2)
                    text.Colour("\n\n[As you mosey along the rusty old railway, you hear someone shouting at you to stop.]\n\n Who's that dusty man?\n\n").cyan()
                    time.sleep(2)
                    text.Colour(f"[A railwayman runs up to you and says:]\n\n{self.npc.get_intro('railwayman_two')}\n\n").magenta()
                    time.sleep(2)
                # Go to location menu.  
                elif options == "3":
                    
                    location.Location(self.username, "puzzle_two",self.gender, self.hair_colour,self.hat, self.boots).get_loc_info()
                # Show status bar.   
                elif options == "4":
                    
                    leaderboard.Leaderboard.status_bar("puzzle_two")
                # Save and exit to start menu.   
                elif options == "e":
                    main.save_progress(self.username, "puzzle_two")
                    break
                else:
                    text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()

    # Method giving Third Puzzle - Break the links.

    def puzzle_three(self):

        time.sleep(3)
        text.Colour(f"\n\nOh no {self.username.title()}! The tunnel ahead has collapsed, that's the end of this track...\n\n").cyan()
        time.sleep(2)
        text.Colour("Wait look!\n\n").cyan()
        time.sleep(2)
        text.Colour(f"There's just a narrow crawl space left.\nYou kick your {self.boots} to see if it'll get any bigger\n\n").cyan()
        time.sleep(2)
        # Show text image.
        text.Typed.image_three()
        time.sleep(2)
        text.Colour("[A miner hollers at ya'll from the other side of the crawl space:]\n").magenta()
        time.sleep(2)
        # Use Npc class for intro speech.
        text.Colour(f"{self.npc.get_intro('miner_crawlspace')}\n\n").magenta()
        time.sleep(2)

        puzzle_three_item = "lasso"
        
        # Prompting for a hint.
        text.Colour(f"{self.npc.get_prompt('miner_crawlspace')}\n").magenta()
        while True:
            choice = input(text.Colour('''How'd you wana respond partner?
Yes - y
No - n
Check inventory - c
''').input_cyan())
            choice = choice.lower().strip(" ")
        
            if choice == "y":
                # Checking player equipment.
                if inventory.Inventory(self.username).has_required_epuipment(puzzle_three_item):
                    time.sleep(2)
                    # Get hint.
                    text.Colour(f"\n{self.npc.get_hint('miner_crawlspace')}\n\n").magenta()
                    # Update equipment.
                    inventory.Inventory(self.username).update_equipment(puzzle_three_item)
                    break
                else:
                    time.sleep(2)
                    text.Colour("\nNow now partner, don't ya go yankin my strings, I see no lasso in sight!\n\n").red()
                    break
            elif choice == "n":
                time.sleep(2)
                text.Colour("\nI sure could've given you a hand if you had a lasso my friend\n\n").magenta()
                break
            # Player checks inventory.
            elif choice == "c":
                time.sleep(2)
                text.Colour(f"Your equipment: {inventory.Inventory(self.username).show_player_inventory()}\n\n").green()
                continue
            else:
                text.Colour("\nThat aint a choice my friend...Try again.\n\n").red()
                time.sleep(2)
        # Puzzle menu.
        while True:

            options = input(text.Colour('''\nI wonder what that was all about...Maybe there's a puzzle to solve?\n\n
Solve puzzle - 1
Hear again - 2
Look around - 3
See status - 4
Save and Exit - e                           
\n''').input_cyan())
                
            options = options.lower().strip(" ")
            solution = ['4','four','Four']
            
            # Puzzle Logic.
            if options == "1":
                # Start timer.
                start_time = time.perf_counter()
            
                while True:
                    try:
                        #Show text image
                        text.Typed.image_six()
                        time.sleep(2)
                        user_input = input(text.Colour("\nThink hard and enter the minimum number of breaks needed to fix this chain.\n\n\nHelp Menu - h\n:").input_cyan()).strip()

                        # Help Menu
                        if user_input == 'h':
                            help.Help(self.username, "puzzle_three").get_help()
                            continue
                        elif user_input in solution:
                            # End time.
                            end_time = time.perf_counter()
                            time.sleep(2)
                            text.Colour(f"\nAin't you a clever one {self.username.title()}! You're sharper than the prick of a cactus! Only 4 breaks are needed.\n\n").cyan()
                            time.sleep(2)
                            text.Colour("[The miner swiftly breaks the links, joins the chain, and pulls you through the space.]\n\n").magenta()
                            # Count time.
                            count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                            # Update leaderboard.
                            leaderboard.Leaderboard(self.username, "puzzle_four", count_time).update_leaderboard()
                            # Show leaderboard.
                            leaderboard.Leaderboard.show_Leaderboard()
                            # Save progress.
                            main.save_progress(self.username, "puzzle_four")
                            # Continue game menu.
                            options = input(text.Colour('''You did real well there partner!\n\nYa'll wana carry on into this here mine and rescue them miners?
Continue - c
Exit - e
:''').input_cyan())
                            options = options.lower().strip(" ")
                                
                            if options == "c":
                                # Go to next puzzle.
                                main.load_progress(self.username)
                                return True
                            
                            elif options == "e":
                                # Exit to start menu.
                                time.sleep(2)
                                text.Colour("\nSorry to see you go partner! Mines aren't for the faint hearted...\n\n\n").cyan()
                                return False
                            else:
                                time.sleep(2)
                                text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                continue
                        elif user_input not in solution:
                            
                            time.sleep(2)
                            text.Colour("\nNope, that ain't it. You gotta think like you're spendin' links, not silver dollars. Try again...\n").red()
                            time.sleep(2)
                            # Continue puzzle menu.
                            cont = input(text.Colour("Want to have another go fella?\n\nYes - y\nExit puzzle - e\n:").input_cyan())
                            cont = cont.lower().strip(" ")
                            
                            if cont == "y":
                                continue
                            elif cont == "e":
                                # End time.
                                end_time = time.perf_counter()
                                # Count time.
                                count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                # Update leaderboard.
                                leaderboard.Leaderboard(self.username, "puzzle_three", count_time).update_leaderboard()
                                break
                            
                        else:
                            time.sleep(2)
                            text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
                            continue
                    except:
                        text.Colour("Enter the number of breaks ya'll!").red()
            # Rehear puzzle.
            elif options == "2":
                
                time.sleep(3)
                text.Colour(f"\n\nOh no {self.username.title()}! The tunnel ahead has collapsed, that's the end of this track...\n\n").cyan()
                time.sleep(2)
                text.Colour("Wait look!\n\n").cyan()
                time.sleep(2)
                text.Colour(f"There's just a narrow crawl space left.\nYou kick your {self.boots} to see if it'll get bigger\n\n").cyan()
                time.sleep(2)
                text.Colour("[A miner hollers at ya'll from the other side of the crawl space:]\n").magenta()
                time.sleep(2)
                text.Colour(f"{self.npc.get_intro('miner_crawlspace')}\n\n").magenta()
                time.sleep(2)
            # Go to location menu.   
            elif options == "3":
                
                location.Location(self.username, "puzzle_three",self.gender, self.hair_colour,self.hat, self.boots).get_loc_info()
            # Show status bar.  
            elif options == "4":
                
                leaderboard.Leaderboard.status_bar("puzzle_three")
            # Save and exit to start menu.
            elif options == "e":
                main.save_progress(self.username, "puzzle_three")
                break
            else:
                text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()

    # Method giving Fourth Puzzle - Cross the lake.

    def puzzle_four(self):
        
        time.sleep(3)
        text.Colour(f"\n\nHowdy {self.username.title()}! You've just gotten to some kinda underground lake.\n\n").cyan()
        time.sleep(2)
        text.Colour("That smells funny...\n\n").cyan()
        time.sleep(2)
        text.Colour("Is that gas?! Y'all gotta find a way out!!\n\n").cyan()
        time.sleep(2)
        text.Colour("Looky over there!\n\n").cyan()
        time.sleep(2)
        text.Colour("There's a rickety old boat, a jittery old miner, some unstable dynamite, and a sneaky rat!\n\n").cyan()
        time.sleep(2)
        # Show text image.
        text.Typed.image_four()
        time.sleep(2)
        text.Colour("\nI reckon ya'll gotta get em all across to the other side before the whole place floods!\n\n").cyan()
        time.sleep(2)
        
        # Use Npc class for intro speech.
        text.Colour(f"[The jittery miner stumbles up to you:]\n{self.npc.get_intro('miner_two')}\n\n").magenta()
        time.sleep(2)
        
        puzzle_four_item = "mask"
        
        text.Colour('''What in the name ya'll gona do??
The actions are:
A - Take Rat Across/Back
B - Take Dynamite Across/Back
C - Take Miner Across/Back
D - Take Nothing Across/Back
''').magenta()
        
        # Prompting for a hint.
        time.sleep(3)
        text.Colour(f"{self.npc.get_prompt('miner_two')}\n\n\n").magenta()
        # Hint menu.
        while True: 
            choice = input(text.Colour('''How'd you wana respond partner?
Yes - y
No - n
Check inventory - c
''').input_cyan())
            choice = choice.lower().strip(" ")        
            if choice == "y":
                # Checking player equipment.
                if inventory.Inventory(self.username).has_required_epuipment(puzzle_four_item):
                    time.sleep(2)
                    # Get hint.
                    text.Colour(f"{self.npc.get_hint('miner_two')}\n\n").magenta()
                    # Update equipment.
                    inventory.Inventory(self.username).update_equipment(puzzle_four_item)
                    break
                else:
                    time.sleep(2)
                    text.Colour("Tryna pull a fast one on me eh? Only mask I see's ya blatant lie!\n\n").red()
                    break
            elif choice == "n":
                time.sleep(2)
                text.Colour("No mask eh? Guess you gotta figure it out ya self\n\n").magenta()
                break
            # Player checks inventory.
            elif choice == "c":
                time.sleep(2)
                text.Colour(f"Your equipment: {inventory.Inventory(self.username).show_player_inventory()}\n\n").green()
                continue
            else:
                text.Colour("\nThat aint a choice my friend...Try again.\n\n").red()
                time.sleep(2)
        # Puzzle menu.
        while True:
            # Some puzzle flags.
            leave_puzzle = False
            set_three_used = False
            set_five_used = False
            time.sleep(2)
            options = input(text.Colour('''\nI wonder what that was all about...Maybe there's a puzzle to solve?\n\n
Solve puzzle - 1
Hear again - 2
Look around - 3
See status - 4
Save and Exit - e                           
\n''').input_cyan())
        
            options = options.lower().strip(" ")
            # Solution dictionary.
            solution = {1 : ["a", "A"],
                    2 : ["b","B"],
                    3 : ["c", "C"],
                    4 : ["d", "D"]}
        
            # Puzzle Logic - nested while loops so that player doesn't lose entire puzzle entry if one entry is wrong.
            if options == "1":
            
                while True:
                    # Breakout conditional - to break out of multiple while loops back to puzzle menu.
                    if leave_puzzle == True:
                       break
                    else:
                        # Start timer.
                        start_time = time.perf_counter()
                        answer = input(text.Colour('''\nTime's wastin', enter yer moves ONE AT A TIME friend. Real slow-like.
Remember you can't take everyone across at once!

The actions are:
A - Take Rat Across/Back
B - Take Dynamite Across/Back
C - Take Miner Across/Back
D - Take Nothing Across/Back

Help Menu - h
:''').input_cyan())
                        answer = answer.strip(" ")
                    
                        if answer in solution[2]:
                            
                            text.Colour(f"\nThat's a good start {self.username.title()}.\n").cyan()
                            
                            while True:
                                
                                if leave_puzzle == True:
                                   break
                                else:
                                
                                    text.Colour("\nYa'll got:\nB - Take Dynamite Across/Back.\n").cyan()
                                    
                                    answer = input(text.Colour('''\nTime's wastin', enter yer moves ONE AT A TIME friend. Real slow-like.
Remember you can't take everyone across at once!

The actions are:
A - Take Rat Across/Back
B - Take Dynamite Across/Back
C - Take Miner Across/Back
D - Take Nothing Across/Back

Help Menu - h
:''').input_cyan())
                                    answer = answer.lower().strip(" ")
                                    
                                    if answer in solution[4]:
                                        
                                        text.Colour(f"\nKeep it up {self.username.title()}.\n").cyan()
                                    
                                        while True:
                                            
                                            if leave_puzzle == True:
                                               break
                                            else:
                                  
                                                text.Colour("\nYa'll got:\nB - Take Dynamite Across/Back.\nD - Take Nothing Across/Back.\n").cyan()
                                                
                                                answer = input(text.Colour('''\nTime's wastin', enter yer moves ONE AT A TIME friend. Real slow-like.
Remember you can't take everyone across at once!

The actions are:
A - Take Rat Across/Back
B - Take Dynamite Across/Back
C - Take Miner Across/Back
D - Take Nothing Across/Back

Help Menu - h
:''').input_cyan())
                                                answer = answer.lower().strip(" ")
                                                
                                                # As either "A" or "C" could be selected at this point.
                                                if answer in solution[1] or answer in solution[3]:
                                                    # Set flags depending on whether "A" or "C" selected - as if action 3 is "A" then the action 5 must be "C".
                                                    if answer in solution[1]:
                                                        set_three_used = True
                                                        take_across_one = "A - Take Rat Across/Back."
                                                    elif answer in solution[3]:
                                                        take_across_one ="C - Take Miner Across/Back."
                                                        set_five_used = True
                                                    
                                                    text.Colour(f"\nKeep it up {self.username.title()}.\n").cyan()
                                                    
                                                    while True:
                                                        
                                                        if leave_puzzle == True:
                                                           break
                                                        else:
                                                        
                                                            text.Colour(f"\nYa'll got:\nB - Take Dynamite Across/Back.\nD - Take Nothing Across/Back.\n{take_across_one}\n").cyan()
                                                            
                                                            answer = input(text.Colour('''\nTime's wastin', enter yer moves ONE AT A TIME friend. Real slow-like.
Remember you can't take everyone across at once!

The actions are:
A - Take Rat Across/Back
B - Take Dynamite Across/Back
C - Take Miner Across/Back
D - Take Nothing Across/Back

Help Menu - h
:''').input_cyan())
                                                            answer = answer.lower().strip(" ")
                                                        
                                                            if answer in solution[2]:
                                                                
                                                                text.Colour(f"\nKeep it up {self.username.title()}.\n").cyan()
                                                                
                                                                while True:
                                                                    
                                                                    if leave_puzzle == True:
                                                                       break
                                                                    else:
                                                                        
                                                                        text.Colour(f"\nYa'll got:\nB - Take Dynamite Across/Back.\nD - Take Nothing Across/Back.\n{take_across_one}\nB - Take Dynamite Across/Back.\n").cyan()
                                                                        
                                                                        answer = input(text.Colour('''\nTime's wastin', enter yer moves ONE AT A TIME friend. Real slow-like.
Remember you can't take everyone across at once!

The actions are:
A - Take Rat Across/Back
B - Take Dynamite Across/Back
C - Take Miner Across/Back
D - Take Nothing Across/Back

Help Menu - h
:''').input_cyan())
                                                                        answer = answer.lower().strip(" ")
                                                                        
                                                                        # Ensuring either "A" or "C" has not been entered twice using flags established above.
                                                                        if (answer in solution[3] and set_three_used == True) or (answer in solution[1] and set_five_used == True):
                                                                            
                                                                            if answer in solution[1]:
                                                                                take_across_two = "A - Take Rat Across/Back."
                                                                            elif answer in solution[3]:
                                                                                take_across_two ="C - Take Miner Across/Back."                                              
                                                                            
                                                                            text.Colour(f"\nKeep it up {self.username.title()}.\n").cyan()
                                                                            
                                                                            while True:
                                                                                
                                                                                if leave_puzzle == True:
                                                                                   break
                                                                                else:
                                                                            
                                                                                    text.Colour(f"\nYa'll got:\nB - Take Dynamite Across/Back.\nD - Take Nothing Across/Back.\n{take_across_one}\nB - Take Dynamite Across/Back.\n{take_across_two}\n").cyan()
                                                                                    
                                                                                    answer = input(text.Colour('''\nTime's wastin', enter yer moves ONE AT A TIME friend. Real slow-like.
Remember you can't take everyone across at once!

The actions are:
A - Take Rat Across/Back
B - Take Dynamite Across/Back
C - Take Miner Across/Back
D - Take Nothing Across/Back

Help Menu - h
:''').input_cyan())
                                                                                    answer = answer.lower().strip(" ")
                                
                                                                                    if answer in solution[4]:
                                                                                        
                                                                                        text.Colour(f"\nKeep it up {self.username.title()}.\n").cyan()
                                                                                        
                                                                                        while True:
                                                                                            
                                                                                            if leave_puzzle == True:
                                                                                               break
                                                                                            else:
                                                                                            
                                                                                                text.Colour(f"\nYa'll got:\nB - Take Dynamite Across/Back.\nD - Take Nothing Across/Back.\n{take_across_one}\nB - Take Dynamite Across/Back.\n{take_across_two}\nD - Take Nothing Across/Back.\n").cyan()
                                                                                                answer = input(text.Colour('''\nTime's wastin', enter yer moves ONE AT A TIME friend. Real slow-like.
Remember you can't take everyone across at once!

The actions are:
A - Take Rat Across/Back
B - Take Dynamite Across/Back
C - Take Miner Across/Back
D - Take Nothing Across/Back

Help Menu - h
:''').input_cyan())
                                                                                                answer = answer.lower().strip(" ")
                                    
                                                                                                if answer in solution[2]:
                                                                                                    # End timer.
                                                                                                    end_time = time.perf_counter()
                                                                                                    time.sleep(2)
                                                                                                    text.Colour(f"\nYeehaw! Ya did it {self.username.title()}! All safe and sound on t'other side.\n\n").cyan()
                                                                                                    time.sleep(2)
                                                                                                    text.Colour(f"\nYa'll got:\nB - Take Dynamite Across/Back.\nD - Take Nothing Across/Back.\n{take_across_one}\nB - Take Dynamite Across/Back.\n{take_across_two}\nD - Take Nothing Across/Back.\nB - Take Dynamite Across/Back.\n").cyan()
                                                                                                    # Count time.
                                                                                                    count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                                                                                    # Update leaderboard.
                                                                                                    leaderboard.Leaderboard(self.username, "puzzle_five", count_time).update_leaderboard()
                                                                                                    # Show leaderboard.
                                                                                                    leaderboard.Leaderboard.show_Leaderboard()
                                                                                                    # Save progress.
                                                                                                    main.save_progress(self.username, "puzzle_five")
                                                                                                    # Continue game menu.
                                                                                                    options = input(text.Colour('''You did real well there partner!\n\nYa'll wana carry on into this here mine and rescue them miners?
Continue - "c"
Exit - "e"
:''').input_cyan())
                                                                                                    options = options.lower().strip(" ")
                                                                                                    # Go to next puzzle.   
                                                                                                    if options == "c":
                                                                                                        main.load_progress(self.username)
                                                                                                        return False
                                                                                                    # Exit to start menu.
                                                                                                    elif options == "e":
                                                                                                        time.sleep(2)
                                                                                                        text.Colour("\nSorry to see you go partner! Mines aren't for the faint hearted...\n\n\n").cyan()
                                                                                                        return False
                                                                                                    else:
                                                                                                        time.sleep(2)
                                                                                                        text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                                                                                        continue
                                                                                                    break
                                                                                                # Help Menu
                                                                                                elif answer == 'h':
                                                                                                    help.Help(self.username,"puzzle_four").get_help()
                                                                                                    continue
                                                                                                elif answer not in solution[2]:
                                                                                                    
                                                                                                    time.sleep(2)
                                                                                                    text.Colour("\nThat don't sound quite right, we ain't got forever...\n\n").red()
                                                                                                    time.sleep(1)
                                                                                                    # Continue puzzle menu.
                                                                                                    cont = input(text.Colour("Want to have another go fella?\n\nYes - y\nExit puzzle - e\n:").input_cyan())
                                                                                                    cont = cont.lower().strip(" ")
                                                                                                    
                                                                                                    if cont == "y":
                                                                                                        continue
                                                                                                    elif cont == "e":
                                                                                                        # End timer.
                                                                                                        end_time = time.perf_counter()
                                                                                                        time.sleep(1)
                                                                                                        text.Colour("\n\nReckon the gas hurt'n ya brain my friend.\n").red()
                                                                                                        time.sleep(2)
                                                                                                        # Count time.
                                                                                                        count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                                                                                        # Update leaderboard.
                                                                                                        leaderboard.Leaderboard(self.username, "puzzle_four", count_time).update_leaderboard()
                                                                                                        # Using flag initiated after puzzle menu.
                                                                                                        leave_puzzle = True
                                                                                                    
                                                                                                    else:
                                                                                                        time.sleep(1)
                                                                                                        text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
                                                                                                        continue
                                                                                    # Help Menu
                                                                                    elif answer == 'h':
                                                                                        help.Help(self.username,"puzzle_four").get_help()
                                                                                    elif answer not in solution[4]:
                                                                                        
                                                                                        time.sleep(2)
                                                                                        text.Colour("\nThat don't sound quite right, we ain't got forever...\n\n").red()
                                                                                        time.sleep(1)
                                                                                        cont = input(text.Colour("Want to have another go fella?\n\nYes - y\nExit puzzle - e\n:").input_cyan())
                                                                                        cont = cont.lower().strip(" ")
                                                                                        
                                                                                        if cont == "y":
                                                                                            continue
                                                                                        elif cont == "e":
                                                                                            end_time = time.perf_counter()
                                                                                            time.sleep(1)
                                                                                            text.Colour("\nReckon the gas hurt'n ya brain my friend.\n\n").red()
                                                                                            time.sleep(2)
                                                                                            count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                                                                            leaderboard.Leaderboard(self.username, "puzzle_four", count_time).update_leaderboard()
                                                                                            leave_puzzle = True
                                                                                        
                                                                                        else:
                                                                                            time.sleep(1)
                                                                                            text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
                                                                                            continue
                                                                        # Help Menu
                                                                        elif answer == 'h':
                                                                            help.Help(self.username,"puzzle_four").get_help()
                                                                            continue
                                                                        elif (answer not in solution[3]) or (answer in solution[3] and set_three_used == False) or (answer not in solution[1]) or (answer in solution[1] and set_five_used == False):
                                                                            
                                                                            time.sleep(2)
                                                                            text.Colour("\nThat don't sound quite right, we ain't got forever...\n\n").red()
                                                                            time.sleep(1)
                                                                            cont = input(text.Colour("Want to have another go fella?\n\nYes - y\nExit puzzle - e\n:").input_cyan())
                                                                            cont = cont.lower().strip(" ")
                                                                            
                                                                            if cont == "y":
                                                                                continue
                                                                            elif cont == "e":
                                                                                end_time = time.perf_counter()
                                                                                time.sleep(1)
                                                                                text.Colour("\nReckon the gas hurt'n ya brain my friend.\n\n").red()
                                                                                time.sleep(2)
                                                                                count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                                                                leaderboard.Leaderboard(self.username, "puzzle_four", count_time).update_leaderboard()
                                                                                leave_puzzle = True
                                                                            
                                                                            else:
                                                                                time.sleep(1)
                                                                                text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
                                                                                continue
                                                            # Help Menu
                                                            elif answer == 'h':
                                                                help.Help(self.username, "puzzle_four").get_help()
                                                                continue
                                                            elif answer not in solution[2]:
                                                                
                                                                time.sleep(2)
                                                                text.Colour("\nThat don't sound quite right, we ain't got forever...\n\n").red()
                                                                time.sleep(1)
                                                                cont = input(text.Colour("Want to have another go fella?\n\nYes - y\nExit puzzle - e\n:").input_cyan())
                                                                cont = cont.lower().strip(" ")
                                                                
                                                                if cont == "y":
                                                                    continue
                                                                elif cont == "e":
                                                                    end_time = time.perf_counter()
                                                                    time.sleep(1)
                                                                    text.Colour("\nReckon the gas hurt'n ya brain my friend.\n\n").red()
                                                                    time.sleep(2)
                                                                    count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                                                    leaderboard.Leaderboard(self.username, "puzzle_four", count_time).update_leaderboard()
                                                                    leave_puzzle = True
                                                                
                                                                else:
                                                                    time.sleep(1)
                                                                    text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
                                                                    continue
                                                # Help Menu
                                                elif answer == 'h':
                                                    help.Help(self.username, "puzzle_four").get_help()
                                                    continue
                                                elif answer not in solution[1] and answer not in solution[3]:
                                                    
                                                    time.sleep(2)
                                                    text.Colour("\nThat don't sound quite right, we ain't got forever...\n\n").red()
                                                    time.sleep(1)
                                                    cont = input(text.Colour("Want to have another go fella?\n\nYes - y\nExit puzzle - e\n:").input_cyan())
                                                    cont = cont.lower().strip(" ")
                                                    
                                                    if cont == "y":
                                                        continue
                                                    elif cont == "e":
                                                        end_time = time.perf_counter()
                                                        time.sleep(1)
                                                        text.Colour("\nReckon the gas hurt'n ya brain my friend.\n\n").red()
                                                        time.sleep(2)
                                                        count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                                        leaderboard.Leaderboard(self.username, "puzzle_four", count_time).update_leaderboard()
                                                        leave_puzzle = True
                                                    
                                                    else:
                                                        time.sleep(1)
                                                        text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
                                                        continue
                                    # Help Menu
                                    elif answer == 'h':
                                        help.Help(self.username,"puzzle_four").get_help()
                                        continue
                                    elif answer not in solution[4]:
                                        
                                        time.sleep(2)
                                        text.Colour("\nThat don't sound quite right, we ain't got forever...\n\n").red()
                                        time.sleep(1)
                                        cont = input(text.Colour("Want to have another go fella?\n\nYes - y\nExit puzzle - e\n:").input_cyan())
                                        cont = cont.lower().strip(" ")
                                        
                                        if cont == "y":
                                            continue
                                        elif cont == "e":
                                            end_time = time.perf_counter()
                                            time.sleep(1)
                                            text.Colour("\nReckon the gas hurt'n ya brain my friend.\n\n").red()
                                            time.sleep(2)
                                            count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                            leaderboard.Leaderboard(self.username, "puzzle_four", count_time).update_leaderboard()
                                            leave_puzzle = True
                                        
                                        else:
                                            time.sleep(1)
                                            text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
                                            continue
                        # Help Menu
                        elif answer == 'h':
                            help.Help(self.username,"puzzle_four").get_help()
                            continue
                        elif answer not in solution[2]:
                            
                            time.sleep(2)
                            text.Colour("\nThat don't sound quite right, we ain't got forever...\n\n").red()
                            time.sleep(1)
                            cont = input(text.Colour("Want to have another go fella?\n\nYes - y\nExit puzzle - e\n:").input_cyan())
                            cont = cont.lower().strip(" ")
                            
                            if cont == "y":
                                continue
                            elif cont == "e":
                                end_time = time.perf_counter()
                                time.sleep(1)
                                text.Colour("\nReckon the gas hurt'n ya brain my friend.\n\n").red()
                                time.sleep(2)
                                count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                leaderboard.Leaderboard(self.username, "puzzle_four", count_time).update_leaderboard()
                                break
                            
                            else:
                                time.sleep(1)
                                text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
                                continue

            # Rehear puzzle.           
            elif options == "2":
                 
                time.sleep(3)
                text.Colour(f"\n\nHowdy {self.username.title()}! You've just gotten to some kinda underground lake.\n\n").cyan()
                time.sleep(2)
                text.Colour("That smells funny...\n\n\n").cyan()
                time.sleep(2)
                text.Colour("Is that gas?! Y'all gotta find a way out!!\n\n").cyan()
                time.sleep(2)
                text.Colour("Looky over there!\n\n").cyan()
                time.sleep(2)
                text.Colour("There's a rickety old boat, a jittery old miner, some unstable dynamite, and a sneaky rat!\n\n").cyan()
                time.sleep(2)
                text.Colour("I reckon ya'll gotta get em all across to the other side before the whole place floods!\n\n").cyan()
                time.sleep(2)
                text.Colour(f"[The jittery miner stumbles up to you:]\n{self.npc.get_intro('miner_two')}\n\n").magenta()
                time.sleep(2)
                
                text.Colour('''What in the name ya'll gona do??
Your actions are:
A - Take Rat Across
B - Take Dynamite Across
C - Take Miner Across
D - Take Nothing Across
''').magenta()
            # Go to location menu.     
            elif options == "3":
                 
                 location.Location(self.username, "puzzle_four",self.gender, self.hair_colour,self.hat, self.boots).get_loc_info()
            # Show status bar.    
            elif options == "4":
                 
                 leaderboard.Leaderboard.status_bar("puzzle_four")
            # Save and exit to start menu.     
            elif options == "e":
                
                main.save_progress(self.username, "puzzle_four")
                break
            else:
                 text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()

    # Method giving Fifth Puzzle - Lift Shaft.

    def puzzle_five(self):
        
        time.sleep(3)
        text.Colour(f"\nHowdy {self.username.title()}! You must be close to the lift shaft now. That must be where the miners are trapped!\n\n\n").cyan()
        time.sleep(2)
        text.Colour("It's a real squeeze down here! I wonder if we're ever going to find these fellas?\n\n").cyan()
        time.sleep(2)
        text.Colour("Drip\n").cyan()
        time.sleep(2)
        text.Colour("Drip\n").cyan()
        time.sleep(2)
        text.Colour("Drip\n").cyan()
        time.sleep(2)
        text.Colour("Whoa! Wait partner, you hear that?\n\n").cyan()
        time.sleep(2)
        text.Colour("[Faintly, off down the tunnel] Help! Is there someone there?\n\n").magenta()
        time.sleep(2)
        text.Colour("You reckon that's them?\n").cyan()
        time.sleep(2)
        text.Colour("Let's shout back!\n").cyan()
        time.sleep(2)
        text.Colour("Hellllooooo!\n\n").cyan()
        time.sleep(2)
        text.Colour("Anyone down there?\n\n").cyan()
        time.sleep(2)
        text.Colour("[SILENCE]\n\n").magenta()
        time.sleep(2)
        text.Colour("[Louder] Anyone doooowwwwn theeerrreeee?\n\n\n").cyan()
        time.sleep(2)
        text.Colour("Heeelllp! Weee'reee traappped!\n\n").magenta()
        time.sleep(2)
        text.Colour("That must be them!\nLet's go find out!\n\n\n\n").cyan()
        time.sleep(2)
        text.Colour("[Some minutes later...]\n\n").magenta()
        time.sleep(3)
        text.Colour("Look, it's a lift shaft\n\n\nYou fellas alright down there?\n\n").cyan()
        time.sleep(2)
        text.Typed.image_five()
        time.sleep(3)
        
        # Use Npc class for intro.
        text.Colour(f"Boy are we glad to see you!\n\n{self.npc.get_intro('trapped_miner')}\n").magenta()
        time.sleep(3)
        
        puzzle_five_item = "notebook" 
        
        # Prompting for a hint.
        text.Colour(f"{self.npc.get_prompt('trapped_miner')}\n\n").magenta()
        # Hint menu.
        while True: 
            choice = input(text.Colour('''How'd you wana respond partner?
Yes - y
No - n
Check inventory - c
''').input_cyan())
            choice = choice.lower().strip(" ")
            
            if choice == "y":
                # Checking player equipment.
                if inventory.Inventory(self.username).has_required_epuipment(puzzle_five_item):
                    time.sleep(2)
                    # Give hint.
                    text.Colour(f"{self.npc.get_hint('trapped_miner')}\n\n").magenta()
                    # Update equipment.
                    inventory.Inventory(self.username).update_equipment(puzzle_five_item)
                    break
                else:
                    time.sleep(2)
                    text.Colour("Tryna pull a fast one on me eh? Only mask I see's ya blatant lie!\n\n").red()
                    break
            elif choice == "n":
                time.sleep(2)
                text.Colour("Ah dang! Ya'll don't got a notebook? Guess you gotta figure it out ya self...\n\n").magenta()
                break
            # Player checks inventory.
            elif choice == "c":
                time.sleep(2)
                text.Colour(f"Your equipment: {inventory.Inventory(self.username).show_player_inventory()}\n\n").green()
                continue
            else:
                text.Colour("\nThat aint a choice my friend...Try again.\n\n").red()
                time.sleep(2)        
        
        # Puzzle menu.
        while True:
            # Initiating flag to leave puzzle.
            leave_puzzle = False
            
            options = input(text.Colour('''\nSeems like a tricky puzzle partner... What do ya'll wana do?
Solve puzzle - 1
Hear again - 2
Look around - 3
See status - 4
Save and Exit - e                           
\n''').input_cyan())
            
            options = options.lower().strip(" ")
            # Dictionary containing possible solutions for each stage of puzzle.
            solution = {1 : ["98-7", "98 - 7", "98- 7", "98 -7", "-7", "- 7"],
                        2 : ["91-6", "91 - 6", "91- 6", "91 -6", "-6", "- 6"],
                        3 : ["85+5", "85 + 5", "85+ 5", "85 +5", "+5", "+ 5"],
                        4 : ["90+4", "90 + 4", "90+ 4", "90 +4", "+4", "+ 4"],
                        5 : ["94+3", "94 + 3", "94+ 3", "94 +3", "+3", "+ 3"],
                        6 : ["97+2", "97 + 2", "97+ 2", "97 +2", "+2", "+ 2"],
                        7 : ["99+1", "99 + 1", "99+ 1", "99 +1", "+1", "+ 1"]}
            # Puzzle logic.
            if options == "1":
                
                while True:
                    # Breakout conditional - to break out of multiple while loops back to puzzle menu.
                    if leave_puzzle == True:
                       break
                    else:
                        # Start timer.
                        start_time = time.perf_counter()
                        answer = input(text.Colour("\nSo what's your answer partner?\n\nYou got 98, 7, 6, 5, 4, 3, 2, 1, and as many + and - as ya'll want to work with\n\nEnter each operation at a time\n\nHelp Menu - h\n:").input_cyan())
                        answer = answer.lower().strip(" ")
                    
                        if answer in solution[1]:
                            
                            text.Colour(f"\nThat's a good start {self.username.title()}.\n").cyan()
                            
                            while True:
                                
                                if leave_puzzle == True:
                                   break
                                else: 
                                    text.Colour("\nYa'll got 91.\n").cyan()
                                    
                                    answer = input(text.Colour("\nWhat next partner?\n\nYou got 6, 5, 4, 3, 2, 1, and as many + and - as ya'll want to work with\n\nEnter one stage at a time:\n\nHelp Menu - h\n:").input_cyan())
                                    answer = answer.lower().strip(" ")
                                    
                                    if answer in solution[2]:
                                        
                                        text.Colour(f"\nKeep it up {self.username.title()}.\n").cyan()
                                        
                                        while True:
                                            
                                            if leave_puzzle == True:
                                               break
                                            else:
                                                text.Colour("\nYa'll got 85.\n").cyan()
                                                
                                                answer = input(text.Colour("\nWhat next partner??\n\nYou got 5, 4, 3, 2, 1, and as many + and - as ya'll want to work with\n\nEnter one stage at a time:\n\nHelp Menu - h\n:").input_cyan())
                                                answer = answer.lower().strip(" ")
                                            
                                                if answer in solution[3]:
                                                    
                                                    text.Colour(f"\nKeep it up {self.username.title()}.\n").cyan()
                                                    
                                                    while True:
                                                        
                                                        if leave_puzzle == True:
                                                           break
                                                        else:
                                                            text.Colour("\nYa'll got 90.\n").cyan()
                                                            
                                                            answer = input(text.Colour("\nWhat next partner??\n\nYou got 4, 3, 2, 1,and as many + and - as ya'll want to work with\n\nEnter one stage at a time:\n\nHelp Menu - h\n:").input_cyan())
                                                            answer = answer.lower().strip(" ")
                                                            
                                                            if answer in solution[4]:
                                                                
                                                                text.Colour(f"\nKeep it up {self.username.title()}.\n").cyan()
                                                                
                                                                while True:
                                                                    
                                                                    if leave_puzzle == True:
                                                                       break
                                                                    else:
                                                                        text.Colour("\nYa'll got 94.\n").cyan()
                                                                        answer = input(text.Colour("\nWhat next partner??\n\nYou got 3, 2, 1, and as many + and - as ya'll want to work with\n\nEnter one stage at a time:\n\nHelp Menu - h\n:").input_cyan())
                                                                        answer = answer.lower().strip(" ")
                    
                                                                        if answer in solution[5]:
                                                                            
                                                                            text.Colour(f"\nKeep it up {self.username.title()}.\n").cyan()
                                                                            
                                                                            while True:
                                                                                
                                                                                if leave_puzzle == True:
                                                                                   break
                                                                                else:
                                                                                    text.Colour("\nYa'll got 97.\n").cyan()
                                                                                    answer = input(text.Colour("\nWhat next partner?\n\nYou got 2, 1, and as many + and - as ya'll want to work with\n\nEnter one stage at a time:\n\nHelp Menu - h\n:").input_cyan())
                                                                                    answer = answer.lower().strip(" ")
                        
                                                                                    if answer in solution[6]:
                                                                                        
                                                                                        text.Colour(f"\nKeep it up {self.username.title()}.\n").cyan()
                                                                                        
                                                                                        while True:
                                                                                            
                                                                                            if leave_puzzle == True:
                                                                                               break
                                                                                            else:
                                                                                                text.Colour("\nYa'll got 99.\n").cyan()
                                                                                                
                                                                                                answer = input(text.Colour("\nWhat next partner?\n\nYou got 1, and as many + and - as ya'll want to work with\n\nEnter one stage at a time:\n\nHelp Menu - h\n:").input_cyan())
                                                                                                answer = answer.lower().strip(" ")
                                                                                                
                                                                                                if answer in solution[7]:
                                                                                                    # End timer.
                                                                                                    end_time = time.perf_counter()
                                                                                                    text.Colour(f"\nGREAT WORK {self.username.title()}!\n").cyan()
                                                                                                    text.Colour("\nYa'll got 100.\n").cyan()
                                                                                                    # Count time.
                                                                                                    count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                                                                                    # Update leaderboard.
                                                                                                    leaderboard.Leaderboard(self.username, "finished", count_time).update_leaderboard()
                                                                                                    # Save progress
                                                                                                    main.save_progress(self.username, "finished")
                                                                                                    text.Colour(f"YOU DID IT {self.username.title()}!\n\n\n").cyan()
                                                                                                    time.sleep(4)
                                                                                                    # Use Npc to give outro.
                                                                                                    text.Colour(f"{self.npc.get_outro('trapped_miner')}\n\n\n").magenta()
                                                                                                    # Show status bar.
                                                                                                    leaderboard.Leaderboard.status_bar("finished")
                                                                                                    # Show Outro Image
                                                                                                    text.Typed.outro_image()
                                                                                                    # Show leaderboard.
                                                                                                    leaderboard.Leaderboard.show_Leaderboard()
                                                                                                    return False

                                                                                                elif answer == 'h':
                                                                                                    help.Help(self.username,"puzzle_five").get_help()
                                                                                                    continue
                                                                                                elif answer not in solution[7]:
                                                                                                    time.sleep(2)
                                                                                                    text.Colour("That don't sound quite right, we ain't got forever...\n\n").red()
                                                                                                    time.sleep(2)
                                                                                                    # Continue puzzle menu.
                                                                                                    cont = input(text.Colour("Want to have another go fella?\n\nYes - y\nExit puzzle - e\n:").input_cyan())
                                                                                                    cont = cont.lower().strip(" ")
                                                                                                    
                                                                                                    if cont == "y":
                                                                                                        continue
                                                                                                    elif cont == "e":
                                                                                                        # End timer.
                                                                                                        end_time = time.perf_counter()
                                                                                                        # Count time.
                                                                                                        count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                                                                                        # Update leaderboard.
                                                                                                        leaderboard.Leaderboard(self.username, "puzzle_five", count_time).update_leaderboard()
                                                                                                        # Using flag initiated after puzzle menu.
                                                                                                        leave_puzzle = True                               
                                                                                                    else:
                                                                                                        time.sleep(1)
                                                                                                        text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
                                                                                                        continue
                                                                                    # Help Menu
                                                                                    elif answer == 'h':
                                                                                        help.Help(self.username,"puzzle_five").get_help()
                                                                                        continue
                                                                                    elif answer not in solution[6]:
                                                                                        
                                                                                        time.sleep(2)
                                                                                        text.Colour("That don't sound quite right, we ain't got forever...\n\n").red()
                                                                                        time.sleep(2)
                                                                                        cont = input(text.Colour("Want to have another go fella?\n\nYes - y\nExit to start menu - e\n:").input_cyan())
                                                                                        cont = cont.lower().strip(" ")
                                                                                        
                                                                                        if cont == "y":
                                                                                            continue
                                                                                        elif cont == "e":
                                                                                            end_time = time.perf_counter()
                                                                                            count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                                                                            leaderboard.Leaderboard(self.username, "puzzle_five", count_time).update_leaderboard()
                                                                                            leave_puzzle = True
                                                                                        else:
                                                                                            time.sleep(1)
                                                                                            text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
                                                                                            continue
                                                                        # Help Menu
                                                                        elif answer == 'h':
                                                                            help.Help(self.username,"puzzle_five").get_help()
                                                                            continue
                                                                        elif answer not in solution[5]:
                                                                            time.sleep(2)
                                                                            text.Colour("That don't sound quite right, we ain't got forever...\n\n").red()
                                                                            time.sleep(2)
                                                                            cont = input(text.Colour("Want to have another go fella?\n\nYes - y\nExit to start menu - e\n:").input_cyan())
                                                                            cont = cont.lower().strip(" ")
                                                                            
                                                                            if cont == "y":
                                                                                continue
                                                                            elif cont == "e":
                                                                                end_time = time.perf_counter()
                                                                                count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                                                                leaderboard.Leaderboard(self.username, "puzzle_five", count_time).update_leaderboard()
                                                                                leave_puzzle = True
                                                                            else:
                                                                                time.sleep(1)
                                                                                text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
                                                                                continue
                                                            # Help Menu
                                                            elif answer == 'h':
                                                                help.Help(self.username,"puzzle_five").get_help()
                                                                continue
                                                            elif answer not in solution[4]:
                                                                time.sleep(2)
                                                                text.Colour("That don't sound quite right, we ain't got forever...\n\n").red()
                                                                time.sleep(2)
                                                                cont = input(text.Colour("Want to have another go fella?\n\nYes - y\nExit to start menu - e\n:").input_cyan())
                                                                cont = cont.lower().strip(" ")
                                                                
                                                                if cont == "y":
                                                                    continue
                                                                elif cont == "e":
                                                                    end_time = time.perf_counter()
                                                                    count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                                                    leaderboard.Leaderboard(self.username, "puzzle_five", count_time).update_leaderboard()
                                                                    leave_puzzle = True
                                                                else:
                                                                    time.sleep(1)
                                                                    text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
                                                                    continue
                                                # Help Menu
                                                elif answer == 'h':
                                                    help.Help(self.username,"puzzle_five").get_help()
                                                    continue
                                                elif answer not in solution[3]:
                                                    time.sleep(2)
                                                    text.Colour("That don't sound quite right, we ain't got forever...\n\n").red()
                                                    time.sleep(2)
                                                    cont = input(text.Colour("Want to have another go fella?\n\nYes - y\nExit to start menu - e\n:").input_cyan())
                                                    cont = cont.lower().strip(" ")
                                                    
                                                    if cont == "y":
                                                        continue
                                                    elif cont == "e":
                                                        end_time = time.perf_counter()
                                                        count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                                        leaderboard.Leaderboard(self.username, "puzzle_five", count_time).update_leaderboard()
                                                        leave_puzzle = True
                                                    else:
                                                        time.sleep(1)
                                                        text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
                                                        continue
                                    # Help Menu
                                    elif answer == 'h':
                                        help.Help(self.username,"puzzle_five").get_help()
                                        continue
                                    elif answer not in solution[2]:
                                        time.sleep(2)
                                        text.Colour("That don't sound quite right, we ain't got forever...\n\n").red()
                                        time.sleep(2)
                                        cont = input(text.Colour("Want to have another go fella?\n\nYes - y\nExit to start menu - e\n:").input_cyan())
                                        cont = cont.lower().strip(" ")
                                        
                                        if cont == "y":
                                            continue
                                        elif cont == "e":
                                            end_time = time.perf_counter()
                                            count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                            leaderboard.Leaderboard(self.username, "puzzle_five", count_time).update_leaderboard()
                                            leave_puzzle = True
                                        else:
                                            time.sleep(1)
                                            text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
                                            continue
                        # Help Menu
                        elif answer == 'h':
                            help.Help(self.username,"puzzle_five").get_help()
                            continue
                        elif answer not in solution[1]:
                            time.sleep(2)
                            text.Colour("That don't sound quite right, we ain't got forever...\n\n").red()
                            time.sleep(2)
                            cont = input(text.Colour("Want to have another go fella?\n\nYes - y\nExit to start menu - e\n:").input_cyan())
                            cont = cont.lower().strip(" ")
                            
                            if cont == "y":
                                continue
                            elif cont == "e":
                                end_time = time.perf_counter()
                                count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                leaderboard.Leaderboard(self.username, "puzzle_five", count_time).update_leaderboard()
                                leave_puzzle = True
                            else:
                                time.sleep(1)
                                text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
                                continue
            # Rehear puzzle.               
            elif options == "2":
                
                time.sleep(3)
                text.Colour(f"\nHowdy {self.username.title()}! You must be close to the lift shaft now. That must be where the miners are trapped!\n\n\n").cyan()
                time.sleep(2)
                text.Colour("It's a real squeeze down here! I wonder if we're ever going to find these fellas?\n\n").cyan()
                time.sleep(2)
                text.Colour("Drip\n").cyan()
                time.sleep(2)
                text.Colour("Drip\n").cyan()
                time.sleep(2)
                text.Colour("Drip\n").cyan()
                time.sleep(2)
                text.Colour("Whoa! Wait partner, youn hear that?\n\n").cyan()
                time.sleep(2)
                text.Colour("[Faintly, off down the tunnel] Help! Is there someone there?\n\n").magenta()
                time.sleep(2)
                text.Colour("You reckon that's them?\n").cyan()
                time.sleep(2)
                text.Colour("Let's shout back!\n").cyan()
                time.sleep(2)
                text.Colour("Hellllooooo!\n\n").cyan()
                time.sleep(2)
                text.Colour("Anyone down there?\n\n").cyan()
                time.sleep(2)
                text.Colour("[SILENCE]\n\n").magenta()
                time.sleep(2)
                text.Colour("[Louder] Anyone doooowwwwn theeerrreeee?\n\n\n").cyan()
                time.sleep(2)
                text.Colour("Heeelllp! Weee'reee traappped!\n\n").magenta()
                time.sleep(2)
                text.Colour("That must be them!\nLet's go find out!\n\n\n\n").cyan()
                time.sleep(2)
                text.Colour("[Some minutes later...]\n\n").magenta()
                time.sleep(3)
                text.Colour("Look, it's a lift shaft\n\n\nYou fellas alright down there?\n\n").cyan()
                time.sleep(2)
                text.Typed.image_five()
                time.sleep(3)
                text.Colour(f"Boy are we glad to see you!\n\n{self.npc.get_intro('trapped_miner')}\n").magenta()
                time.sleep(3)
            # Go to location menu.    
            elif options == "3":
                
                location.Location(self.username, "puzzle_five",self.gender, self.hair_colour,self.hat, self.boots).get_loc_info()
            # Show leaderboard.   
            elif options == "4":
                
                leaderboard.Leaderboard.status_bar("puzzle_five")
            # Save and exit to start menu.   
            elif options == "e":
                main.save_progress(self.username, "puzzle_five")
                break
            else:
                text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\nHave another go...\n\n").red()
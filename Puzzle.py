"""
This is the puzzle module with Puzzle class and methods.

"""
import random
import time
import avatar
import mine_rescue_main as main
import location
import leaderboard
import text
import inventory

class Puzzle:
    
    def __init__(self, username):
        self.username = username
        self.avatar = avatar.Avatar()

#==== Function for puzzle_one to shift text ====#

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

#==== First Puzzle - Decode the writing ====#

    def puzzle_one(self):
        
        text.Typed.intro()
        
        time.sleep(3)
        text.Colour(f"\n\nWhoa there, who's that fella running at you from the entrace of the mine {self.username.title()}?\n\n").cyan()
        time.sleep(2)
        text.Colour("[A mine worker runs up to you speaking an unknown language.]\n\n").magenta()
        # Use Avatar class for intro speech
        text.Colour(f"[He babbles:] {self.avatar.get_intro('railwayman_one')}\n\n").magenta()
        time.sleep(3)
        text.Colour("[He then hands you a piece of paper with words on it and points towards the mine.]\n\n").magenta()
        time.sleep(2)
        text.Typed.image_one()
        time.sleep(3)
                
        original_sentence = "To make your way into the tunnel, you\'re gona need to get on a MINECART"
        answer = "minecart"


        while True:
                
                options = input(text.Colour('''\nI wonder what that was all about...Maybe there's a puzzle to solve?\n\n
Solve puzzle - 1
Hear again - 2
Look around - 3
See status - 4
Save and Exit - e                           
''').input_cyan())
                
                options = options.lower().strip(" ")
        
                if options == "1":
                    start_time = time.perf_counter()
                    
                    while True:
                        shift = random.randint(1, 25)  # Random shift value
                        ciphered_text = self.caesar_cipher(original_sentence, shift)
                        text.Colour(f"[The writing says:]'{ciphered_text}'\n\n\n").magenta()
                        
                        time.sleep(5)
                        
                        user_input = input(text.Colour("Looks like you gotta make some sense of this and figure out the key word\nEnter the key:\n\n\n").input_cyan()).strip().lower()
                        
                        time.sleep(5)

                        if user_input == answer:
                            
                            end_time = time.perf_counter()
                            text.Colour(f"\nWell done {self.username.title()}! You found the way.\n\n\n").cyan()
                            
                            count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                            leaderboard.Leaderboard(self.username, "puzzle_two", count_time).update_leaderboard()
                            
                            leaderboard.Leaderboard.show_Leaderboard()
                            
                            main.save_progress(self.username, "puzzle_two")
                            
                            options = input(text.Colour('''You did real well there partner!\n\nYa'll wana carry on into this here mine and rescue them miners?
Continue - "c"
Exit - "e"
:''').input_cyan())
                            options = options.lower().strip(" ")
                            
                            if options == "c":
                                
                                main.load_progress(self.username)
                                return True
                            
                            elif options == "e":
                                time.sleep(2)
                                text.Colour("\nSorry to see you go partner! Mines aren't for the faint hearted...\n\n\n").cyan()
                                return False
                            
                            else:
                                time.sleep(2)
                                text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                continue
                                
                        elif user_input != answer:
                            
                            text.Colour("Oh dust!, the writing changed?!\n\n\n").cyan()
                            
                            time.sleep(2)
                            
                            cont = input(text.Colour("Want to have another go fella?\n\nYes - \"y\"\nExit puzzle - \"e\"\n:").input_cyan())
                            
                            cont = cont.lower().strip(" ")
                            
                            if cont == "y":
                                continue
                            elif cont == "e":
                            
                                end_time = time.perf_counter()
                                
                                count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                leaderboard.Leaderboard(self.username, "puzzle_one", count_time).update_leaderboard()

                                break
                            
                            else:
                                text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                continue
                            
                        else:
                            text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                            continue
        
                elif options == "2":
                    
                    time.sleep(3)
                    text.Colour(f"\n\nWhoa there, who's that fella running at you from the entrace of the mine {self.username.title()}?\n\n").cyan()
                    time.sleep(2)
                    text.Colour("[A mine worker runs up to you speaking an unknown language.]\n\n").magenta()
                    # Use Avatar class for intro speech
                    text.Colour(f"[He babbles:] {self.avatar.get_intro('railwayman_one')}\n\n").magenta()
                    time.sleep(2)
                    text.Colour("[He then hands you a piece of paper with words on it and points towards the mine.]\n\n").magenta()
                    time.sleep(2)
        
                elif options == "3":
                    
                    location.Location(self.username, "puzzle_one").get_loc_info()
                    
                elif options == "4":
                    
                    leaderboard.Leaderboard.status_bar("puzzle_one")
                    
                elif options == "e":
                    main.save_progress(self.username, "puzzle_one")
                    break
                else:
                    text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()

#==== Second Puzzle - Railway Expansion ====#

    def puzzle_two(self):
        
        time.sleep(3)
        text.Colour("\n\n[As you mosey along the rusty old railway, you hear someone shouting at you to stop.]\n\n").magenta()
        text.Colour("Who's that dusty man?\n\n").cyan()
        time.sleep(2)
        
        # Use Avatar class for intro speech
        text.Colour(f"[A railwayman runs up to you and says:]\n\n{self.avatar.get_intro('railwayman_two')}\n\n").magenta()
        time.sleep(2)
        
        # Set the required item for the puzzle
        puzzle_two_item = "hammer"
        
        # Pompting for a hint
        text.Colour(f"{self.avatar.get_prompt('railwayman_two')}\n").magenta()
        while True: 
            choice = input(text.Colour('''How'd you wana respond partner?
Yes - "y"
No - "n"
Check inventory - "c"
''').input_cyan())
            choice = choice.lower().strip(" ")
        
            if choice == "y":
                if inventory.Inventory(self.username).has_required_epuipment(puzzle_two_item):
                    time.sleep(2)
                    text.Colour(f"\n\n{self.avatar.get_hint('railwayman_two')}\n\n").magenta()
                    inventory.Inventory(self.username).update_equipment(puzzle_two_item)
                    break
                else:
                    time.sleep(2)
                    text.Colour("\n\nNow now, No need to tell a lie my friend, I see you ain't got no hammer!\n\n").cyan()
                    break
            elif choice == "n":
                time.sleep(2)
                text.Colour("\n\nOh riddens, that hammer sure would've been handy\n\n").cyan()
                break
            elif choice == "c":
                time.sleep(2)
                text.Colour(f"\n\nYour equipment: {inventory.Inventory(self.username).get_inventory_item()}\n\n").green()
                continue
            else:
                text.Colour("\nThat aint a choice my friend...Try again.\n\n").red()
                time.sleep(2)
                
        while True:
                
                options = input(text.Colour('''\nI wonder what that was all about...Maybe there's a puzzle to solve?\n\n
Solve puzzle - 1
Hear again - 2
Look around - 3
See status - 4
Save and Exit - e                           
\n''').input_cyan())
                
                options = options.lower().strip(" ")
        
                if options == "1":
                    start_time = time.perf_counter()
        
                    #Puzzle Logic
                    while True:
                        
                        text.Typed.image_two()
                        
                        answer = input(text.Colour("\nWhat's the height of the arch at the center of the railway track? Enter your answer in centimetres:\n\n").input_cyan())
                        answer = int(answer)
                        
                        try:
                            
                            if answer >= 708 and answer <= 709:
                                end_time = time.perf_counter()
                                
                                time.sleep(2)
                                text.Colour(f"\nYou've only gone and done it {self.username.title()}, seems our cart is about a metre long so we'll make it over\n").cyan()
                            
                                count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                leaderboard.Leaderboard(self.username, "puzzle_three", count_time).update_leaderboard()
                                
                                leaderboard.Leaderboard.show_Leaderboard()
                                
                                main.save_progress(self.username, "puzzle_three")
                                
                                options = input(text.Colour('''You did real well there partner!\n\nYa'll wana carry on into this here mine and rescue them miners?
Continue - "c"
Exit - "e"
:''').input_cyan())
                                options = options.lower().strip(" ")
                                
                                if options == "c":
                                    
                                    main.load_progress(self.username)
                                    return True
                                
                                elif options == "e":
                                    time.sleep(2)
                                    text.Colour("\nSorry to see you go partner! Mines aren't for the faint hearted...\n\n\n").cyan()
                                    return False
                                else:
                                    time.sleep(2)
                                    text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                    continue
                                    
                            elif answer < 708 and answer > 709:
                                
                                time.sleep(2)
                                
                                cont = input(text.Colour("Want to have another go fella?\n\nYes - \"y\"\nExit puzzle - \"e\"\n:").input_cyan())
                                
                                cont = cont.lower().strip(" ")
                                
                                if cont == "y":
                                    continue
                                elif cont == "e":
                                
                                    end_time = time.perf_counter()
                                    
                                    count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                    leaderboard.Leaderboard(self.username, "puzzle_two", count_time).update_leaderboard()
                                    
                                    break
                                
                                else:
                                    time.sleep(2)
                                    text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                    continue
                            else:
                                time.sleep(2)
                                text.Colour("\nHmm, that don't seem quite right, have another go eh?\n\n").red()
                        except ValueError:
                            time.sleep(2)
                            text.Colour("\nNow now, enter a number, not some gibberish you fool!\n\n").red() #if input is not an integer prompt to retry
                
                elif options == "2":
                    
                    time.sleep(2)
                    text.Colour("\n\n[As you mosey along the rusty old railway, you hear someone shouting at you to stop.]\n\n Who's that dusty man?\n\n").cyan()
                    time.sleep(2)
                    
                    # Use Avatar class for intro speech
                    text.Colour(f"[A railwayman runs up to you and says:]\n\n{self.avatar.get_intro('railwayman_two')}\n\n").magenta()
                    time.sleep(2)
                    
                elif options == "3":
                    
                    location.Location(self.username, "puzzle_two").get_loc_info()
                    
                elif options == "4":
                    
                    leaderboard.Leaderboard.status_bar("puzzle_two")
                    
                elif options == "e":
                    main.save_progress(self.username, "puzzle_two")
                    break
                else:
                    text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()

#==== Third Puzzle - Break the links ====#

    def puzzle_three(self):
        
        
        time.sleep(3)
        text.Colour(f"\n\nOh no {self.username.title()}! The tunnel ahead has collapsed, that's the end of this track...\n\n").cyan()
        time.sleep(2)
        text.Colour("Wait look!\n\n").cyan()
        time.sleep(2)
        text.Colour("There's just a narrow crawl space left.\n\n").cyan()
        time.sleep(2)
        text.Typed.image_three()
        time.sleep(2)
        text.Colour("[A miner hollers at ya'll from the other side of the crawl space:]\n").magenta()
        time.sleep(2)
        # Use Avatar class for intro speech
        text.Colour(f"{self.avatar.get_intro('miner_crawlspace')}\n\n").magenta()
        time.sleep(2)

        puzzle_three_item = "lasso"
        
        # Pompting for a hint
        text.Colour(f"'{self.avatar.get_prompt('miner_crawlspace')}'\n").magenta()
        while True:
            choice = input(text.Colour('''How'd you wana respond partner?
Yes - "y"
No - "n"
Check inventory - "c"
''').input_cyan())
            choice = choice.lower().strip(" ")
        
            if choice == "y":
                if inventory.Inventory(self.username).has_required_epuipment(puzzle_three_item):
                    time.sleep(2)
                    text.Colour(f"\n{self.avatar.get_hint('miner_crawlspace')}\n\n").magenta()
                    inventory.Inventory(self.username).update_equipment(puzzle_three_item)
                    break
                else:
                    time.sleep(2)
                    text.Colour("\nNow now partner, don't ya go yankin my strings, I see no lasso in sight!\n\n").red()
                    break
            elif choice == "n":
                time.sleep(2)
                text.Colour("\nI sure could've given you a hand if you had a lasso my friend\n\n").cyan()
                break
            elif choice == "c":
                time.sleep(2)
                text.Colour(f"Your equipment: {inventory.Inventory(self.username).get_inventory_item()}\n\n").green()
                continue
            else:
                text.Colour("\nThat aint a choice my friend...Try again.\n\n").red()
                time.sleep(2)

        while True:

            options = input(text.Colour('''\nI wonder what that was all about...Maybe there's a puzzle to solve?\n\n
Solve puzzle - 1
Hear again - 2
Look around - 3
See status - 4
Save and Exit - e                           
\n''').input_cyan())
                
            options = options.lower().strip(" ")
    
            if options == "1":
                start_time = time.perf_counter()
    
                #Puzzle Logic
        
                while True:
                    try:
                        time.sleep(2)
                        user_input = input(text.Colour("\nThink hard and enter the minimum number of breaks needed to fix this chain: \n").input_cyan()).strip()
                        
                        number_of_breaks = int(user_input)
                        
                        if number_of_breaks == 4:
                            
                            end_time = time.perf_counter()
                                
                            time.sleep(2)
                            text.Colour(f"\nAin't you a clever one {self.username.title()}! You're sharper than the prick of a cactus! Only 4 breaks are needed.\n\n").cyan()
                            time.sleep(2)
                            text.Colour("[The miner swiftly breaks the links, joins the chain, and pulls you through the space.]\n\n").magenta()

                            count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                            leaderboard.Leaderboard(self.username, "puzzle_four", count_time).update_leaderboard()
                            
                            leaderboard.Leaderboard.show_Leaderboard()
                            
                            main.save_progress(self.username, "puzzle_four")
                            
                            options = input(text.Colour('''You did real well there partner!\n\nYa'll wana carry on into this here mine and rescue them miners?
Continue - "c"
Exit - "e"
:''').input_cyan())
                            options = options.lower().strip(" ")
                                
                            if options == "c":
                                
                                main.load_progress(self.username)
                                return True
                            
                            elif options == "e":
                                time.sleep(2)
                                text.Colour("\nSorry to see you go partner! Mines aren't for the faint hearted...\n\n\n").cyan()
                                return False
                            else:
                                time.sleep(2)
                                text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                continue
                        
                        elif number_of_breaks != 4:
                            
                            time.sleep(2)
                            text.Colour("\nNope, that ain't it. You gotta think like you're spendin' links, not silver dollars. Try again...\n").red()

                            time.sleep(2)
                            cont = input(text.Colour("Want to have another go fella?\n\nYes - \"y\"\nExit puzzle - \"e\"\n:").input_cyan())
                            
                            cont = cont.lower().strip(" ")
                            
                            if cont == "y":
                                continue
                            elif cont == "e":
                            
                                end_time = time.perf_counter()
                                
                                count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                leaderboard.Leaderboard(self.username, "puzzle_three", count_time).update_leaderboard()
                                
                                break
                            
                        else:
                            time.sleep(2)
                            text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                            continue
                    except ValueError as e:
                        text.Colour(f"There was an error in the value: {e}").red()
                    except Exception as e:
                        text.Colour(f"There was an unknown error: {e}").red()
            
            elif options == "2":
                
                time.sleep(3)
                text.Colour(f"\n\nOh no {self.username.title()}! The tunnel ahead has collapsed, that's the end of this track...\n\n").cyan()
                time.sleep(2)
                text.Colour("Wait look!\n\n").cyan()
                time.sleep(2)
                text.Colour("There's just a narrow crawl space left.\n\n").cyan()
                time.sleep(2)
                text.Colour("[A miner hollers at ya'll from the other side of the crawl space:]\n").magenta()
                time.sleep(2)
                # Use Avatar class for intro speech
                text.Colour(f"{self.avatar.get_intro('miner_crawlspace')}\n\n").magenta()
                time.sleep(2)
                
            elif options == "3":
                
                location.Location(self.username, "puzzle_three").get_loc_info()
                
            elif options == "4":
                
                leaderboard.Leaderboard.status_bar("puzzle_three")
                
            elif options == "e":
                main.save_progress(self.username, "puzzle_three")
                break
            else:
                text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()

#==== Fourth Puzzle - Cross the lake ====#

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
        text.Typed.image_four()
        time.sleep(2)
        text.Colour("\nI reckon ya'll gotta get em all across to the other side before the whole place floods!\n\n").cyan()
        time.sleep(2)
        
        # Use Avatar class for intro speech
        text.Colour(f"[The jittery miner stumbles up to you:]\n{self.avatar.get_intro('miner_two')}\n\n").magenta()
        time.sleep(2)
        
        puzzle_four_item = "mask"
        
        text.Colour('''What in the name ya'll gona do??
Your actions are:
A - Take Rat Across/Back
B - Take Dynamite Across/Back
C - Take Miner Across/Back
D - Take Nothing Across/Back
''').magenta()
        
        # Pompting for a hint
        time.sleep(3)
        text.Colour(f"{self.avatar.get_prompt('miner_two')}\n\n\n").magenta()
        while True: 
            choice = input(text.Colour('''How'd you wana respond partner?
Yes - "y"
No - "n"
Check inventory - "c"
''').input_cyan())
            choice = choice.lower().strip(" ")        
            if choice == "y":
                if inventory.Inventory(self.username).has_required_epuipment(puzzle_four_item):
                    time.sleep(2)
                    text.Colour(f"{self.avatar.get_hint('miner_two')}\n\n").magenta()
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
            elif choice == "c":
                time.sleep(2)
                text.Colour(f"Your equipment: {inventory.Inventory(self.username).get_inventory_item()}\n\n").green()
                continue
            else:
                text.Colour("\nThat aint a choice my friend...Try again.\n\n").red()
                time.sleep(2)        
        
        leave_puzzle = False
        
        while True:
            leave_puzzle = False
            time.sleep(2)
            options = input(text.Colour('''\nI wonder what that was all about...Maybe there's a puzzle to solve?\n\n
Solve puzzle - 1
Hear again - 2
Look around - 3
See status - 4
Save and Exit - e                           
\n''').input_cyan())
        
            options = options.lower().strip(" ")
            solution = {1 : ["b","B"],
                    2 : ["d", "D"],
                    3 : ["a", "A", "c", "C"],
                    4 : ["b", "B"],
                    5 : ["c", "C", "a", "A"],
                    6 : ["d", "D"],
                    7 : ["b", "B"]
                    }  # The correct sequence of actions
        
        # Puzzle Logic
            if options == "1":
            
                while True:
                    
                    if leave_puzzle == True:
                       break
                    else:
                        
                        start_time = time.perf_counter()
                        answer = input(text.Colour("\nTime's wastin', enter yer moves one at a time friend. Real slow-like (A/B/C/D)\nRemember you can't take everyone across at once!\n:").input_cyan())
                        answer = answer.strip(" ")
                    
                        if answer in solution[1]:
                            
                            text.Colour(f"\nThat's a good start {self.username.title()}.\n").cyan()
                            
                            while True:
                                
                                if leave_puzzle == True:
                                   break
                                else:
                                
                                    text.Colour("\nYa'll got:\nB - Take Dynamite Across/Back.\n").cyan()
                                    
                                    answer = input(text.Colour("\nTime's wastin', enter yer moves one at a time friend. Real slow-like (A/B/C/D)\nRemember you can't take everyone across at once!\n:").input_cyan())
                                    answer = answer.lower().strip(" ")
                                    
                                    if answer in solution[2]:
                                        
                                        text.Colour(f"\nKeep it up {self.username.title()}.\n").cyan()
                                    
                                        while True:
                                            
                                            if leave_puzzle == True:
                                               break
                                            else:
                                  
                                                text.Colour("\nYa'll got:\nB - Take Dynamite Across/Back.\nD - Take Nothing Across/Back.\n").cyan()
                                                
                                                answer = input(text.Colour("\nTime's wastin', enter yer moves one at a time friend. Real slow-like (A/B/C/D)\nRemember you can't take everyone across at once!\n:").input_cyan())
                                                answer = answer.lower().strip(" ")
                                                
                                                if answer in solution[3]:
                                                    
                                                    text.Colour(f"\nKeep it up {self.username.title()}.\n").cyan()
                                                    
                                                    while True:
                                                        
                                                        if leave_puzzle == True:
                                                           break
                                                        else:
                                                        
                                                            text.Colour("\nYa'll got:\nB - Take Dynamite Across/Back.\nD - Take Nothing Across/Back.\nA/C - Take Rat or Miner Across/Back.\n").cyan()
                                                            
                                                            answer = input(text.Colour("\nTime's wastin', enter yer moves one at a time friend. Real slow-like (A/B/C/D)\nRemember you can't take everyone across at once!\n:").input_cyan())
                                                            answer = answer.lower().strip(" ")
                                                        
                                                            if answer in solution[4]:
                                                                
                                                                text.Colour(f"\nKeep it up {self.username.title()}.\n").cyan()
                                                                
                                                                while True:
                                                                    
                                                                    if leave_puzzle == True:
                                                                       break
                                                                    else:
                                                                        
                                                                        text.Colour("\nYa'll got:\nB - Take Dynamite Across/Back.\nD - Take Nothing Across/Back.\nA/C - Take Rat or Miner Across/Back.\nB - Take Dynamite Across/Back.\n").cyan()
                                                                        
                                                                        answer = input(text.Colour("\nTime's wastin', enter yer moves one at a time friend. Real slow-like (A/B/C/D)\nRemember you can't take everyone across at once!\n:").input_cyan())
                                                                        answer = answer.lower().strip(" ")
                                                                        
                                                                        if answer in solution[5]:
                                                                            
                                                                            text.Colour(f"\nKeep it up {self.username.title()}.\n").cyan()
                                                                            
                                                                            while True:
                                                                                
                                                                                if leave_puzzle == True:
                                                                                   break
                                                                                else:
                                                                            
                                                                                    text.Colour("\nYa'll got:\nB - Take Dynamite Across/Back.\nD - Take Nothing Across/Back.\nA/C - Take Rat or Miner Across/Back.\nB - Take Dynamite Across/Back.\nA/C - Take Rat or Miner Across/Back.\n").cyan()
                                                                                    
                                                                                    answer = input(text.Colour("\nTime's wastin', enter yer moves one at a time friend. Real slow-like (A/B/C/D)\nRemember you can't take everyone across at once!\n:").input_cyan())
                                                                                    answer = answer.lower().strip(" ")
                                
                                                                                    if answer in solution[6]:
                                                                                        
                                                                                        text.Colour(f"\nKeep it up {self.username.title()}.\n").cyan()
                                                                                        
                                                                                        while True:
                                                                                            
                                                                                            if leave_puzzle == True:
                                                                                               break
                                                                                            else:
                                                                                            
                                                                                                text.Colour("\nYa'll got:\nB - Take Dynamite Across/Back.\nD - Take Nothing Across/Back.\nA/C - Take Rat or Miner Across/Back.\nB - Take Dynamite Across/Back.\nA/C - Take Rat or Miner Across/Back.\nD - Take Nothing Across/Back.\n").cyan()
                                                                                                answer = input(text.Colour("\nTime's wastin', enter yer moves one at a time friend. Real slow-like (A/B/C/D)\nRemember you can't take everyone across at once!\n:").input_cyan())
                                                                                                answer = answer.lower().strip(" ")
                                    
                                                                                                if answer in solution[7]:
                                                                                                            
                                                                                                    end_time = time.perf_counter()
                                                                                                    puzzle_four_completed = True
                                                                                                    time.sleep(2)
                                                                                                    text.Colour(f"\nYeehaw! Ya did it {self.username.title()}! All safe and sound on t'other side.\n\n").cyan()
                                                                                                    time.sleep(2)
                                                                                                    text.Colour("\nYa'll got:\nB - Take Dynamite Across/Back.\nD - Take Nothing Across/Back.\nA/C - Take Rat or Miner Across/Back.\nB - Take Dynamite Across/Back.\nA/C - Take Rat or Miner Across/Back.\nD - Take Nothing Across/Back.\nB - Take Dynamite Across/Back.\n").cyan()
                                                                                                    
                                                                                                    # Save progress and update time and leaderboard
                                                                                                    count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                                                                                    leaderboard.Leaderboard(self.username, "puzzle_five", count_time).update_leaderboard()
                                                                                                    
                                                                                                    leaderboard.Leaderboard.show_Leaderboard()
                                                                                                    
                                                                                                    main.save_progress(self.username, "puzzle_five")
                                                                                            
                                                                                                    options = input(text.Colour('''You did real well there partner!\n\nYa'll wana carry on into this here mine and rescue them miners?
Continue - "c"
Exit - "e"
:''').input_cyan())
                                                                                                    options = options.lower().strip(" ")
                                                                                                        
                                                                                                    if options == "c":
                                                                                                        
                                                                                                        main.load_progress(self.username)
                                                                                                        return False
                                                                                                    
                                                                                                    elif options == "e":
                                                                                                        time.sleep(2)
                                                                                                        text.Colour("\nSorry to see you go partner! Mines aren't for the faint hearted...\n\n\n").cyan()
                                                                                                        return False
                                                                                                    else:
                                                                                                        time.sleep(2)
                                                                                                        text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                                                                                        continue
                                                                                                    break
                                                                    
                                                                                                elif answer not in solution[7]:
                                                                                                    
                                                                                                    time.sleep(2)
                                                                                                    text.Colour("\nThat don't sound quite right, we ain't got forever...\n\n").red()
                                                                                                    time.sleep(1)
                                                                                                    
                                                                                                    cont = input(text.Colour("Want to have another go fella?\n\nYes - \"y\"\nExit puzzle - \"e\"\n:").input_cyan())
                                                                                                    cont = cont.lower().strip(" ")
                                                                                                    
                                                                                                    if cont == "y":
                                                                                                        continue
                                                                                                    elif cont == "e":
                                                                                                        end_time = time.perf_counter()
                                    
                                                                                                        time.sleep(1)
                                                                                                        text.Colour("\n\nReckon the gas hurt'n ya brain my friend.\n").red()
                                                                                                        time.sleep(2)
                                                                                                        
                                                                                                        count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                                                                                        leaderboard.Leaderboard(self.username, "puzzle_four", count_time).update_leaderboard()
                                                                                                        leave_puzzle = True
                                                                                                    
                                                                                                    else:
                                                                                                        time.sleep(1)
                                                                                                        text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                                                                                        continue
                                                                                            
                                                                                    elif answer not in solution[6]:
                                                                                        
                                                                                        time.sleep(2)
                                                                                        text.Colour("\nThat don't sound quite right, we ain't got forever...\n\n").red()
                                                                                        time.sleep(1)
                                                                                        
                                                                                        cont = input(text.Colour("Want to have another go fella?\n\nYes - \"y\"\nExit puzzle - \"e\"\n:").input_cyan())
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
                                                                                            text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                                                                            continue
                                                                                
                                                                        elif answer not in solution[5]:
                                                                            
                                                                            time.sleep(2)
                                                                            text.Colour("\nThat don't sound quite right, we ain't got forever...\n\n").red()
                                                                            time.sleep(1)
                                                                            
                                                                            cont = input(text.Colour("Want to have another go fella?\n\nYes - \"y\"\nExit puzzle - \"e\"\n:").input_cyan())
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
                                                                                text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                                                                continue
                                                            elif answer not in solution[4]:
                                                                
                                                                time.sleep(2)
                                                                text.Colour("\nThat don't sound quite right, we ain't got forever...\n\n").red()
                                                                time.sleep(1)
                                                                
                                                                cont = input(text.Colour("Want to have another go fella?\n\nYes - \"y\"\nExit puzzle - \"e\"\n:").input_cyan())
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
                                                                    text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                                                    continue
                                                elif answer not in solution[3]:
                                                    
                                                    time.sleep(2)
                                                    text.Colour("\nThat don't sound quite right, we ain't got forever...\n\n").red()
                                                    time.sleep(1)
                                                    
                                                    cont = input(text.Colour("Want to have another go fella?\n\nYes - \"y\"\nExit puzzle - \"e\"\n:").input_cyan())
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
                                                        text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                                        continue
                                            
                                    elif answer not in solution[2]:
                                        
                                        time.sleep(2)
                                        text.Colour("\nThat don't sound quite right, we ain't got forever...\n\n").red()
                                        time.sleep(1)
                
                                        cont = input(text.Colour("Want to have another go fella?\n\nYes - \"y\"\nExit puzzle - \"e\"\n:").input_cyan())
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
                                            text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                            continue
                                    
                        elif answer not in solution[1]:
                            
                            time.sleep(2)
                            text.Colour("\nThat don't sound quite right, we ain't got forever...\n\n").red()
                            time.sleep(1)
                            
                            cont = input(text.Colour("Want to have another go fella?\n\nYes - \"y\"\nExit puzzle - \"e\"\n:").input_cyan())
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
                                text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                continue
                        
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
                
                # Use Avatar class for intro speech
                text.Colour(f"[The jittery miner stumbles up to you:]\n{self.avatar.get_intro('miner_two')}\n\n").magenta()
                time.sleep(2)
                
                text.Colour('''What in the name ya'll gona do??
        Your actions are:
        A - Take Rat Across
        B - Take Dynamite Across
        C - Take Miner Across
        D - Take Nothing Across
        ''').magenta()
                 
            elif options == "3":
                 
                 location.Location(self.username, "puzzle_four").get_loc_info()
                 
            elif options == "4":
                 
                 leaderboard.Leaderboard.status_bar("puzzle_four")
                 
            elif options == "e":
                
                main.save_progress(self.username, "puzzle_four")
                break
            else:
                 text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()

#==== Fifth Puzzle - Lift shaft ====#

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
        # Use Avatar class for intro speech
        text.Colour("[Some minutes later...]\n\n").magenta()
        time.sleep(3)
        text.Colour("Look, it's a lift shaft\n\n\nYou fellas alright down there?\n\n").cyan()
        time.sleep(2)
        text.Typed.image_five()
        time.sleep(3)
        
        #Avatar class for intro
        text.Colour(f"Boy are we glad to see you!\n\n{self.avatar.get_intro('trapped_miner')}\n").magenta()
        time.sleep(3)
        
        puzzle_five_item = "notebook" 
        
        text.Colour(f"{self.avatar.get_prompt('trapped_miner')}\n\n").magenta()
        
        while True: 
            choice = input(text.Colour('''How'd you wana respond partner?
Yes - "y"
No - "n"
Check inventory - "c"
''').input_cyan())
            choice = choice.lower().strip(" ")
            
            if choice == "y":
                if inventory.Inventory(self.username).has_required_epuipment(puzzle_five_item):
                    time.sleep(2)
                    text.Colour(f"{self.avatar.get_hint('trapped_miner')}\n\n").magenta()
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
            elif choice == "c":
                time.sleep(2)
                text.Colour(f"Your equipment: {inventory.Inventory(self.username).get_inventory_item()}\n\n").green()
                continue
            else:
                text.Colour("\nThat aint a choice my friend...Try again.\n\n").red()
                time.sleep(2)        
        
        #Puzzle logic
        
        while True:
                    
            options = input(text.Colour('''\nSeems like a tricky puzzle partner... What do ya'll wana do?
Solve puzzle - 1
Hear again - 2
Look around - 3
See status - 4
Save and Exit - e                           
\n''').input_cyan())
            
            options = options.lower().strip(" ")
            
            solution = {1 : ["98-7", "98 - 7", "98- 7", "98 -7", 98-7],
                        2 : ["-6", "- 6", -6],
                        3 : ["+5", "+ 5", +5],
                        4 : ["+4", "+ 4", +4],
                        5 : ["+3", "+ 3", +3],
                        6 : ["+2", "+ 2", +2],
                        7 : ["+1", "+ 1", +1]}
            
            if options == "1":
                
                while True:
                    start_time = time.perf_counter()
                    answer = input(text.Colour("\nSo what's your answer partner?\n\nYou got 98, 7, 6, 5, 4, 3, 2, 1, and as many + and - as ya'll want to work with\n\nEnter each operation at a time:").input_cyan())
                    answer = answer.lower().strip(" ")
                
                    if answer in solution[1]:
                        
                        text.Colour(f"\nThat's a good start {self.username.title()}.\n").cyan()
                        
                        while True:
                            
                            text.Colour("\nYa'll got 91.\n").cyan()
                            
                            answer = input(text.Colour("\nWhat next partner?\n\nYou got 6, 5, 4, 3, 2, 1, and as many + and - as ya'll want to work with\n\nEnter one stage at a time:").input_cyan())
                            answer = answer.lower().strip(" ")
                            
                            if answer in solution[2]:
                                
                                text.Colour(f"\nKeep it up {self.username.title()}.\n").cyan()
                                
                                while True:
                                    
                                    text.Colour("\nYa'll got 85.\n").cyan()
                                    
                                    answer = input(text.Colour("\nWhat next partner??\n\nYou got 5, 4, 3, 2, 1, and as many + and - as ya'll want to work with\n\nEnter one stage at a time:").input_cyan())
                                    answer = answer.lower().strip(" ")
                                
                                    if answer in solution[3]:
                                        
                                        text.Colour(f"\nKeep it up {self.username.title()}.\n").cyan()
                                        
                                        while True:
                                            
                                            text.Colour("\nYa'll got 90.\n").cyan()
                                            
                                            answer = input(text.Colour("\nWhat next partner??\n\nYou got 4, 3, 2, 1,and as many + and - as ya'll want to work with\n\nEnter one stage at a time:").input_cyan())
                                            answer = answer.lower().strip(" ")
                                            
                                            if answer in solution[4]:
                                                
                                                text.Colour(f"\nKeep it up {self.username.title()}.\n").cyan()
                                                
                                                while True:
                                                
                                                    text.Colour("\nYa'll got 94.\n").cyan()
                                                    
                                                    answer = input(text.Colour("\nWhat next partner??\n\nYou got 3, 2, 1, and as many + and - as ya'll want to work with\n\nEnter one stage at a time:").input_cyan())
                                                    answer = answer.lower().strip(" ")

                                                    if answer in solution[5]:
                                                        
                                                        text.Colour(f"\nKeep it up {self.username.title()}.\n").cyan()
                                                        
                                                        while True:
                                                            
                                                            text.Colour("\nYa'll got 97.\n").cyan()
                                                            answer = input(text.Colour("\nWhat next partner?\n\nYou got 2, 1, and as many + and - as ya'll want to work with\n\nEnter one stage at a time:").input_cyan())
                                                            answer = answer.lower().strip(" ")

                                                            if answer in solution[6]:
                                                                
                                                                text.Colour(f"\nKeep it up {self.username.title()}.\n").cyan()
                                                                
                                                                while True:
                                                                    
                                                                    text.Colour("\nYa'll got 99.\n").cyan()
                                                                    
                                                                    answer = input(text.Colour("\nWhat next partner?\n\nYou got 1, and as many + and - as ya'll want to work with\n\nEnter one stage at a time:").input_cyan())
                                                                    answer = answer.lower().strip(" ")
                                                                    
                                                                    if answer in solution[7]:
                                                                        
                                                                        text.Colour(f"\nGREAT WORK {self.username.title()}!\n").cyan()
                                                                        text.Colour("\nYa'll got 100.\n").cyan()
                                                            
                                                                        end_time = time.perf_counter()
                                                                        
                                                                        count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                                                        leaderboard.Leaderboard(self.username, "finished", count_time).update_leaderboard()
                                                                        
                                                                        main.save_progress(self.username, "finished")
                                                                                        
                                                                        text.Colour(f"YOU DID IT {self.username.title()}!\n\n\n").cyan()
                                                                        time.sleep(4)                       
                                                                        text.Colour(f"{self.avatar.get_outro('trapped_miner')}\n\n\n").magenta()
                                                                        
                                                                        leaderboard.Leaderboard.status_bar("finished")
                                                                        
                                                                        leaderboard.Leaderboard.show_Leaderboard()
                                                                        
                                                                        return False
                                                                    
                                                                    elif answer not in solution[7]:
                                                                        
                                                                        time.sleep(2)
                                                                        text.Colour("That don't sound quite right, we ain't got forever...\n\n").red()
                                                
                                                                        time.sleep(2)
                                                                        cont = input(text.Colour("Want to have another go fella?\n\nYes - \"y\"\nExit puzzle - \"e\"\n:").input_cyan())
                                                                        
                                                                        cont = cont.lower().strip(" ")
                                                                        
                                                                        if cont == "y":
                                                                            continue
                                                                        elif cont == "e":
                                                                        
                                                                            end_time = time.perf_counter()
                                                                            
                                                                            count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                                                            leaderboard.Leaderboard(self.username, "puzzle_five", count_time).update_leaderboard()
                                                                            
                                                                            break
                                                                        
                                                                        else:
                                                                            time.sleep(1)
                                                                            text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                                                            continue
                                                                            
                                                            elif answer not in solution[6]:
                                                                
                                                                time.sleep(2)
                                                                text.Colour("That don't sound quite right, we ain't got forever...\n\n").red()
                                        
                                                                time.sleep(2)
                                                                cont = input(text.Colour("Want to have another go fella?\n\nYes - \"y\"\nExit to start menu - \"e\"\n:").input_cyan())
                                                                
                                                                cont = cont.lower().strip(" ")
                                                                
                                                                if cont == "y":
                                                                    continue
                                                                elif cont == "e":
                                                                
                                                                    end_time = time.perf_counter()
                                                                    
                                                                    count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                                                    leaderboard.Leaderboard(self.username, "puzzle_five", count_time).update_leaderboard()
                                                                    
                                                                    break
                                                                else:
                                                                    time.sleep(1)
                                                                    text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                                                    continue
                                                            
                                                    elif answer not in solution[5]:
                                                        
                                                        time.sleep(2)
                                                        text.Colour("That don't sound quite right, we ain't got forever...\n\n").red()
                                
                                                        time.sleep(2)
                                                        cont = input(text.Colour("Want to have another go fella?\n\nYes - \"y\"\nExit to start menu - \"e\"\n:").input_cyan())
                                                        
                                                        cont = cont.lower().strip(" ")
                                                        
                                                        if cont == "y":
                                                            continue
                                                        elif cont == "e":
                                                        
                                                            end_time = time.perf_counter()
                                                            
                                                            count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                                            leaderboard.Leaderboard(self.username, "puzzle_five", count_time).update_leaderboard()
                                                            
                                                            break
                                                        else:
                                                            time.sleep(1)
                                                            text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                                            continue
                                                
                                            elif answer not in solution[4]:
                                                
                                                time.sleep(2)
                                                text.Colour("That don't sound quite right, we ain't got forever...\n\n").red()
                        
                                                time.sleep(2)
                                                cont = input(text.Colour("Want to have another go fella?\n\nYes - \"y\"\nExit to start menu - \"e\"\n:").input_cyan())
                                                
                                                cont = cont.lower().strip(" ")
                                                
                                                if cont == "y":
                                                    continue
                                                elif cont == "e":
                                                
                                                    end_time = time.perf_counter()
                                                    
                                                    count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                                    leaderboard.Leaderboard(self.username, "puzzle_five", count_time).update_leaderboard()
                                                    
                                                    break
                                                else:
                                                    time.sleep(1)
                                                    text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                                    continue
                                        
                                    elif answer not in solution[3]:
                                        
                                        time.sleep(2)
                                        text.Colour("That don't sound quite right, we ain't got forever...\n\n").red()
                
                                        time.sleep(2)
                                        cont = input(text.Colour("Want to have another go fella?\n\nYes - \"y\"\nExit to start menu - \"e\"\n:").input_cyan())
                                        
                                        cont = cont.lower().strip(" ")
                                        
                                        if cont == "y":
                                            continue
                                        elif cont == "e":
                                        
                                            end_time = time.perf_counter()
                                            
                                            count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                            leaderboard.Leaderboard(self.username, "puzzle_five", count_time).update_leaderboard()
                                            
                                            break
                                        else:
                                            time.sleep(1)
                                            text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                            continue
                                
                            elif answer not in solution[2]:
                                
                                time.sleep(2)
                                text.Colour("That don't sound quite right, we ain't got forever...\n\n").red()
        
                                time.sleep(2)
                                cont = input(text.Colour("Want to have another go fella?\n\nYes - \"y\"\nExit to start menu - \"e\"\n:").input_cyan())
                                
                                cont = cont.lower().strip(" ")
                                
                                if cont == "y":
                                    continue
                                elif cont == "e":
                                
                                    end_time = time.perf_counter()
                                    
                                    count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                    leaderboard.Leaderboard(self.username, "puzzle_five", count_time).update_leaderboard()
                                    
                                    break
                                else:
                                    time.sleep(1)
                                    text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                                    continue
                        
                    elif answer not in solution[1]:
                        
                        time.sleep(2)
                        text.Colour("That don't sound quite right, we ain't got forever...\n\n").red()
    
                        time.sleep(2)
                        cont = input(text.Colour("Want to have another go fella?\n\nYes - \"y\"\nExit to start menu - \"e\"\n:").input_cyan())
                        
                        cont = cont.lower().strip(" ")
                        
                        if cont == "y":
                            continue
                        elif cont == "e":
                            
                            end_time = time.perf_counter()
                            
                            count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                            leaderboard.Leaderboard(self.username, "puzzle_five", count_time).update_leaderboard()
                            
                            break
                        else:
                            time.sleep(1)
                            text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
                            continue

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
                # Use Avatar class for intro speech
                text.Colour("[Some minutes later...]\n\n").magenta()
                time.sleep(3)
                text.Colour("Look, it's a lift shaft\n\n\nYou fellas alright down there?\n\n").cyan()
                time.sleep(2)
                text.Typed.image_five()
                time.sleep(3)
                
                #Avatar class for intro
                text.Colour(f"Boy are we glad to see you!\n\n{self.avatar.get_intro('trapped_miner')}\n").magenta()
                time.sleep(3)
                
            elif options == "3":
                
                location.Location(self.username, "puzzle_five").get_loc_info()
                
            elif options == "4":
                
                leaderboard.Leaderboard.status_bar("puzzle_five")
                
            elif options == "e":
                main.save_progress(self.username, "puzzle_five")
                break
            else:
                text.Colour("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n").red()
"""
This is the puzzle class file.

"""
import random
import time
import avatar
import mine_rescue_main as main
import location
import leaderboard

class Puzzle:
    
    def __init__(self, username):
        self.username = username
        self.avatar = avatar.Avatar()

#==== Show player inventory to check for equipment ====#

    def get_inventory_item(self):
        with open('characters.txt', 'r') as char_file:
            for line in char_file:
                line_parts = line.strip().split(',')
                if line_parts[0].strip() == self.username:
                    return line_parts[-2].strip()
        # Return a default message if no item is found
        return "No item found"
    
#==== Check if the user has the required item ====#

    def has_required_epuipment(self, required_item):
           
           return required_item in self.get_inventory_item()

#==== Set the equipment to default "None" once it's been used in a puzzle ====#

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
        
        
        time.sleep(8)
        print(f"\n\nWhoa there, who's that fella running at you from the entrace of the mine {self.username.title()}?\n\n")
        time.sleep(4)
        print("[A mine worker runs up to you speaking an unknown language.]\n\n")
        # Use Avatar class for intro speech
        print(f"[He babbles:] {self.avatar.get_intro('railwayman_one')}\n\n")
        time.sleep(4)
        print("[He then hands you a piece of paper with words on it and points towards the mine.]\n\n")
        time.sleep(5)
                
        original_sentence = "To make your way into the tunnel, you\'re gona need to get on a MINECART"
        answer = "minecart"


        while True:
                
                options = input('''\nI wonder what that was all about...Maybe there's a puzzle to solve?\n\n
Solve puzzle - 1
Hear again - 2
Look around - 3
See status - 4
Save and Exit - e                           
\n''')
                
                options = options.lower().strip(" ")
        
                if options == "1":
                    start_time = time.perf_counter()
                    print(start_time)
                    
                    while True:
                        shift = random.randint(1, 25)  # Random shift value
                        ciphered_text = self.caesar_cipher(original_sentence, shift)
                        print(f"[The writing says:]'{ciphered_text}'\n\n\n")
                        
                        time.sleep(5)
                        
                        user_input = input("Looks like you gotta make some sense of this and figure out the key word\nEnter the key:\n\n\n").strip().lower()
                        
                        time.sleep(5)
                        

                        if user_input == answer:
                            
                            end_time = time.perf_counter()
                            print(end_time)
                            print(f"\nWell done {self.username.title()}! You found the way.\n\n\n")
                            
                            count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                            leaderboard.Leaderboard(self.username, "puzzle_two", count_time).update_leaderboard()
                            
                            leaderboard.Leaderboard.show_Leaderboard()
                            
                            main.save_progress(self.username)
                            
                            options = input('''You did real well there partner!\n\nYa'll wana carry on into this here mine and rescue them miners?
Continue - "c"
Exit - "e"
:''')
                            options = options.lower().strip(" ")
                            
                            if options == "c":
                                
                                main.load_progress(self.username)
                                return True
                            
                            elif options == "e":
                                time.sleep(2)
                                print("\nSorry to see you go partner! Mines aren't for the faint hearted...\n\n\n")
                                break
                            
                            else:
                                time.sleep(2)
                                print("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n")
                                continue
                                
                        elif user_input != answer:
                            
                            print("Oh dust!, the writing changed?!\n\n\n")
                            
                            time.sleep(3)
                            
                            cont = input("Want to have another go fella?\n\nYes - \"y\"\nNo - \"n\"\n:")
                            
                            cont = cont.lower().strip(" ")
                            
                            if cont == "y":
                                continue
                            elif cont == "n":
                            
                                end_time = time.perf_counter()
                                
                                count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                leaderboard.Leaderboard.update_leaderboard(self.username, "puzzle_one", count_time)
                                
                                break
                            
                            else:
                                print("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n")
                                continue
                            
                        else:
                            print("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n")
                            continue
        
                elif options == "2":
                    
                     print(f"Whoa there, who's that fella running at you from the entrace of the mine {self.username.title()}?\n\n")
                     time.sleep(4)
                     print("[A mine worker runs up to you speaking an unknown language.]\n\n")
                     # Use Avatar class for intro speech
                     print(f"[He babbles:] {self.avatar.get_intro('railwayman_one')}\n\n")
                     time.sleep(4)
                     print("[He then hands you a piece of paper with words on it and points towards the mine.]\n\n")
                     time.sleep(5)
        
                elif options == "3":
                    
                    location.get_loc_info("puzzle_one")
                    
                elif options == "4":
                    
                    leaderboard.Leaderboard.status_bar("puzzle_one")
                    
                elif options == "e":
                    main.save_progress(self.username)
                    break
                else:
                    print("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n")

#==== Second Puzzle - Railway Expansion ====#

    def puzzle_two(self):
        
        time.sleep(8)
        print("\n\n[As you mosey along the rusty old railway, you hear someone shouting at you to stop.]\n\n Who's that dusty man?\n\n")
        time.sleep(4)
        
        # Use Avatar class for intro speech
        print(f"[A railwayman runs up to you and says:]\n\n{self.avatar.get_intro('railwayman_two')}\n\n")
        time.sleep(3)
        
        # Set the required item for the puzzle
        puzzle_two_item = "hammer"
        
        # Pompting for a hint
        print(f"{self.avatar.get_prompt('railwayman_two')}\n")
        while True: 
            choice = input('''How'd you wana respond partner?
Yes - "y"
No - "n"
Check inventory - "c"
''')
            choice = choice.lower().strip(" ")
        
            if choice == "y":
                if self.has_required_epuipment(puzzle_two_item):
                    time.sleep(3)
                    print(f"\n\n{self.avatar.get_hint('railwayman_two')}\n\n")
                    self.update_equipment()
                    break
                else:
                    time.sleep(3)
                    print("\n\nNow now, No need to tell a lie my friend, I see you ain't got no hammer!\n\n")
                    break
            elif choice == "n":
                time.sleep(3)
                print("\n\nOh riddens, that hammer sure would've been handy\n\n")
                break
            elif choice == "c":
                time.sleep(3)
                print(f"\n\nYour equipment: {self.get_inventory_item()}\n\n")
                continue
            else:
                print("\nThat aint a choice my friend...Try again.\n\n")
                time.sleep(6)
                
        while True:
                
                options = input('''\nI wonder what that was all about...Maybe there's a puzzle to solve?\n\n
Solve puzzle - 1
Hear again - 2
Look around - 3
See status - 4
Save and Exit - e                           
\n''')
                
                options = options.lower().strip(" ")
        
                if options == "1":
                    start_time = time.perf_counter()
        
                    #Puzzle Logic
                    while True:
                        
                        answer = input("\nWhat's the height of the arch at the center of the railway track? Enter your answer in centimetres:\n\n")
                        answer = int(answer)
                        
                        try:
                            
                            if answer >= 708 or answer <= 709:
                                end_time = time.perf_counter()
                                
                                time.sleep(3)
                                print(f"\nYou've only gone and done it {self.username.title()}, seems our cart is about a metre long so we'll make it over\n")
                            
                                count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                leaderboard.Leaderboard.update_leaderboard(self.username, "puzzle_three", count_time)
                                
                                leaderboard.Leaderboard.show_Leaderboard()
                                
                                main.save_progress(self.username)
                                
                                options = input('''You did real well there partner!\n\nYa'll wana carry on into this here mine and rescue them miners?
Continue - "c"
Exit - "e"
:''')
                                options = options.lower().strip(" ")
                                
                                if options == "c":
                                    
                                    main.load_progress(self.username)
                                    return True
                                
                                elif options == "e":
                                    time.sleep(2)
                                    print("\nSorry to see you go partner! Mines aren't for the faint hearted...\n\n\n")
                                    break
                                else:
                                    time.sleep(2)
                                    print("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n")
                                    continue
                                    
                            elif answer < 708 or answer >709:
                                
                                time.sleep(3)
                                
                                cont = input("Want to have another go fella?\n\nYes - \"y\"\nNo - \"n\"\n:")
                                
                                cont = cont.lower().strip(" ")
                                
                                if cont == "y":
                                    continue
                                elif cont == "n":
                                
                                    end_time = time.perf_counter()
                                    
                                    count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                    leaderboard.Leaderboard.update_leaderboard(self.username, "puzzle_two", count_time)
                                    
                                    break
                                
                                else:
                                    time.sleep(2)
                                    print("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n")
                                    continue
                            else:
                                time.sleep(3)
                                print("\nHmm, that don't seem quite right, have another go eh?\n\n")
                        except ValueError:
                            time.sleep(2)
                            print("\nNow now, enter a number, not some gibberish you fool!\n\n") #if input is not an integer prompt to retry
                
                elif options == "2":
                    
                    time.sleep(8)
                    print("\n\n[As you mosey along the rusty old railway, you hear someone shouting at you to stop.]\n\n Who's that dusty man?\n\n")
                    time.sleep(4)
                    
                    # Use Avatar class for intro speech
                    print(f"[A railwayman runs up to you and says:]\n\n{self.avatar.get_intro('railwayman_two')}\n\n")
                    time.sleep(3)
                    
                elif options == "3":
                    
                    location.get_loc_info("puzzle_two")
                    
                elif options == "4":
                    
                    leaderboard.Leaderboard.status_bar("puzzle_two")
                    
                elif options == "e":
                    main.save_progress(self.username)
                    break
                else:
                    print("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n")

#==== Third Puzzle - Break the links ====#

    def puzzle_three(self):
        
        
        time.sleep(8)
        print(f"\n\nOh no {self.username.title()}! The tunnel ahead has collapsed, that's the end of this track...\n\n")
        time.sleep(5)
        print("Wait look!\n\n")
        time.sleep(4)
        print("There's just a narrow crawl space left.\n\n")
        time.sleep(3)
        print("[A miner hollers at ya'll from the other side of the crawl space:\n")
        time.sleep(2)
        # Use Avatar class for intro speech
        print(f"{self.avatar.get_intro('miner_crawlspace')}\n\n")
        time.sleep(12)

        puzzle_three_item = "lasso"
        
        # Pompting for a hint
        print(f"'{self.avatar.get_prompt('miner_crawlspace')}'\n")
        while True:
            choice = input('''How'd you wana respond partner?
Yes - "y"
No - "n"
Check inventory - "c"
''')
            choice = choice.lower().strip(" ")
        
            if choice == "y":
                if self.has_required_epuipment(puzzle_three_item):
                    time.sleep(3)
                    print(f"\n{self.avatar.get_hint('miner_crawlspace')}\n\n")
                    self.update_equipment()
                    break
                else:
                    time.sleep(3)
                    print("\nNow now partner, don't ya go yankin my strings, I see no lasso in sight!\n\n")
                    break
            elif choice == "n":
                time.sleep(3)
                print("\nI sure could've given you a hand if you had a lasso my friend\n\n")
                break
            elif choice == "c":
                time.sleep(3)
                print(f"Your equipment: {self.get_inventory_item()}\n\n")
                continue
            else:
                print("\nThat aint a choice my friend...Try again.\n\n")
                time.sleep(3)

        while True:

            options = input('''\nI wonder what that was all about...Maybe there's a puzzle to solve?\n\n
Solve puzzle - 1
Hear again - 2
Look around - 3
See status - 4
Save and Exit - e                           
\n''')
                
            options = options.lower().strip(" ")
    
            if options == "1":
                start_time = time.perf_counter()
    
                #Puzzle Logic
        
                while True:
                    try:
                        time.sleep(3)
                        user_input = input("\nThink hard and enter the minimum number of breaks needed to fix this chain: \n").strip()
                        
                        number_of_breaks = int(user_input)
                        
                        if number_of_breaks == 4:
                            
                            end_time = time.perf_counter()
                                
                            time.sleep(3)
                            print(f"\nAin't you a clever one {self.username.title()}! You're sharper than the prick of a cactus! Only 4 breaks are needed.\n\n")
                            time.sleep(4)
                            print("[The miner swiftly breaks the links, joins the chain, and pulls you through the space.]\n\n")

                            count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                            leaderboard.Leaderboard.update_leaderboard(self.username, "puzzle_four", count_time)
                            
                            leaderboard.Leaderboard.show_Leaderboard()
                            
                            main.save_progress(self.username)
                            
                            options = input('''You did real well there partner!\n\nYa'll wana carry on into this here mine and rescue them miners?
Continue - "c"
Exit - "e"
:''')
                            options = options.lower().strip(" ")
                                
                            if options == "c":
                                
                                main.load_progress(self.username)
                                return True
                            
                            elif options == "e":
                                time.sleep(2)
                                print("\nSorry to see you go partner! Mines aren't for the faint hearted...\n\n\n")
                                break
                            else:
                                time.sleep(2)
                                print("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n")
                                continue
                        
                        elif number_of_breaks != 4:
                            
                            time.sleep(3)
                            print("\nNope, that ain't it. You gotta think like you're spendin' links, not silver dollars. Try again...")

                            time.sleep(3)
                            cont = input("Want to have another go fella?\n\nYes - \"y\"\nNo - \"n\"\n:")
                            
                            cont = cont.lower().strip(" ")
                            
                            if cont == "y":
                                continue
                            elif cont == "n":
                            
                                end_time = time.perf_counter()
                                
                                count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                leaderboard.Leaderboard.update_leaderboard(self.username, "puzzle_three", count_time)
                                
                                break
                            
                        else:
                            time.sleep(2)
                            print("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n")
                            continue
                    except ValueError as e:
                        print(f"There was an error in the value: {e}")
                    except Exception as e:
                        print(f"There was an unknown error: {e}")
            
            elif options == "2":
                
                time.sleep(8)
                print(f"\n\nOh no {self.username.title()}! The tunnel ahead has collapsed, that's the end of this track...\n\n")
                time.sleep(5)
                print("Wait look!\n\n")
                time.sleep(4)
                print("There's just a narrow crawl space left.\n\n")
                time.sleep(3)
                print("[A miner hollers at ya'll from the other side of the crawl space:\n")
                time.sleep(2)
                # Use Avatar class for intro speech
                print(f"{self.avatar.get_intro('miner_crawlspace')}\n\n")
                time.sleep(4)
                
            elif options == "3":
                
                location.get_loc_info("puzzle_three")
                
            elif options == "4":
                
                leaderboard.Leaderboard.status_bar("puzzle_three")
                
            elif options == "e":
                main.save_progress(self.username)
                break
            else:
                print("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n")

#==== Fourth Puzzle - Cross the lake ====#

    def puzzle_four(self):
        
        time.sleep(8)
        print(f"\n\nHowdy {self.username.title()}! You've just gotten to some kinda underground lake.\n\n")
        time.sleep(4)
        print("That smells funny...\n\n\n")
        time.sleep(6)
        print("Is that gas?! Y'all gotta find a way out!!\n\n")
        time.sleep(5)
        print("Looky over there!\n\n")
        time.sleep(3)
        print("There's a rickety old boat, a jittery old miner, some unstable dynamite, and a sneaky rat!\n\n")
        time.sleep(4)
        print("I reckon ya'll gotta get em all across to the other side before the whole place floods!\n\n")        
        time.sleep(4)
        
        # Use Avatar class for intro speech
        print(f"[The jittery miner stumbles up to you:]\n{self.avatar.get_intro('miner_two')}\n\n")
        time.sleep(17)
        
        puzzle_four_item = "mask"
        
        print('''What is the name ya'll gona do??
Your actions are:
A - Take Rat Across
B - Take Dynamite Across
C - Take Miner Across
D - Take Nothing Across
''')
        
        # Pompting for a hint
        time.sleep(5)
        print(f"{self.avatar.get_prompt('miner_two')}\n\n\n")
        while True: 
            choice = input('''How'd you wana respond partner?
Yes - "y"
No - "n"
Check inventory - "c"
''')
            choice = choice.lower().strip(" ")        
            if choice == "y":
                if self.has_required_epuipment(puzzle_four_item):
                    time.sleep(3)
                    print(f"{self.avatar.get_hint('miner_two', self.username)}\n\n")
                    self.update_equipment()
                    break
                else:
                    time.sleep(3)
                    print("Tryna pull a fast one on me eh? Only mask I see's ya blatant lie!\n\n")
                    break
            elif choice == "n":
                time.sleep(3)
                print("No mask eh? Guess you gotta figure it out ya self\n\n")
                break
            elif choice == "c":
                time.sleep(3)
                print(f"Your equipment: {self.get_inventory_item()}\n\n")
                continue
            else:
                print("\nThat aint a choice my friend...Try again.\n\n")
                time.sleep(3)        
        
        while True:
            time.sleep(4)
            options = input('''\nI wonder what that was all about...Maybe there's a puzzle to solve?\n\n
Solve puzzle - 1
Hear again - 2
Look around - 3
See status - 4
Save and Exit - e                           
\n''')
                
            options = options.lower().strip(" ")
    
            if options == "1":
                start_time = time.perf_counter()
    
                # Puzzle Logic
                #valid_choices = ['A', 'B', 'C', 'D']
                solution = "BDABCDB"  # The correct sequence of actions
                
                while True:
                    try:
                        player_input = input("\nChoose yer action in the right order: e.g. ABCABCD\n\n").upper().strip()
                
                        # Validate each character
                        #input_valid = True
                        
                        # Check if the input is in the correct order
                        if player_input == solution:
                            
                            end_time = time.perf_counter()
                            time.sleep(4)
                            print(f"\nYeehaw! Ya did it {self.username.title()}! All safe and sound on t'other side.\n\n")
                            time.sleep(3)
                            
                            # Save progress and move to next puzzle
                            count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                            leaderboard.Leaderboard.update_leaderboard(self.username, "puzzle_five", count_time)
                            
                            leaderboard.Leaderboard.show_Leaderboard()
                            
                            main.save_progress(self.username)
                            
                            options = input('''You did real well there partner!\n\nYa'll wana carry on into this here mine and rescue them miners?
Continue - "c"
Exit - "e"
:''')
                            options = options.lower().strip(" ")
                                
                            if options == "c":
                                
                                main.load_progress(self.username)
                                return True
                            
                            elif options == "e":
                                time.sleep(2)
                                print("\nSorry to see you go partner! Mines aren't for the faint hearted...\n\n\n")
                                break
                            else:
                                time.sleep(2)
                                print("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n")
                                continue
                            break
                        
                        # Check input length
                       # elif len(player_input) != len(solution):
                            #time.sleep(3)
                            #print("That don't sound quite right, we ain't got forever...\n\n")
                            #continue  # Get new input if length is incorrect
                
                        #for char in player input:
                            #if char not in valid_choices:
                               #time.sleep(3)
                                #print("That ain't a valid choice, partner. Pick A, B, C, or D.")
                                #input_valid = False
                                #break                                
                
                        #if input_valid == False:
                            #continue  # Get new input if any character is invalid
                            
                        elif player_input != solution:
                            
                            time.sleep(3)
                            print("That don't sound quite right, we ain't got forever...\n\n")

                            time.sleep(3)
                            cont = input("Want to have another go fella?\n\nYes - \"y\"\nNo - \"n\"\n:")
                            
                            cont = cont.lower().strip(" ")
                            
                            if cont == "y":
                                continue
                            elif cont == "n":
                            
                                end_time = time.perf_counter()
                                
                                count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                                leaderboard.Leaderboard.update_leaderboard(self.username, "puzzle_four", count_time)
                                
                                break
                        else:
                            time.sleep(2)
                            print("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n")
                            continue
                
                    except Exception as e:
                        print(f"There was an unknown error: {e}")
                        
            elif options == "2":
                 
                time.sleep(8)
                print(f"\n\nHowdy {self.username.title()}! You've just gotten to some kinda underground lake.\n\n")
                time.sleep(4)
                print("That smells funny...\n\n\n")
                time.sleep(6)
                print("Is that gas?! Y'all gotta find a way out!!\n\n")
                time.sleep(5)
                print("Looky over there!\n\n")
                time.sleep(3)
                print("There's a rickety old boat, a jittery old miner, some unstable dynamite, and a sneaky rat!\n\n")
                time.sleep(4)
                print("I reckon ya'll gotta get em all across to the other side before the whole place floods!\n\n")        
                time.sleep(4)
                
                # Use Avatar class for intro speech
                print(f"[The jittery miner stumbles up to you:]\n{self.avatar.get_intro('miner_two')}\n\n")
                time.sleep(5)
                
                puzzle_four_item = "mask"
                
                print('''What is the name ya'll gona do??
        Your actions are:
        A - Take Rat Across
        B - Take Dynamite Across
        C - Take Miner Across
        D - Take Nothing Across
        ''')
                 
            elif options == "3":
                 
                 location.get_loc_info("puzzle_four")
                 
            elif options == "4":
                 
                 leaderboard.Leaderboard.status_bar("puzzle_four")
                 
            elif options == "e":
                 main.save_progress(self.username)
                 break
            else:
                 print("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n")

#==== Fifth Puzzle - Lift shaft ====#

    def puzzle_five(self):
        
        time.sleep(8)
        print(f"\nHowdy {self.username.title()}! You must be close to the lift shaft now. That must be where the miners are trapped!\n\n\n")
        time.sleep(4)
        print("It's a real squeeze down here! I wonder if we're ever going to find these fellas?\n\n")
        time.sleep(4)
        print("Drip\n")
        time.sleep(2)
        print("Drip\n")
        time.sleep(2)
        print("Drip\n")
        time.sleep(3)
        print("Whoa! Wait partner, youn hear that?\n\n")
        time.sleep(4)
        print("[Faintly, off down the tunnel] Help! Is there someone there?\n\n")
        time.sleep(4)
        print("You reckon that's them?\n")
        time.sleep(3)
        print("Let's shout back!\n")  
        time.sleep(2)
        print("Hellllooooo!\n\n")
        time.sleep(3)
        print("Anyone down there?\n\n")
        time.sleep(5)
        print("[SILENCE]\n\n")
        time.sleep(3)
        print("[Louder] Anyone doooowwwwn theeerrreeee?\n\n\n")
        time.sleep(4)
        print("Heeelllp! Weee'reee traappped!\n\n")
        time.sleep(4)
        print("That must be them!\nLet's go find out!\n\n\n\n")
        time.sleep(6)
        # Use Avatar class for intro speech
        print("[Some minutes later...]\n\n")
        time.sleep(4)
        print("Look, it's a lift shaft\n\n\nYou fellas alright down there?\n\n") 
        time.sleep(4)
        
        #Avatar class for intro
        print(f"Boy are we glad to see you!\n\n{self.avatar.get_intro('trapped_miner')}\n")
        time.sleep(30)
        
        puzzle_five_item = "notebook" 
        
        print(f"{self.avatar.get_prompt('trapped_miner')}\n\n")
        
        while True: 
            choice = input('''How'd you wana respond partner?
Yes - "y"
No - "n"
Check inventory - "c"
''')
            choice = choice.lower().strip(" ")
            
            if choice == "y":
                if self.has_required_epuipment(puzzle_five_item):
                    time.sleep(3)
                    print(f"{self.avatar.get_hint('trapped_miner', self.username)}\n\n")
                    self.update_equipment()
                    break
                else:
                    time.sleep(3)
                    print("Tryna pull a fast one on me eh? Only mask I see's ya blatant lie!\n\n")
                    break
            elif choice == "n":
                time.sleep(3)
                print("Ah dang! Ya'll don't got a notebook? Guess you gotta figure it out ya self...\n\n")
                break
            elif choice == "c":
                time.sleep(3)
                print(f"Your equipment: {self.get_inventory_item()}\n\n")
                continue
            else:
                print("\nThat aint a choice my friend...Try again.\n\n")
                time.sleep(3)        
        
        #Puzzle logic
        
        while True:
            
            options = input('''\nSeems like a tricky puzzle partner... What do ya'll wana do?
Solve puzzle - 1
Hear again - 2
Look around - 3
See status - 4
Save and Exit - e                           
\n''')
            
            options = options.lower().strip(" ")
    
            if options == "1":
                start_time = time.perf_counter()
                answer = input("\nSo what's your answer partner?\nEnter it here:")
                
                if answer == "98-7-6+5+4+3+2+1":
                    end_time = time.perf_counter()
                    
                    count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                    leaderboard.Leaderboard.update_leaderboard(self.username, "finished", count_time)
                    
                    main.save_progress(self.username)
                                    
                    print(f"YOU DID IT {self.username.title()}!\n\n\n")
                    time.sleep(4)                       
                    print(f"{self.avatar.get_outro('trapped_miner')}\n\n\n")
                    
                    leaderboard.Leaderboard.status_bar("finished")
                    
                    leaderboard.Leaderboard.show_Leaderboard()
                    
                    break
                elif answer != "98-7-6+5+4+3+2+1":
                    
                    time.sleep(3)
                    print("That don't sound quite right, we ain't got forever...\n\n")

                    time.sleep(3)
                    cont = input("Want to have another go fella?\n\nYes - \"y\"\nNo - \"n\"\n:")
                    
                    cont = cont.lower().strip(" ")
                    
                    if cont == "y":
                        continue
                    elif cont == "n":
                    
                        end_time = time.perf_counter()
                        
                        count_time = leaderboard.Leaderboard.count_time(start_time, end_time)
                        leaderboard.Leaderboard.update_leaderboard(self.username, "puzzle_five", count_time)
                        
                        break

            elif options == "2":
                
                time.sleep(8)
                print(f"\nHowdy {self.username.title()}! You must be close to the lift shaft now. That must be where the miners are trapped!\n\n\n")
                time.sleep(4)
                print("It's a real squeeze down here! I wonder if we're ever going to find these fellas?\n\n")
                time.sleep(4)
                print("Drip\n")
                time.sleep(2)
                print("Drip\n")
                time.sleep(2)
                print("Drip\n")
                time.sleep(3)
                print("Whoa! Wait partner, youn hear that?\n\n")
                time.sleep(4)
                print("[Faintly, off down the tunnel] Help! Is there someone there?\n\n")
                time.sleep(4)
                print("You reckon that's them?\n")
                time.sleep(3)
                print("Let's shout back!\n")  
                time.sleep(2)
                print("Hellllooooo!\n\n")
                time.sleep(3)
                print("Anyone down there?\n\n")
                time.sleep(5)
                print("[SILENCE]\n\n")
                time.sleep(3)
                print("[Louder] Anyone doooowwwwn theeerrreeee?\n\n\n")
                time.sleep(4)
                print("Heeelllp! Weee'reee traappped!\n\n")
                time.sleep(4)
                print("That must be them!\nLet's go find out!\n\n\n\n")
                time.sleep(6)
                # Use Avatar class for intro speech
                print("[Some minutes later...]\n\n")
                time.sleep(4)
                print("Look, it's a lift shaft\n\n\nYou fellas alright down there?\n\n") 
                time.sleep(4)
                
                #Avatar class for intro
                print(f"Boy are we glad to see you!\n\n{self.avatar.get_intro('trapped_miner')}\n")
                time.sleep(5)

            elif options == "3":
                
                location.get_loc_info("puzzle_five")
                
            elif options == "4":
                
                leaderboard.Leaderboard.status_bar("puzzle_five")
                
            elif options == "e":
                main.save_progress(self.username)
                break
            else:
                print("\nWhoa there, partner! That ain't somethin' you can pick.\n Have another go...\n\n")
                
# -*- coding: utf-8 -*-
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

    def puzzle_four(self):
        
        
        
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
username = "s"
Puzzle(username).puzzle_four()        

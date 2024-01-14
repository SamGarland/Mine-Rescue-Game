'''
 ===== Main file for MUD Game CW 2 APP PROG sem 1 =====

This is the main file for Mine Rescue.
It contains functions for registering, logging-in, saving progress and loading
progress.
It also contains the start menu.
 
'''

#==== Imports ====#

import time
import sys
sys.path.append('./modules')
import character
import leaderboard
import puzzle
import text

#===== Functions =====#

# This function allows the player to register by entering a username and password into "user.txt".

def register_user():
        
    with open("../resources/users.txt", "r+") as f:#r+
         
         new_username = ""
         usernames = []
         user_exists = True
         
         for line in f:
             line = line.split(", ")
             if line:
                 usernames.append(line[0])
         
         while user_exists:
              new_username = input('''\nGive me your name of choice friend\nor Back to start menu - e\n:''')
              new_username = new_username.strip(" ")
              
              if new_username == "e":
                  return False
              elif new_username in usernames:
                 text.Typed.typed_text("\nWell dang! That name is taken...Have another go.\n")
              else:
                  user_exists = False
                  continue
              
         while True:
              new_password = input("\nWhat password y'all gona use? Shhhh, keep this a secret!\n")
              confirm_password = input("\nTell me one more time:\n")
              if new_password != confirm_password:
                  text.Colour("\nSorry, no matcheroo...\n").red()
              else:
                  text.Typed.typed_text("\nWelcome partner! That's all been taken care of for you!\n")
                  f.write(f"{new_username}, {new_password}\n")
                  break
    f.close()
    
    text.Typed.typed_text("\nNow have a go at logging-in and we'll make sure everything is hunky-dorey!\n")
    login()

# This function allows the player to login by taking a username and password stored in "users.txt"  
# and compares them with a username and password entered by the player.

def login():
    
    f = open("../resources/users.txt", "r")
    
    authenticated = False
    
    lines = f.readlines()
    
    while authenticated == False:
        
        username = input("\nHowdy! Enter your username partner:\n")
        username = username.strip(" ")
        password = input("\nHowdy! Enter your password partner:\n")
        password = password.strip(" ")
        
        
        for line in lines:
            
            line = line.strip("\n").split(", ")
            
            if username == line[0] and password == line[1]:
                authenticated = True
            else:
                continue
    
        if authenticated == True:
            text.Typed.typed_text("\nThat's right my friend!\n\nWelcome to the game!")
            load_progress(username)
        else:
            options = input('''\n\nSeems you either entered it wrong or you aint registered! What do ya'll wana do?
Have another go - 1
Register - 2
Back to start menu - e
:''')
            options = options.lower().strip(" ")
            
            if options == "1":    
                text.Typed.typed_text("\nAlright partner! Have another go...\n\n")
                time.sleep(2)
            elif options == "2":
                register_user()
            elif options == "e":
                return False
            else:
                time.sleep(2)
                text.Typed.typed_text("\nDo'ya know what? I don't understand a thang you just said... Have another go!\n")
                
    f.close()

# This functions loads game progress by looking at the puzzle number for a player in "characters.txt". 

def load_progress(username):
    with open("../resources/characters.txt", "r") as char_file:
        lines = char_file.readlines()

    character_found = False

    for line in lines:
        items = line.strip().split(',')
        if items[0] == username:
            character_found = True
            current_puzzle = items[-1]
            gender = items[2]
            hair_colour = items[3]
            hat = items[4]
            boots = items[5]
            
            # Redirect to respective puzzle based on current_puzzle value.
            if current_puzzle == "puzzle_one":
                puzzle.Puzzle(username, gender, hair_colour, hat, boots).puzzle_one()
            elif current_puzzle == "puzzle_two":
                puzzle.Puzzle(username, gender, hair_colour, hat, boots).puzzle_two()
            elif current_puzzle == "puzzle_three":
                puzzle.Puzzle(username, gender, hair_colour, hat, boots).puzzle_three()
            elif current_puzzle == "puzzle_four":
                puzzle.Puzzle(username, gender, hair_colour, hat, boots).puzzle_four()
            elif current_puzzle == "puzzle_five":
                puzzle.Puzzle(username, gender, hair_colour, hat, boots).puzzle_five()
            elif current_puzzle == "finished":
                text.Typed.typed_text("\n\nSeems you already completed this fella!\nLet's see how you did\n\n")
                leaderboard.Leaderboard.show_Leaderboard()
                # Restart game menu
                while True:
                    options = input("\nYa'll wana restart the game and have another go? Ya'll can keep your username and password but all your progress will be lost.\nYes - y\nNo - n\n:")
                    if options == "y":
                        text.Typed.typed_text("\nYipeee! We's bout to go on another adventure ya'll!\n\n")
                        restart_game(username)
                        return False
                    elif options == "n":
                        break
                    else:
                        text.Colour("That ain't no choice ya'll can make partner!").red()
    if not character_found:
        text.Typed.typed_text("\nTime to saddle up and create yer character!")
        character.Character.create_character(username)
    
    char_file.close()

# This function saves the player game progress.

def save_progress(username, puzzle):
    with open("../resources/characters.txt", "r") as char_file:
        lines = char_file.readlines()

    character_found = False
    new_lines = []

    for line in lines:
        items = line.strip().split(',')
        if items[0] == username:
            character_found = True
            items[-1] = puzzle
                
            new_line = ','.join(items)
        else:
            new_line = line.strip()

        new_lines.append(new_line)

    if character_found:
        
        with open("../resources/characters.txt", "w") as file:
            for line in new_lines:
                file.write(line + '\n')
    else:
        text.Colour(f"User '{username}' not found in file. Unable to load progress.").red()

    char_file.close()
    
# This function allows a player who has completed the game to create a new character and start again.
# It wipes their previous character and leaderboard entries.

def restart_game(username):
    
    try:
        try:
            # Stripping leaderboard info for user.
            with open("../resources/leaderboard.txt", "r") as lb:
                lines = lb.readlines()
            
                new_lines = []
                lb_deleted = False
                
                for line in lines:
                    items = line.strip().split(',')
                    if items[0] == username:
                        line.strip()
                        lb_deleted = True
                    else:
                        new_line = line.strip()
                        new_lines.append(new_line)
            
                if lb_deleted:
                    
                    with open("../resources/leaderboard.txt", "w") as lb:
                        for line in new_lines:
                            lb.write(line + '\n')
                text.Typed.typed_text(f"\nHowdy, {username}. Ya'll no longer in the leaderboard!\n\n")
            lb.close()
        except:
            text.Colour("\nSorry friend, we can't find ya'll in the leaderboard.\n\n").red()
        
        try:
            # Stripping character info for user.
            with open("../resources/characters.txt", "r") as char:
                lines = char.readlines()
            
                new_lines = []
                char_deleted = False
                
                for line in lines:
                    items = line.strip().split(',')
                    if items[0] == username:
                        line.strip()
                        char_deleted = True
                    else:
                        new_line = line.strip()
                        new_lines.append(new_line)
            
                if char_deleted:
                    
                    with open("../resources/characters.txt", "w") as char:
                        for line in new_lines:
                            char.write(line + '\n')
                text.Typed.typed_text(f"\nHowdy, {username}. Ya'll gona be starting the game again any second!\n\n")
            char.close()
        except:
            text.Colour("\nSorry friend, we can't find ya'll character.\n\n").red()
        # Loading progress, which will go to create_character().
        load_progress(username)
        
    except:
        text.Colour("\nSorry friend, something went wrong with tryin'a restart the game for ya'll!\n\n").red()
    

#==== Start Menu ====#

# This menu allows users to either register, login or exit the game. 
    
if __name__ == "__main__":
    
    # Intro to Mine Rescue.
    text.Typed.intro_image()

    while True:
        
        user_selection = input('''\nNow what are you wanting to do partner?
Register - r
Login - l
Exit game - e
:''')
    
        user_selection = user_selection.lower().strip(" ")
        
        if user_selection == "r":
            
           register_user()
        
        elif user_selection == "l": 
            
            login()
            
        elif user_selection == "e":
            text.Typed.typed_text("\nSorry to see you go partner! Mines aren't for the faint hearted...\n\n\n")
            break
            
        else:
            text.Colour("\nDo'ya know what? I don't understand a thang you just said... Have another go!\n").red()
            continue
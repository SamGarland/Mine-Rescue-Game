'''
 ===== This programme is for MUD Game CW 2 APP PROG sem 1 =====
    
'''
import time
import character
import leaderboard
import puzzle
import text

#===== FUNCTIONS =====#

def register_user():
    
    # This function allows the user to register by entering a username and password into
    # "user.txt".
    
    with open("users.txt", "r+") as f:
         
         new_username = ""
         usernames = []
         user_exists = True
         
         for line in f:
             line = line.split(", ")
             if line:
                 usernames.append(line[0])
         
         while user_exists:
              new_username = input(text.Colour('''\nGive me your name of choice friend\nor Exit - "e"\n:''').input_cyan())
              new_username = new_username.lower().strip(" ")
              
              if new_username == "e":
                  text.Colour("\nSorry to see you go partner! Mines aren't for the faint hearted...\n\n\n").cyan()
                  return False
              elif new_username in usernames:
                 text.Colour("\nWell dang! That name is taken...Have another go.\n").cyan()
              else:
                  user_exists = False
                  continue
              
         while True:
              new_password = input(text.Colour("\nWhat password y'all gona use? Shhhh, keep this a secret!\n").input_cyan())
              confirm_password = input(text.Colour("\nTell me one more time:\n").input_cyan())
              if new_password != confirm_password:
                  text.Colour("\nSorry, no matcheroo...\n").red()
                  continue
              else:
                  text.Colour("\nWelcome partner! That's all been taken care of for you!\n").cyan()
                  f.write(f"{new_username}, {new_password}\n")
                  break
    f.close()
    
    text.Colour("\nNow have a go at logging-in and we'll make sure everything is hunky-dorey!\n").cyan()
    login()


def login():
    
    # This function allows the user to login by taking a username and password stored in "users.txt"  
    # and compares them with a username and password entered by the user.
    
    f = open("users.txt", "r")
    
    authenticated = False
    
    lines = f.readlines()
    
    while authenticated == False:
        
        username = input(text.Colour("\nHowdy! Enter your username partner:\n").input_cyan())
        username = username.lower().strip(" ")
        password = input(text.Colour("\nHowdy! Enter your password partner:\n").input_cyan())
        password = password.lower().strip(" ")
        
        
        for line in lines:
            
            line = line.strip("\n").split(", ")
            
            if username == line[0] and password == line[1]:
                authenticated = True
            else:
                continue
    
        if authenticated == True:
            text.Colour("\nThat's right my friend!\n\nWelcome to the game!").cyan()
            load_progress(username)
        else:
            options = input(text.Colour('''\n\nSeems you either entered it wrong or you aint registered! What do ya'll wana do?
Have another go - 1
Register - 2
Exit - e
:''').input_cyan())
            options = options.lower().strip(" ")
            
            if options == "1":    
                text.Colour("\nAlright partner! Have another go...\n\n").cyan()
                time.sleep(2)
                continue
            elif options == "2":
                register_user()
            elif options == "e":
                return False
            else:
                time.sleep(2)
                text.Colour("\nDo'ya know what? I don't understand a thang you just said... Have another go!\n").cyan()
                continue
                
    f.close()
    
def load_progress(username):
    with open('characters.txt', 'r') as char_file:
        lines = char_file.readlines()

    character_found = False

    for line in lines:
        items = line.strip().split(',')
        if items[0] == username:
            character_found = True
            current_puzzle = items[-1]
            
            # Redirect to respective puzzle based on current_puzzle value
            if current_puzzle == "puzzle_one":
                puzzle.Puzzle(username).puzzle_one()
            elif current_puzzle == "puzzle_two":
                puzzle.Puzzle(username).puzzle_two()
            elif current_puzzle == "puzzle_three":
                puzzle.Puzzle(username).puzzle_three()
            elif current_puzzle == "puzzle_four":
                puzzle.Puzzle(username).puzzle_four()
            elif current_puzzle == "puzzle_five":
                puzzle.Puzzle(username).puzzle_five()
            elif current_puzzle == "finished":
                text.Colour("\n\nSeems you already completed this fella!\nLet's see how you did\n\n").cyan()
                leaderboard.Leaderboard.show_Leaderboard()
            break

    if not character_found:
        text.Colour("\nWell well, we ain't got no record of ya partner. Time to saddle up and create yer character!").cyan()
        character.Character.create_character(username)
    
    char_file.close()

def save_progress(username):
    with open('characters.txt', 'r') as char_file:
        lines = char_file.readlines()

    character_found = False
    new_lines = [] #Create empty list to hold new lines

    for line in lines:
        items = line.strip().split(',')
        if items[0] == username: #Check for username
            character_found = True
            current_puzzle = items[-1] #Store current puzzle
            
            # Update to the next puzzle based on the current puzzle
            if current_puzzle == "puzzle_one":
                items[-1] = "puzzle_two"
            elif current_puzzle == "puzzle_two":
                items[-1] = "puzzle_three"
            elif current_puzzle == "puzzle_three":
                items[-1] = "puzzle_four"
            elif current_puzzle == "puzzle_four":
                items[-1] = "puzzle_five"
            elif current_puzzle == "puzzle_five":
                items[-1] = "finished"
                #Take player to leaderboard
            else:
                text.Colour("puzzle name not found...").red()
                
            new_line = ','.join(items)
        else:
            new_line = line.strip() #keep lines same if user not found

        new_lines.append(new_line) #append empty list with updated line

    if character_found:
        # Write the updated lines back to the file
        with open('characters.txt', 'w') as file:
            for line in new_lines:
                file.write(line + '\n')
    else:
        # Print a message if the user was not found in the file
        text.Colour(f"User '{username}' not found in file. Unable to load progress.").red()

    char_file.close()
    

#==== Main execution file =====

if __name__ == "__main__":

#===== Start Menu =====#

# This menu allows users to either register, login or exit the game. 
    
    while True:
        
        user_selection = input(text.Colour('''\nNow what are you wanting to do partner?
Register - "r"
Login - "l"
Exit game - "e"
:''').input_cyan())
    
        user_selection = user_selection.lower().strip(" ")
        
        if user_selection == "r":
            
           register_user()
        
        elif user_selection == "l": 
            
            login()
            
        elif user_selection == "e":
            text.Colour("\nSorry to see you go partner! Mines aren't for the faint hearted...\n\n\n").cyan()
            break
            
        else:
            text.Colour("\nDo'ya know what? I don't understand a thang you just said... Have another go!\n").red()
            continue
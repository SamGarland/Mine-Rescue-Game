'''
 ===== Main file for MUD Game CW 2 APP PROG sem 1 =====
    
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
              new_username = input('''\nGive me your name of choice friend\nor Exit - "e"\n:''')
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
                  continue
              else:
                  text.Typed.typed_text("\nWelcome partner! That's all been taken care of for you!\n")
                  f.write(f"{new_username}, {new_password}\n")
                  break
    f.close()
    
    text.Typed.typed_text("\nNow have a go at logging-in and we'll make sure everything is hunky-dorey!\n")
    login()


def login():
    
    # This function allows the user to login by taking a username and password stored in "users.txt"  
    # and compares them with a username and password entered by the user.
    
    f = open("users.txt", "r")
    
    authenticated = False
    
    lines = f.readlines()
    
    while authenticated == False:
        
        username = input("\nHowdy! Enter your username partner:\n")
        username = username.lower().strip(" ")
        password = input("\nHowdy! Enter your password partner:\n")
        password = password.lower().strip(" ")
        
        
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
Exit - e
:''')
            options = options.lower().strip(" ")
            
            if options == "1":    
                text.Typed.typed_text("\nAlright partner! Have another go...\n\n")
                time.sleep(2)
                continue
            elif options == "2":
                register_user()
            elif options == "e":
                return False
            else:
                time.sleep(2)
                text.Typed.typed_text("\nDo'ya know what? I don't understand a thang you just said... Have another go!\n")
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
                text.Typed.typed_text("\n\nSeems you already completed this fella!\nLet's see how you did\n\n")
                leaderboard.Leaderboard.show_Leaderboard()
            break

    if not character_found:
        text.Typed.typed_text("\nTime to saddle up and create yer character!")
        character.Character.create_character(username)
    
    char_file.close()

def save_progress(username, puzzle):
    with open('characters.txt', 'r') as char_file:
        lines = char_file.readlines()

    character_found = False
    new_lines = [] #Create empty list to hold new lines

    for line in lines:
        items = line.strip().split(',')
        if items[0] == username: #Check for username
            character_found = True
            items[-1] = puzzle #Store current puzzle
                
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
    
    text.Typed.intro_image()

    while True:
        
        user_selection = input('''\nNow what are you wanting to do partner?
Register - "r"
Login - "l"
Exit game - "e"
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
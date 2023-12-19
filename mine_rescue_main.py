'''
 ===== This programme is for MUD Game CW 2 APP PROG sem 1 =====

FILES REQUIRED :
    - "users.txt" - this takes and saves username and password as: username, password per line.
    - "characters.txt" - this takes username, character info and equipment.
    - "leaderboard.txt" - this takes username and puzzle timestamps (positions and timestamp aggregations can be worked out later)

FUNCTIONS:
    
    -register_user(username, password)
    -login(username, password)
    -load_progress(username)
    -create_character(username)
    -save_progress(username)
    -show_leaderboard()
    -puzzle_one()
    -puzzle_two()
    -puzzle_three()
    -puzzle_four()
    -puzzle_five()
    
'''

import Character
import Location
import Leaderboard
import Puzzle
import Avatar

#===== FUNCTIONS =====#

class main():
    pass
    #Add the main file functions to this class.

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
              new_username = input("\nGive me your name of choice friend:\n")
              if new_username in usernames:
                 print("\nWell dang! That name is taken...Have another go.\n")
              else:
                  user_exists = False
                  continue
              
         while True:
              new_password = input("\nWhat password y'all gona use? Shhhh, keep this a secret!\n")
              confirm_password = input("\nTell me one more time:\n")
              if new_password != confirm_password:
                  print("\nSorry, no matcheroo...\n")
                  continue
              else:
                  print("\nWelcome partner! That's all been taken care of for you!\n")
                  f.write(f"{new_username}, {new_password}\n")
                  break
    f.close()
    
    print("\nNow have a go at logging-in and we'll make sure everything is hunky-dorey!\n")
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
            print("\nThat's right my friend!\n\nWelcome to the game!")
        else:
            print("\nSorry partner! Have another go...")
                
    f.close()
    load_progress(username)
    
def load_progress(username):
    with open('characters.txt', 'r') as char_file:
        lines = char_file.readlines()

    character_found = False

    for line in lines:
        items = line.strip().split(',')
        if items[0] == username:
            character_found = True
            current_puzzle = items[-1]
            print(f"\nHowdy {username.title()}! Time to carry on to {current_puzzle}, the miners ain't wait'n forever")

            # Redirect to respective puzzle based on current_puzzle value
            if current_puzzle == "puzzle_one":
                puzzle_one(username)
            elif current_puzzle == "puzzle_two":
                puzzle_two()
           # elif current_puzzle == "puzzle_three":
           #     puzzle_three()
           # elif current_puzzle == "puzzle_four":
           #     puzzle_four()
           # elif current_puzzle == "puzzle_five":
           #     puzzle_five()
            #elif current_puzzle == "puzzles_completed":
           #     print("Seems you already completed this fella!Let's see how you did\n")
           #     take to leaderboard
            break

    if not character_found:
        print("\nWell well, we ain't got no record of ya partner. Time to saddle up and create yer character!")
<<<<<<< Updated upstream
        create_character(username)
    
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
                items[-1] = "puzzles_completed"
                #Take player to leaderboard
            else:
                print("puzzle name not found, file error")
                
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
        print(f"User '{username}' not found in file. Unable to load progress.")

    char_file.close()
    

def puzzle_one(username):
    print("\nAlright, here's your first challenge:")
    answer = input("What is the capital of England? ").lower().strip()
    
    # Check if the answer is correct
    if answer == "london":
        print("Correct! London is the capital of England. You're moving on to the next challenge!")
        save_progress(username)
        load_progress(username)
    else:
        print("Oops! That's not quite right. Try again!")
        return False

def puzzle_two():
    print("\nHere comes your second challenge:")
    answer = input("What is the capital of Japan? ").lower().strip()
    
    # Check if the answer is correct
    if answer == "tokyo":
        print("Correct! Tokyo is indeed the capital of Japan. You're doing great!")
        return True
    else:
        print("That's not the right answer. Give it another shot!")
        return False


#==== Main execution file =====

if __name__ == "__main__":

#===== Start Menu =====#

# This menu allows users to either register, login or exit the game. 
    
    while True:
        
        user_selection = input('''\nNow what are you wanting to do partner?
    Register - "r"
    Login - "l"\n''')
    
        user_selection = user_selection.lower().strip(" ")
        
        if user_selection == "r":
            
           register_user()
           break
        
        elif user_selection == "l": 
            
            login()
            break
            
        else:
            print("\nDo'ya know what? I don't understand a thang you just said... Have another go!\n")
            continue


#===== Gameplay Conditional =====#



'''- This function takes username and checks "character.txt" to find puzzle_no.

if username not in "character.txt"
    create_character(username)
    this uses the character class to create a new character and saves it to 
    "character.txt" with default puzzle_one
elif username in "character.txt":
    load_character(username)
    this loads character stats from "character.txt" in a readable way
    and takes user to saved puzzle. 
    it also loads timestamp progress. '''
 
'''
while True:
    
    if user_character[puzzle] == "puzzle_one":
    
        pass
        puzzle_one() 
        at the end of puzzle_one: 
            - save progress to character.txt as puzzle_two and 
            take away any equipment used
            - update "leaderboard.txt"
            - load_progress()
            
    elif user_character[puzzle] == "puzzle_two":
        
       puzzle_two() 
        at the end of puzzle_two: 
            - save progress to character.txt as puzzle_three and 
            take away any equipment used
            - update "leaderboard.txt"
            - load_progress()
    
    elif user_character[puzzle] == "puzzle_three":
    
       puzzle_three() 
        at the end of puzzle_three: 
            - save progress to character.txt as puzzle_four and 
            take away any equipment used
            - update "leaderboard.txt"
            - load_progress()
        
    elif user_character[puzzle] == "puzzle_four":
    
        puzzle_four() 
        at the end of puzzle_four: 
            - save progress to character.txt as puzzle_five and 
            take away any equipment used
            - update "leaderboard.txt"
            - load_progress()
    
    elif user_character[puzzle] == "puzzle_five":
    
       puzzle_five() 
        at the end of puzzle_five: 
            - save progress to character.txt as puzzles_finished and 
            take away any equipment used
            - update "leaderboard.txt"
            - load_leaderboard()
            break and print leaving statement
    
    elif user_character[puzzle] == "puzzles_finished":
        print("You've already finished the game partner. Want to try again?")
    
    else:
        print("My sincerest condolences partner, we are having trouble loading your progress. Let's try again.")
        load_progress(username)

'''

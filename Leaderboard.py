
"""
This is the Leaderboard class

"""

import time
import os

class Leaderboard():
    #This class need to have a function that displays a status bar.
    #It also needs to be able to agregate timestamps to add to the leaderboard and display the leaderboard. 
    pass

    def __init__(self, username, status, puzzle_time, agg_time):
        
        self._username = username
        self._status = status
        self._puzzle_time = puzzle_time
        self._agg_time = agg_time
    
    def __str__(self):
        return (f"{self._username},{self._status},{self._puzzle_time},{self._agg_time}")


    def update_leaderboard(username, puzzle, count_time):
        # This isn't working as expected: the issue is that it can't find lines that are not new to the file, but don't have the username being looked for to tranfer
        #them to the new file...
        usernames = []
        line_set = []
        
        with open("leaderboard.txt", "r+") as lb, open("new_leaderboard.txt", "a+") as new_lb:
            
            lines = lb.readlines()
            
            for line in lines:
                                
                line = line.strip("\n").split(",")
                
                usernames.append(line[0])
                line_set.append(line)
                print(usernames)
                print(line_set)
                
                if line[0] == username:
                    
                    agg_time = float(line[3]) + float(count_time)
                    
                    update = Leaderboard(username, puzzle, count_time, agg_time)
                    
                    new_lb.write(f"{str(update)}\n")
                    
                else:
                    continue
        
            for line in line_set:
                
                if line[0] != username:
                
                    new_lb.write(f"{line[0]},{line[1]},{line[2]},{line[3]}\n")
                
                else:
                    continue
            
        os.remove("Leaderboard.txt")
        os.rename("new_leaderboard.txt", "Leaderboard.txt")
        
        
        with open("leaderboard.txt", "r+") as lb:
            
            new_entry = Leaderboard(username, puzzle, count_time, count_time)
            
            try:    
                if len(usernames) == 0:
                    
                    lb.write(f"{str(new_entry)}\n")
                
                else:
                    try:
                        if username not in usernames: 
                            lb.write(f"{str(new_entry)}\n")
                    except:
                        print("We got an issue updating the leaderboard!")
            except:
                pass
        
        lb.close()
        
    def show_Leaderboard():

        # This function takes each line from the file and displays a leaderboard.
        
        def underline(text):
            print("\u0332".join(text))
        
        with open("Leaderboard.txt", "r") as lb:
            
            lines = lb.readlines()
            
            file_set = []
            agg_times_set = []
            
            for line in lines:
                line = line.strip("\n").split(",")
                file_set.append(line)
                agg_times_set.append(line[3])
            
            agg_times_set.sort()
            
            text = f"\n\nPosition    Username   Status    Current_Puzzle_Time  Total_Puzzle_Time\n"
            underline(text)
            
            count = 1
            for item in file_set:
                for ele in agg_times_set:
                    if item[3] == ele:
                        print(f" #{count}          {item[0]}    {item[1]}  {item[2]}  {item[3]}\n")
                        count += 1
        lb.close()
            
    def count_time(start_time, end_time):
        
        puzzle_time = end_time - start_time
        
        return puzzle_time



Leaderboard.update_leaderboard("John", "puzzle_two", time.time())

#Leaderboard.show_Leaderboard()
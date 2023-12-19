
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
        
        usernames = []
        
        with open("leaderboard.txt", "r+") as lb, open("new_leaderboard.txt", "a+") as new_lb:
            
            lines = lb.readlines()
            
            for line in lines:
                                
                line = line.strip("\n").split(",")
                str_line = f"{line[0]},{line[1]},{line[2]},{line[3]}"
                
                usernames.append(line[0])
                
                if line[0] != username:
                    
                    new_lb.write(str_line)
                
                elif line[0] == username:
                    
                    l_3 = int(line[3])
                    c_t = int(count_time)
                    
                    agg_time = l_3 + c_t
                    
                    update = Leaderboard(username, puzzle, count_time, agg_time)
                    
                    new_lb.write(str(update))
                    
                else:
                    continue
        lb.close()
        os.remove("Leaderboard.txt")
        os.rename("new_leaderboard.txt", "Leaderboard.txt")
        
        
        with open("leaderboard.txt", "r+") as lb:
            
            new_entry = Leaderboard(username, puzzle, count_time, count_time)
            
            try:    
                if len(usernames) == 0:
                    
                    lb.write(str(new_entry))
                
                else:
                    try:
                        if username not in usernames: 
                            lb.write(str(new_entry))
                    except:
                        print("We got an issue updating the leaderboard!")
            except:
                pass
        
        lb.close
        
            
'''
    
show_leaderboard():
    this prints current leaderboard to console in a table
    
count_time(start_time, end_time):
    this takes the start_time from the end_time to give the time it took to complete a puzzle.

'''

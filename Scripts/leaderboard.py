'''
This is the leaderboard module with Leaderboard class and methods.
These are used to count the puzzle time, update the leaderboard,
show the leaderboard and show status.
 
'''
#==== Imports ====#

import datetime
import math
import os
import text

#==== Class and methods ====#

class Leaderboard:
    
    # Constructor.
    def __init__(self, username, puzzle, count_time):
        
        self.username = username
        self.puzzle = puzzle
        self.count_time = count_time
    
    # Self string.
    def __str__(self,  agg_time):
        return (f"{self.username},{self.puzzle},{self.count_time},{agg_time}\n")
    
    # Method to calculate puzzle time.
    
    def count_time(start_time, end_time):
        
        start_time = math.trunc(start_time)
        end_time = math.trunc(end_time)
        
        count_time = (end_time) - (start_time)
        
        return count_time
    
    # Method to update leaderboard.
    
    def update_leaderboard(self):
        
        usernames = []
        
        try:
            # Look for username already in "leaderboard.txt" and update entry.
            with open("../Resources/leaderboard.txt", "r") as lb, open("../Resources/new_leaderboard.txt", "a+") as new_lb:
                
                lines = lb.readlines()
                
                for line in lines:
                                    
                    line = line.strip("\n").split(",")
                    
                    usernames.append(line[0])
                    if line[0] == self.username:
                        a_t = float(line[3])
                        c_t = float(self.count_time)
                        agg_time = math.floor(a_t) + math.floor(c_t)
                        update = Leaderboard(self.username, self.puzzle, self.count_time)
                        new_lb.write(str(f"{Leaderboard.__str__(update, agg_time)}"))
                        
                    elif line != self.username:
                        user = line[0]
                        status = line[1]
                        puzzle_time = line[2]
                        time = line[3]
                        new_lb.write(f"{user},{status},{puzzle_time},{time}\n")
                        
            os.remove("../Resources/leaderboard.txt")
            os.rename("../Resources/new_leaderboard.txt", "../Resources/leaderboard.txt")
        
            lb.close()
        
        except:
            text.Colour("Failure to update the leaderboard!").red()
        
        with open("../Resources/leaderboard.txt", "r+") as lb:
             # Add new leaderboard entry.
             lines = lb.readlines()
             
             for line in lines:
                                 
                 line = line.strip("\n").split(",")
                 
                 usernames.append(line[0])
                 
             agg_time = self.count_time
             new_entry = Leaderboard(self.username, self.puzzle, self.count_time)
             
             try:    
                 if len(usernames) == 0:       
                     lb.write(str(f"{Leaderboard.__str__(new_entry, agg_time)}"))
                 else:
                     try:
                         if self.username not in usernames:
                             lb.write(str(f"{Leaderboard.__str__(new_entry, agg_time)}"))
                     except:
                         text.Colour("We got an issue updating the leaderboard!").red()
             except:
                 text.Colour("Failure to update the leaderboard!").red()
        
        lb.close()
        
    # Method that takes each line from the "leaderboard.txt" and displays a leaderboard.
   
    def show_Leaderboard():
        
        def underline(text):
            print("\u0332".join(text))
        
        file_set = []
        agg_times_set = []
        
        with open("../Resources/leaderboard.txt", "r") as lb:
            
            lines = lb.readlines()
            
            for line in lines:
                line = line.strip("\n").split(",")
                file_set.append(line)
                a_t = float(line[3])
                agg_times_set.append(int(a_t))
                
            agg_times_set.sort()
            
            text = "\n\nPosition    Username   Status    Current_Puzzle_Time  Total_Puzzle_Time\n"
            underline(text)
            count = 1
            
            for ele in agg_times_set:
               for item in file_set: 
                    if item[1] == "finished":
                        if math.floor(float(item[3])) == ele:
                            print(f" #{count:<5}{item[0]:^15}{item[1]:^10}{str(datetime.timedelta(seconds = int(item[2]))):^21}{str(datetime.timedelta(seconds = int(ele))):^20}\n")
                            count += 1
            for ele in agg_times_set:
               for item in file_set: 
                    if item[1] == "puzzle_five":
                        if math.floor(float(item[3])) == ele:
                            print(f" #{count:<5}{item[0]:^15}{item[1]:^10}{str(datetime.timedelta(seconds = int(item[2]))):^20}{str(datetime.timedelta(seconds = int(ele))):^20}\n")
                            count += 1
            for ele in agg_times_set:
               for item in file_set: 
                    if item[1] == "puzzle_four":
                        if math.floor(float(item[3])) == ele:
                            print(f" #{count:<5}{item[0]:^15}{item[1]:^10}{str(datetime.timedelta(seconds = int(item[2]))):^20}{str(datetime.timedelta(seconds = int(ele))):^20}\n")
                            count += 1
            for ele in agg_times_set:
               for item in file_set: 
                    if item[1] == "puzzle_three":
                        if math.floor(float(item[3])) == ele:
                            print(f" #{count:<5}{item[0]:^15}{item[1]:^10}{str(datetime.timedelta(seconds = int(item[2]))):^18}{str(datetime.timedelta(seconds = int(ele))):^21}\n")
                            count += 1
            for ele in agg_times_set:
                for item in file_set:                
                    if item[1] == "puzzle_two":
                        if math.floor(float(item[3])) == ele:
                            print(f" #{count:<5}{item[0]:^15}{item[1]:^10}{str(datetime.timedelta(seconds = int(item[2]))):^21}{str(datetime.timedelta(seconds = int(ele))):^20}\n")
                            count += 1
            for ele in agg_times_set:
               for item in file_set:                 
                    if item[1] == "puzzle_one":
                        if math.floor(float(item[3])) == ele:
                            print(f" #{count:<5}{item[0]:^15}{item[1]:^10}{str(datetime.timedelta(seconds = int(item[2]))):^21}{str(datetime.timedelta(seconds = int(ele))):^20}\n")
                            count += 1
        
        lb.close()
    
    # Method to show player status bar.
    
    def status_bar(puzzle): 

        if puzzle == "puzzle_one":
            text.Colour("\nStatus :  " + "[" + "-" * 10 + "]" + "  0% complete\n").cyan()
        elif puzzle == "puzzle_two":
            text.Colour("\nStatus :  " + "[" + "■"*2 + "-" * 8 + "]" + "  20% complete\n").cyan()
        elif puzzle == "puzzle_three":
            text.Colour("\nStatus :  " + "[" + "■"*4 + "-" * 6 + "]" + "  40% complete\n").cyan()
        elif puzzle == "puzzle_four":
            text.Colour("\nStatus :  " + "[" + "■"*6 + "-" * 4 + "]" + "  60% complete\n").cyan()
        elif puzzle == "puzzle_five":
            text.Colour("\nStatus :  " + "[" + "■"*8 + "-" * 2 + "]" + "  80% complete\n").cyan()
        elif puzzle == "finished":
            text.Colour("\nStatus :  " + "[" + "■"*10 + "]" + "  100% complete\n").cyan()
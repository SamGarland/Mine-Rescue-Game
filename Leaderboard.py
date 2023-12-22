
"""
This is the Leaderboard class
 
"""

import time
import os

class Leaderboard():
    
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
        
        try:

            with open("leaderboard.txt", "r") as lb, open("new_leaderboard.txt", "a") as new_lb:
                
                lines = lb.readlines()
                
                for line in lines:
                                    
                    line = line.strip("\n").split(",")
                    
                    usernames.append(line[0])
                    
                    if line[0] == username:
                        
                        agg_time = float(line[3]) + float(count_time)
                        
                        update = Leaderboard(username, puzzle, count_time, agg_time)
                        
                        new_lb.write(f"{str(update)}\n")
                        
                    elif line != username:
                        user = line[0]
                        status = line[1]
                        puzzle_time = line[2]
                        time = line[3]
                        new_lb.write(f"{user},{status},{puzzle_time},{time}\n")
                        
            os.remove("Leaderboard.txt")
            os.rename("new_leaderboard.txt", "Leaderboard.txt")
        
            lb.close()
        
        except:
            pass
        
        with open("leaderboard.txt", "r+") as lb:
             
             lines = lb.readlines()
             
             for line in lines:
                                 
                 line = line.strip("\n").split(",")
                 
                 usernames.append(line[0])
             
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
        
        file_set = []
        agg_times_set = []
        
        with open("Leaderboard.txt", "r") as lb:
            
            lines = lb.readlines()
            
            for line in lines:
                line = line.strip("\n").split(",")
                file_set.append(line)
                agg_times_set.append(line[3])
            
            agg_times_set.sort()
            
            text = f"\n\nPosition    Username   Status    Current_Puzzle_Time  Total_Puzzle_Time\n"
            underline(text)
            
            count = 1
            
            for ele in agg_times_set:
                for item in file_set:
                    if item[3] == ele:
                        print(f" #{count}          {item[0]}    {item[1]}  {item[2]}  {item[3]}\n")
                        count += 1
        lb.close()
            
    def count_time(start_time, end_time):
        
        puzzle_time = end_time - start_time
        
        return puzzle_time
    
    def status_bar(puzzle):

        if puzzle == "puzzle_one":
            print("\nStatus :  " + "[" + "-" * 10 + "]" + "  0% complete\n")
        elif puzzle == "puzzle_two":
            print("\nStatus :  " + "[" + "■"*2 + "-" * 8 + "]" + "  20% complete\n")
        elif puzzle == "puzzle_three":
            print("\nStatus :  " + "[" + "■"*4 + "-" * 6 + "]" + "  40% complete\n")
        elif puzzle == "puzzle_four":
            print("\nStatus :  " + "[" + "■"*6 + "-" * 4 + "]" + "  60% complete\n")
        elif puzzle == "puzzle_five":
            print("\nStatus :  " + "[" + "■"*8 + "-" * 2 + "]" + "  80% complete\n")
        elif puzzle == "finished":
            print("\nStatus :  " + "[" + "■"*10 + "]" + "  100% complete\n")

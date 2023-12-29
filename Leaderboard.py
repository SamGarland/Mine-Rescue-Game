
"""
This is the Leaderboard class
 
"""
import datetime
import math
import os

class Leaderboard:

    def __init__(self, username, puzzle, count_time):
        
        self.username = username
        self.puzzle = puzzle
        self.count_time = count_time
    
    def __str__(self,  agg_time):
        return (f"{self.username},{self.puzzle},{self.count_time},{agg_time}\n")

    def count_time(start_time, end_time):
        
        start_time = math.trunc(start_time)
        end_time = math.trunc(end_time)
        
        count_time = (end_time) - (start_time)
        
        return count_time
    
    def update_leaderboard(self):
        
        usernames = []
        
        try:

            with open("leaderboard.txt", "r") as lb, open("new_leaderboard.txt", "a+") as new_lb:
                
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
                        
            os.remove("Leaderboard.txt")
            os.rename("new_leaderboard.txt", "Leaderboard.txt")
        
            lb.close()
        
        except:
            print("Failure to update the leaderboard!")
        
        with open("leaderboard.txt", "r+") as lb:
             
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
                         print("We got an issue updating the leaderboard!")
             except:
                 print("Failure to update the leaderboard!")
        
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
                            print(f" #{count}          {item[0]}       {item[1]}       {str(datetime.timedelta(seconds = int(item[2])))}              {str(datetime.timedelta(seconds = int(ele)))}\n")
                            count += 1
            for ele in agg_times_set:
               for item in file_set: 
                    if item[1] == "puzzle_five":
                        if math.floor(float(item[3])) == ele:
                            print(f" #{count}          {item[0]}       {item[1]}       {str(datetime.timedelta(seconds = int(item[2])))}              {str(datetime.timedelta(seconds = int(ele)))}\n")
                            count += 1
            for ele in agg_times_set:
               for item in file_set: 
                    if item[1] == "puzzle_four":
                        if math.floor(float(item[3])) == ele:
                            print(f" #{count}          {item[0]}       {item[1]}       {str(datetime.timedelta(seconds = int(item[2])))}              {str(datetime.timedelta(seconds = int(ele)))}\n")
                            count += 1
            for ele in agg_times_set:
               for item in file_set: 
                    if item[1] == "puzzle_three":
                        if math.floor(float(item[3])) == ele:
                            print(f" #{count}          {item[0]}       {item[1]}       {str(datetime.timedelta(seconds = int(item[2])))}              {str(datetime.timedelta(seconds = int(ele)))}\n")
                            count += 1
            for ele in agg_times_set:
                for item in file_set:                
                    if item[1] == "puzzle_two":
                        if math.floor(float(item[3])) == ele:
                            print(f" #{count}          {item[0]}       {item[1]}       {str(datetime.timedelta(seconds = int(item[2])))}              {str(datetime.timedelta(seconds = int(ele)))}\n")
                            count += 1
            for ele in agg_times_set:
               for item in file_set:                 
                    if item[1] == "puzzle_one":
                        if math.floor(float(item[3])) == ele:
                            print(f" #{count}          {item[0]}       {item[1]}       {str(datetime.timedelta(seconds = int(item[2])))}              {str(datetime.timedelta(seconds = int(ele)))}\n")
                            count += 1
        
        lb.close()

    
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
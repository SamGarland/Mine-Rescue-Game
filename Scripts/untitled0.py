import text

def restart_game(username):
    
    try:
        try:
            with open("../Resources/leaderboard.txt", "r") as lb:
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
                    
                    with open("../Resources/leaderboard.txt", "w") as lb:
                        for line in new_lines:
                            lb.write(line + '\n')
                text.Typed.typed_text(f"\nHowdy, {username}. Ya'll no longer in the leaderboard!\n\n")
            lb.close()
        except:
            text.Colour("\nSorry friend, we can't find ya'll in the leaderboard.\n\n").red()
        
        try:
            with open("../Resources/characters.txt", "r") as char:
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
                    
                    with open("../Resources/characters.txt", "w") as char:
                        for line in new_lines:
                            char.write(line + '\n')
                text.Typed.typed_text(f"\nHowdy, {username}. Ya'll gona be starting the game again any second!\n\n")
            char.close()
        except:
            text.Colour("\nSorry friend, we can't find ya'll character.\n\n").red()
    except:
        text.Colour("\nSorry friend, something went wrong with tryin'a restart the game for ya'll!\n\n").red()
username = "Dave"
restart_game(username)
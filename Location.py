
"""
This is the Location class

"""
import mine_rescue_main
import time

class Location():
    
    #This will only work if the puzzle name is initialised at the beginning of each puzzle as a local variable that can be used only when the puzzle is happening.
    # i.e. in the beginning of each puzzle method.
    
    def get_loc_info(puzzle):
        
        while True:
            user_input = input(print('''Give me a description of where I'm at - "l"
Look right - "r"
Look left - "l"
Look up - "u"
Look down - "d"
Back to the puzzle - "e"
'''))
            if user_input == "l":
                Location.description(puzzle)
            elif user_input == "r":
                Location.look_right(puzzle)
            elif user_input == "l":
                Location.look_left(puzzle)
            elif user_input == "u":
                Location.look_up(puzzle)
            elif user_input == "d":
                Location.look_down(puzzle)
            elif user_input == "e":
                break
            else:
                print("\nI'm not sure what you entered there, but it aint one of the options!\n")
    
    def description(puzzle):
        #This takes the puzzle name and returns a brief description of the location.
        if puzzle == "puzzle_one":
            print("Ya'll at the entrance to the Lower Creek Gold Mine. Damn, it's hot out here!\n")
            time.sleep(2)
            print("Better see what this guy wants so we can figure out what's a happened to all them miners...\n")
            time.sleep(2)
        elif puzzle == "puzzle_two":
            print("You're inside the mine, heading down the railway track. Boy, it's a loooong way!\n")
            time.sleep(2)
            print("There's someone approaching. Quickly, go see what they want. Maybe they can help figure out what's going on in here...\n")
            time.sleep(2)
        elif puzzle == "puzzle_three":
            print("It's getting tight in here partner.\n")
            time.sleep(1)
            print("Damn, I can hardly breath!\n")
            time.sleep(1)
            print("Cough! Cough!\n")
            time.sleep(2)
            print("Sorry, about that. Looks like there's a collapsed tunnel up ahead.\n")
            time.sleep(1)
            print("Hell, look! There's light on the other side!\nGo see if there's anyone there...\n")
        elif puzzle == "puzzle_four":
            print("It's some kind of underground lake. Maybe it's a flooded cavern?\n")
            time.sleep(1)
            print("Oh my lord, it smells baaaad in here!\n")
            time.sleep(1)
            print("I think this tunnel is leaking gas partner. Better stick that mask on!\n")
            time.sleep(2)
            print("Hey look! There's a fella crouching over there in the shadows. Let's see what he wants...\n")
        elif puzzle == "puzzle_five":
            print("This must be it! I can hear the miners!")
            time.sleep(1)
            print("They're trapped in the lift shaft. Go over to the panel and see if you can figure out how to get it up and running again...\n")
            time.sleep(2)
        else:
            print("\nSeems like you're lost my friend. I don't know where ya'll at!\n")
    
    def look_right(puzzle):
        # This allows the player to look right.
        if puzzle == "puzzle_one":
            print("That big building is the pump house. That pumps all the water out of the mine, so it don't get too dangerous down there.\n")
            time.sleep(1)
        elif puzzle == "puzzle_two":
            print("The tracks are mighty wide in here.\n")
            time.sleep(1)
            print("Looks like there are about six or seven different lines. I wonder which one I need to take?\n")
            time.sleep(1)
        elif puzzle == "puzzle_three":
            print("I can't see much over there.\nJust a couple ol' oil lamps and some crates.\n")
            time.sleep(1)
        elif puzzle == "puzzle_four":
            print("Wow! This place is huge!\n")
            time.sleep(2)
            print("I wonder what happens if I shout:\n")
            time.sleep(1)
            print("ECHO!\n")
            time.sleep(1)
            print("echo...\n")
            time.sleep(1)
            print("echo...\n")
            time.sleep(1)
        elif puzzle == "puzzle_five":
            print("There's the panel! Looks kind of rusty and old, but maybe you can figure something out...\n")
            time.sleep(1)
        else:
            print("\nSeems like you're lost my friend. I don't know where ya'll at!\n")
    
    def look_left(puzzle):
        # This allows the player to look left.
        if puzzle == "puzzle_one":
            print("Them mountains are mighty big off in the distance. Nothing between here and there but scorched desert...\n")
            time.sleep(1)
        elif puzzle == "puzzle_two":
            print("The tracks are mighty wide in here.\n")
            time.sleep(1)
            print("Looks like there are about six or seven different lines. I wonder which one I need to take?\n")
            time.sleep(1)
        elif puzzle == "puzzle_three":
            print("Just plain ol' rock this way. Looks like a no-go.\n")
            time.sleep(1)
        elif puzzle == "puzzle_four":
            print("How'd this place get so flooded?\n")
            time.sleep(2)
            print("Probably that pumping station out the front aint working.\nMaybe that's why the miners are stuck?\n")
            time.sleep(1)
        elif puzzle == "puzzle_five":
            print("Looks like some sort of substation...\n")
            time.sleep(2)
            print("Better not get too close in case it got flooded!\n")
            time.sleep(1)
        else:
            print("\nSeems like you're lost my friend. I don't know where ya'll at!\n")
        
    
    def look_up(puzzle):
        # This allows the player to look up.
        if puzzle == "puzzle_one":
            print("Beautiful blue! Not a cloud in the sky!\n")
            time.sleep(1)
        elif puzzle == "puzzle_two":
            print("They've sure put a lot of effort into holding up that ceiling!\nThose beams look mighty strong.\n")
            time.sleep(1)
        elif puzzle == "puzzle_three":
            print("I can't even tilt my head to look up. I hope ya'll aint clostrophobic or nothing...\n")
            time.sleep(1)
        elif puzzle == "puzzle_four":
            print("I can jus about see the roof of this thing.\n")
            time.sleep(2)
            print("It's damn enormous in here!\n")
            time.sleep(1)
        elif puzzle == "puzzle_five":
            print("Just a load of mesh I guess.\n")
            time.sleep(1)
        else:
            print("\nSeems like you're lost my friend. I don't know where ya'll at!\n")
    
    def look_down(puzzle):
        # This allows the player to look down.
        if puzzle == "puzzle_one":
            print("Nothing much around here on the floor. Just a bunch of dust bits of old oily rag...\n")
            time.sleep(1)
        elif puzzle == "puzzle_two":
            print("There's bits of track all over the place.\n")
            time.sleep(1)
            print("Amazing they don't get more accidents in here...\n")
            time.sleep(1)
        elif puzzle == "puzzle_three":
            print("Yep, jus my boots...\n")
            time.sleep(1)
            print("I can't see much in here.\n")
            time.sleep(1)
        elif puzzle == "puzzle_four":
            print("Aw man! My boots are all wet...\n")
            time.sleep(1)
        elif puzzle == "puzzle_five":
            print("There's loads of bits of wire all over the floor... What in the name happened here?\n")
            time.sleep(2)
            print("I bet that panel will give us a clue or two. Better get over there!\n")
            time.sleep(2)
        else:
            print("\nSeems like you're lost my friend. I don't know where ya'll at!\n")
    

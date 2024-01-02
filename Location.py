
"""
This is the Location class

"""
import time
import text

def get_loc_info(puzzle):
    
    while True:
        user_input = input(text.Colour('''\n\nGive me a description of where I'm at - "w"
Look right - "r"
Look left - "l"
Look up - "u"
Look down - "d"
Back to the puzzle - "e"
:''').input_cyan())
        try:
            if user_input == "w":
                description(puzzle)
            elif user_input == "r":
                look_right(puzzle)
            elif user_input == "l":
                look_left(puzzle)
            elif user_input == "u":
                look_up(puzzle)
            elif user_input == "d":
                look_down(puzzle)
            elif user_input == "e":
                break
            else:
                text.Colour("\nI'm not sure what you entered there, but it aint one of the options!\n").red()
        except:
            text.Colour("\nI'm not sure what you entered there, but it aint one of the options!\n").red()

def description(puzzle):
    #This takes the puzzle name and returns a brief description of the location.
    try:
        if puzzle == "puzzle_one":
            text.Colour("Ya'll at the entrance to the Lower Creek Gold Mine. Damn, it's hot out here!\n").cyan()
            time.sleep(2)
            text.Colour("Better see what this guy wants so we can figure out what's a happened to all them miners...\n").cyan()
            time.sleep(2)
        elif puzzle == "puzzle_two":
            text.Colour("You're inside the mine, heading down the railway track. Boy, it's a loooong way!\n").cyan()
            time.sleep(2)
            text.Colour("There's someone approaching. Quickly, go see what they want. Maybe they can help figure out what's going on in here...\n").cyan()
            time.sleep(2)
        elif puzzle == "puzzle_three":
            text.Colour("It's getting tight in here partner.\n").cyan()
            time.sleep(2)
            text.Colour("Damn, I can hardly breath!\n").cyan()
            time.sleep(2)
            text.Colour("Cough! Cough!\n").cyan()
            time.sleep(2)
            text.Colour("Sorry, about that. Looks like there's a collapsed tunnel up ahead.\n").cyan()
            time.sleep(2)
            text.Colour("Hell, look! There's light on the other side!\nGo see if there's anyone there...\n").cyan()
        elif puzzle == "puzzle_four":
            text.Colour("It's some kind of underground lake. Maybe it's a flooded cavern?\n").cyan()
            time.sleep(2)
            text.Colour("Oh my lord, it smells baaaad in here!\n").cyan()
            time.sleep(2)
            text.Colour("I think this tunnel is leaking gas partner. Better stick that mask on!\n").cyan()
            time.sleep(2)
            text.Colour("Hey look! There's a fella crouching over there in the shadows. Let's see what he wants...\n").cyan()
        elif puzzle == "puzzle_five":
            text.Colour("This must be it! I can hear the miners!").cyan()
            time.sleep(2)
            text.Colour("They're trapped in the lift shaft. Go over to the panel and see if you can figure out how to get it up and running again...\n").cyan()
            time.sleep(2)
        else:
            text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()
    except:
        text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()

def look_right(puzzle):
    # This allows the player to look right.
    try:
        if puzzle == "puzzle_one":
            text.Colour("That big building is the pump house. That pumps all the water out of the mine, so it don't get too dangerous down there.\n").cyan()
            time.sleep(2)
        elif puzzle == "puzzle_two":
            text.Colour("The tracks are mighty wide in here.\n").cyan()
            time.sleep(2)
            text.Colour("Looks like there are about six or seven different lines. I wonder which one I need to take?\n").cyan()
            time.sleep(2)
        elif puzzle == "puzzle_three":
            text.Colour("I can't see much over there.\nJust a couple ol' oil lamps and some crates.\n").cyan()
            time.sleep(2)
        elif puzzle == "puzzle_four":
            text.Colour("Wow! This place is huge!\n").cyan()
            time.sleep(2)
            text.Colour("I wonder what happens if I shout:\n").cyan()
            time.sleep(1)
            text.Colour("ECHO!\n").cyan()
            time.sleep(1)
            text.Colour("echo...\n").cyan()
            time.sleep(1)
            text.Colour("echo...\n").cyan()
            time.sleep(1)
        elif puzzle == "puzzle_five":
            text.Colour("There's the panel! Looks kind of rusty and old, but maybe you can figure something out...\n").cyan()
            time.sleep(2)
            text.Colour("Ahah! Look on the wall there!\n\n[Written on the wall] +, -, 98, 7, 6, 5, 4, 3, 2, 1... 100?\n").cyan()
            time.sleep(2)
            text.Colour("Them must be the notes that they's talking bout!").cyan()
            time.sleep(2)
        else:
            text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()
    except:
        text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()

def look_left(puzzle):
    # This allows the player to look left.
    try:
        if puzzle == "puzzle_one":
            text.Colour("Them mountains are mighty big off in the distance. Nothing between here and there but scorched desert...\n").cyan()
            time.sleep(2)
        elif puzzle == "puzzle_two":
            text.Colour("The tracks are mighty wide in here.\n").cyan()
            time.sleep(2)
            text.Colour("Looks like there are about six or seven different lines. I wonder which one I need to take?\n").cyan()
            time.sleep(2)
        elif puzzle == "puzzle_three":
            text.Colour("Just plain ol' rock this way. Looks like a no-go.\n").cyan()
            time.sleep(2)
        elif puzzle == "puzzle_four":
            text.Colour("How'd this place get so flooded?\n").cyan()
            time.sleep(2)
            text.Colour("Probably that pumping station out the front aint working.\nMaybe that's why the miners are stuck?\n").cyan()
            time.sleep(2)
        elif puzzle == "puzzle_five":
            text.Colour("Looks like some sort of substation...\n").cyan()
            time.sleep(2)
            text.Colour("Better not get too close in case it got flooded!\n").cyan()
            time.sleep(2)
        else:
            text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()
    except:
        text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()

def look_up(puzzle):
    # This allows the player to look up.
    try:
        if puzzle == "puzzle_one":
            text.Colour("Beautiful blue! Not a cloud in the sky!\n").cyan()
            time.sleep(2)
        elif puzzle == "puzzle_two":
            text.Colour("They've sure put a lot of effort into holding up that ceiling!\nThose beams look mighty strong.\n").cyan()
            time.sleep(2)
        elif puzzle == "puzzle_three":
            text.Colour("I can't even tilt my head to look up. I hope ya'll aint clostrophobic or nothing...\n").cyan()
            time.sleep(2)
        elif puzzle == "puzzle_four":
            text.Colour("I can jus about see the roof of this thing.\n").cyan()
            time.sleep(2)
            text.Colour("It's damn enormous in here!\n").cyan()
            time.sleep(2)
        elif puzzle == "puzzle_five":
            text.Colour("Just a load of mesh I guess.\n").cyan()
            time.sleep(2)
        else:
            text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()
    except:
        text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()

def look_down(puzzle):
    # This allows the player to look down.
    try:
        if puzzle == "puzzle_one":
            text.Colour("Nothing much around here on the floor. Just a bunch of dust bits of old oily rag...\n").cyan()
            time.sleep(2)
        elif puzzle == "puzzle_two":
            text.Colour("There's bits of track all over the place.\n").cyan()
            time.sleep(2)
            text.Colour("Amazing they don't get more accidents in here...\n").cyan()
            time.sleep(2)
        elif puzzle == "puzzle_three":
            text.Colour("Yep, jus my boots...\n").cyan()
            time.sleep(2)
            text.Colour("I can't see much in here.\n").cyan()
            time.sleep(2)
        elif puzzle == "puzzle_four":
            text.Colour("Aw man! My boots are all wet...\n").cyan()
            time.sleep(2)
        elif puzzle == "puzzle_five":
            text.Colour("There's loads of bits of wire all over the floor... What in the name happened here?\n").cyan()
            time.sleep(2)
            text.Colour("I bet that panel will give us a clue or two. Better get over there!\n").cyan()
            time.sleep(2)
        else:
            text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()
    except:
        text.Colour("\nSeems like you're lost my friend. I don't know where ya'll at!\n").red()
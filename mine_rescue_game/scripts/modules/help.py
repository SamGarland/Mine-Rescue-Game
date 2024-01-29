'''
This is the help module with Help class and methods.
These provide the player with guidance on how to approach the puzzles and provides common mistakes.
'''

#==== Imports ====#

import time
import text

# ==== Class and methods ===#

class Help:

    # Constructor.
    def __init__(self, username, puzzle):
        self.username = username
        self.puzzle = puzzle

    # Method to show help menu.
    def get_help(self):

        while True:
            user_input = input(text.Colour('''\n\nGeneral Guidance - g
Common Mistakes - m
Back to the puzzle - e
:''').input_cyan())
            user_input.strip()

            if user_input == "g":
                self.general_guidance()
            elif user_input == "m":
                self.common_mistakes()
            elif user_input == "e":
                break
            else:
                text.Colour("\nI'm not sure what you entered there, but it ain't one of the options!\n").red()

    # Method gives guidance for the task in each puzzle
    def general_guidance(self):
        try:
            if self.puzzle == "puzzle_one":
                time.sleep(1)
                text.Colour('''
Your task is to decrypt a sentence that has been scrambled.
All the letters have shifted by the same number of spaces, for example:
if the scrambled sentence is "Ifmmp xpsme", by finding the words have shifted 
by one place (A -> B -> C), you know this sentence says "Hello World".

Your goal is to figure out the original sentence and identify the key word,
which will be the final word in all capitals.''').cyan()
            elif self.puzzle == "puzzle_two":
                time.sleep(1)
                text.Colour('''
You need to determine the height of an arch based on the given scenario and constraints.
The expansion has formed a triangle shape, the height will be at the centre of the track.''').cyan()
            elif self.puzzle == "puzzle_three":
                time.sleep(1)
                text.Colour('''
You're faced with a collapsed tunnel and need to figure out the minimum 
number of breaks needed to fix a chain to crawl through a narrow space.
By breaking one link, you can attach two chains together.''').cyan()
            elif self.puzzle == "puzzle_four":
                time.sleep(1)
                text.Colour('''
You must plan how to safely transport a group of items across a lake using a rickety boat. 
Plan your moves to ensure all items and yourself get across safely without any accidents.
You must be able to find the fastest solution, requiring the least journeys as the lake is flooding.''').cyan()
            elif self.puzzle == "puzzle_five":
                time.sleep(1)
                text.Colour('''
Your task is to solve a numerical puzzle to operate a lift shaft and rescue trapped miners.
In this task, you must make sure to do the correct operations to get to 100
e.g. with 25,50,12,13 can be 25+50+12+13 = 100.''').cyan()
            else:
                text.Colour("\nThere is no such puzzle!").red()
        except:
            text.Colour("\nAn error occurred while trying to provide help.").red()

    # Method highlights common mistakes in each puzzle
    def common_mistakes(self):
        try:
            if self.puzzle == "puzzle_one":
                time.sleep(1)
                text.Colour("- Don't forget to enter only the KEYWORD is this task.").cyan()
            elif self.puzzle == "puzzle_two":
                time.sleep(1)
                text.Colour('''
- Convert the final answer to metres (1 Metre = 100cm)
- Don't guess it, calculate it!''').cyan()
            elif self.puzzle == "puzzle_three":
                time.sleep(1)
                text.Colour("\nMake sure you break enough links to join all of the parts together.").cyan()
            elif self.puzzle == "puzzle_four":
                time.sleep(1)
                text.Colour('''
- Don't forget how each item interacts with each other.
- You can only carry one item at a time.
- Don't repeatedly move an item and waste time!''').cyan()
            elif self.puzzle == "puzzle_five":
                time.sleep(1)
                text.Colour('''
- Don't change the order of the numbers given, it has to stay the same!
- Don't forget the aim is 100, don't go over and don't be under.''').cyan()
            else:
                text.Colour("\nThere is no such puzzle!").red()
        except:
            text.Colour("\nAn error occurred while trying to provide a reminder.").red()

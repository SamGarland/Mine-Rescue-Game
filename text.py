'''
This module contains Typed and Colour classes that manipulate text.

'''
import time

#==== Typed class for typing out text =====#

class Typed:
    
    def typed_text(sentence): 
        for char in sentence:
            time.sleep(0.05)
            print(char, end="", flush=True)
            
    def typed_text_fast(sentence): 
        for char in sentence:
            time.sleep(0.002)
            print(char, end="", flush=True)
    
    #Intro Script
    def intro():
        Typed.typed_text("""
Welcome to Mine Rescue, the ultimate test of skills, set in the daring and rugged expanse of the wild west.

A dreadful situation has unfolded at the local mine near your town.
A terrible accident has caused the locals who work in the mine to be trapped!

Your mission, if you choose to accept, is a race against time to save the miners trapped below.
A critical expedition lies before you in the dark and dangerous tunnels of the mine.

So gather your resolve explorer, and prepare to venture into the unknown. The mysteries of the mines are  yours to solve, each bringing you a step closer to the miners below. 
\n\n\n\n\n\n""")
    
    def intro_image():
        #Intro_Image_One
        Typed.typed_text_fast("""
        0     0  00000  0     0  000000                
        00   00    0    00    0  0                     
        0 0 0 0    0    0 0   0  0                     
        0  0  0    0    0  0  0  0000                  
        0     0    0    0   0 0  0                     
        0     0    0    0    00  0                     
        0     0  00000  0     0  000000                

        000000    000000  000000  000000  0    0  000000
        0     0   0       0       0       0    0  0     
        0     0   0       0       0       0    0  0     
        000000    0000    000000  0       0    0  0000  
        0   0     0            0  0       0    0  0     
        0    0    0            0  0       0    0  0     
        0     0   000000  000000  000000  000000  000000

        """)
        
    def image_one():
        #Puzzle_One_Image_One
        Typed.typed_text_fast("""
                                                       ____________ 
                                                       |   MINE   | 
                                                       | ENTRANCE | 
                                                    ################
                                                 ###################
                                                ####################
                                               #######            ##
                                             ########             ##
                                            #########       O     ##
            _______                        #########       /|\    ##
           |DANGER!|                      #########        / \    ##
           |_______|                     ##########               ##
               |                      #############               ##
               |                    ################################
        ############################################################
        ############################################################
        ############################################################
""")
        
    def image_two():
        #Puzzle_Two_Image_One
        Typed.typed_text_fast("""
                                     *
                                 *       *
                             *               *
                         *                       *
                     *                               *
                 *                   mp                  *    
              ...............................................

        [.....] original track
        [*****] buckled track
        [mp] mid point
""")
        
    def image_three():
        
        #Puzzle_Three_Image_One
        Typed.typed_text_fast("""
               #########       
             #############     
            ###############    
           #################   
          ###################  
         ##################### 
        #######################
        #######################
        #######################
        #######################
        #######################
        #######################
        ############     ######
        ###########     #######
        #######################
        #######################
             //      //
            //      //
           //      //
          //      //
         //      //

""")
            
    def image_four():
        
        #Puzzle_Four_Image_One
        Typed.typed_text_fast("""
        ______________
        \\\          //                          _____
         \\\        //                          |
        ~~^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~|
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")

    def image_five():
        
        #Puzzle_Five_Image_One

        Typed.typed_text_fast("""
              
                        ________________________
               Help! ---|--O      O      O      |
                        | /|\    /|\    /|\     |
                        | / \    / \    / \     |
          It's Dark! ---|-----O      O      O   |
                        |    /|\    /|\    /|\  |
                        |    / \    / \    / \  |
                        |_______________________|

""")


class Colour:
    
    def __init__(self, text):
        
        self.text = text
    
    def green(self): 
        for char in self.text:
            time.sleep(0.05)
            char = "\u001b[32m{ele}\u001b[0m".format(ele=char)
            print(char, end="", flush=True)
    
    def cyan(self): 
        for char in self.text:
            time.sleep(0.05)
            char = "\u001b[36m{ele}\u001b[0m".format(ele=char)
            print(char, end="", flush=True)
    
    def magenta(self):
        for char in self.text:
            time.sleep(0.05)
            char = "\u001b[35m{ele}\u001b[0m".format(ele=char)
            print(char, end="", flush=True)
            
    def red(self):
        for char in self.text:
            time.sleep(0.05)
            char = "\u001b[31m{ele}\u001b[0m".format(ele=char)
            print(char, end="", flush=True)
            
    def input_cyan(self):
        return "\u001b[36m{ele}\u001b[0m".format(ele=self.text)
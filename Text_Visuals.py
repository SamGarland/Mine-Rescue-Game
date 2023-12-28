import time

def typed_text(sentence): 
    for char in sentence:
        time.sleep(0.05)
        print(char, end="", flush=True)
        
def typed_text_fast(sentence): 
    for char in sentence:
        time.sleep(0.002)
        print(char, end="", flush=True)

#Intro Script
typed_text("""
Welcome to Mine Rescue, the ultimate test of skills, set in the daring and rugged expanse of the wild west.

A dreadful situation has unfolded at the local mine near your town.
A terrible accident has caused the locals who work in the mine to be trapped!

Your mission, if you choose to accept, is a race against time to save the miners trapped below.
A critical expedition lies before you in the dark and dangerous tunnels of the mine.

So gather your resolve explorer, and prepare to venture into the unknown. The mysteries of the mines are  yours to solve, each bringing you a step closer to the miners below. 
""")

#Intro_Image_One
typed_text_fast("""
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




#Puzzle_One_Image_One
typed_text_fast("""
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

   


#Puzzle_Two_Image_One
print("""
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

#Puzzle_Three_Image_One
print("""
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

#Puzzle_Four_Image_One
print("""
______________
\\\          //                          _____
 \\\        //                          |
~~^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")


#Puzzle_Five_Image_One

print("""
      
                ________________________
       Help! ---|--O      O      O      |
                | /|\    /|\    /|\     |
                | / \    / \    / \     |
  It's Dark! ---|-----O      O      O   |
                |    /|\    /|\    /|\  |
                |    / \    / \    / \  |
                |_______________________|

""")
     
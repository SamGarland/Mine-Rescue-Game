"""
This is the avatar module with Avatar class.

"""
class Avatar:
    
    def __init__(self):
        # Dictionary to hold speech for each character
        self.characters = {
            # Avatar for puzzle_one
            "railwayman_one": {
                "intro": "Tm st ymj fwj fqq ytwwid!"
            },
            # Avatar for puzzle_two
            "railwayman_two": {
                "intro": (
                    '''The heat of the mining equipment has caused the 100-metre rails to expand!
                    
They've expanded by a whole metre, creating a bit of a predicament.

The rails have formed an arch, buckling upward right at the center.

You gotta figure out just how high this arch is at the midpoint (mp), 
if it ain't that high you might just make it.\n\n'''),
                "prompt_hint": "I might be able to give you a hand, Y'all got a hammer?\n\n",
                "hint": "\nI reckon old Pythagoras would know the answer, A square plus B square or something I think\n\n", },
            #TODO make and insert image for puzzles
            
            # Avatar for puzzle_three
            "miner_crawlspace": {
                "intro": (
                    '''I can pull ya through with this here chain, but my good riddens, it's in 5 pieces!
                    
Each piece has 4 links. I can only mend it by breakin' each links and then joinin' 'em back together.

How many links do I gotta break to fix this chain up?\n\n'''),    
                "prompt_hint": "I might have some old tricks up me slieves, y'all got a lasso?\n\n",
                "hint": "\nDon't one chain got 4 links? dunno if you gotta break em all\n\n", },
            #TODO make and insert image for puzzles
            
            # Avatar for puzzle_four
            "miner_two": {
                "intro": (
                    '''Boy am I glad to see you! Just a warning 'bout that dynamite, some scary stuff.
                    
That sneaky lil rat's got a taste for trouble. Can't leave it alone with that stuff or it's a heap of trouble.

And don't ya dare leave it wit me, I tend to get a bit shaky and before we know it... kaboom\n\n'''),
                "prompt_hint": "I might have some old wisdom in here somewhere, y'all got a mask?\n\n",                 
                "hint": "\nI'd get going wit that dynamite first, shouldn't take more than 7 trips I reckon\n\n", },

            # Avatar for puzzle_five
            "trapped_miner": {
                "intro": ('''We think the lift has stalled and we'be been trapped down here for quite some time!
                          
There's 17 of us...Can ya'll see anything that might have gone wrong up there?

If ya'll take a look at the control panel, you might be able to restart the engine...

There's a series of coloured switches that bring in power to the lift that have to add up to 100 Volts. No more, no less!

I think the lift guy usually makes some notes on the wall. Have a look around to see if you can't find'em.

Then see if ya'll can't get them engines up and running!

Remember, you gotta match up them power sources to get to exactly 100!\n\n'''),
                "prompt_hint": "We can help ya'll figure it out, but you're gona need something to take notes. Ya'll got a notebook up there?",   
                "hint": "\nTake a look around and maybe you'll see some notes on the wall. Remember, decrease before you increase!",
                "outro": '''Thank ya'll for rescuing us out of that tight spot! We're mighty thankfull!

We can take it from here and get this mine back in working order. 
                '''
            },
            }

    #Method for retreiving avatar's introductory speech /if not found prints default
    def get_intro(self, avatar_name):
        return self.characters.get(avatar_name).get("intro", "Unknown avatar")
    
    def get_outro(self, avatar_name):
        return self.characters.get(avatar_name).get("outro", "Unknown avatar")

    #Get avatar to prompt for a hint, asking for equipment
    def get_prompt(self, avatar_name):
        return self.characters.get(avatar_name).get("prompt_hint", "Unknown avatar")

    #Returns the avatar's hint 
    def get_hint(self, avatar_name):
        return self.characters.get(avatar_name).get("hint", "No hint found.") 
# TODO Make method for retreiving text-image
   

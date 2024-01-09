'''
This is the npc module with Npc class.
It contains a dictionary with text for different npcs, plus methods.

'''
#==== Class and methods ====#

class Npc:
    
    # Constructor.
    def __init__(self):
        # Dictionary to hold speech for each npc
        self.npc = {
            # npc for puzzle_one.
            "railwayman_one": {
                "intro": "Tm st ymj fwj fqq ytwwid!"
            },
            # npc for puzzle_two.
            "railwayman_two": {
                "intro": (
                    '''The heat of the mining equipment has caused 100-meters of rails to expand!
                    
They've expanded by one whole metre, creating a bit of a predicament.

The rails have formed an arch, buckling upward right at the center.

You gotta figure out just how high this arch is at the midpoint (mp), 
if it ain't that high you might just make it.\n\n'''),
                "prompt_hint": "I might be able to give you a hand, Y'all got a hammer?\nIf so, I'll swap ya'll a hammer for a hint?\n\n",
                "hint": "\nYipee! I've been needing me a hammer!\nAlrighty, a hint, I get it.\nI reckon old Pythagoras would know the answer, A squared plus B squared gives C squared or something... I think.\n\n"},
            
            # npc for puzzle_three.
            "miner_crawlspace": {
                "intro": (
                    '''I can pull ya through with this here chain, but my good riddens, it's in 5 pieces!
                    
Each piece has 4 links. I can only mend it by breakin' each links and then joinin' 'em back together.

How many links do I gotta break to fix this chain up?\n\n'''),    
                "prompt_hint": "\nI might have some old tricks up me sleeves, y'all got a lasso?\nIf so, I'll swap ya'll a lasso for a hint?\n\n",
                "hint": "\nGosh dang! I finally did get me a lasso! Might give up this mining lark and become a rancher.\nOh right, the hint.\nDon't one chain got 4 links? dunno if you gotta break em all...\n\n"},
            
            # npc for puzzle_four.
            "miner_two": {
                "intro": (
                    '''Boy am I glad to see you! Just a warning 'bout that dynamite, some scary stuff!
                    
That sneaky lil' rat's got a taste for trouble. Can't leave it alone with that!

And don't ya dare leave it wit me, I tend to get a bit shaky and before we know it... KABOOM!!!\n\n'''),
                "prompt_hint": "I might have some old wisdom in here somewhere, y'all got a mask?\nIf so, I'll swap ya'll a mask for a hint?\n\n",                 
                "hint": "\nAhhh, I can breath a bit better now.\nI'd get going wit that dynamite first, shouldn't take more than 7 trips I reckon.\n\n"},

            # npc for puzzle_five.
            "trapped_miner": {
                "intro": ('''We think the lift has stalled and we've been trapped down here for quite some time!
                          
There's a bunch of us...Can ya'll see anything that might have gone wrong up there?

If ya'll take a look at the control panel, you might be able to restart the engine...

There's a series of numbered switches that bring in power to the lift that have to add up to 100 Volts. No more, no less!

I think the lift guy usually makes some notes on the wall. Have a look around to see if you can't find'em.

Then see if ya'll can't get them engines up and running!

Remember, you gotta match up them power sources to get to exactly 100!\n\n'''),
                "prompt_hint": "We can help ya'll figure it out, but you're gona need something to take notes. Ya'll got a notebook up there?",   
                "hint": "\nTake a look around and maybe you'll see some notes to take on the wall. Remember, decrease before you increase!",
                "outro": '''Thank ya'll for rescuing us out of that tight spot! We're mighty thankfull!

We can take it from here and get this mine back in working order. 
'''
            },
            }

    # Method for retreiving npc's introductory speech /if not found prints default.
    def get_intro(self, npc_name):
        return self.npc.get(npc_name).get("intro", "Unknown avatar")
    
    # Method for retreiving npc's outro speech /if not found prints default.
    def get_outro(self, npc_name):
        return self.npc.get(npc_name).get("outro", "Unknown avatar")

    # Method to get npc to prompt for a hint - asking for equipment.
    def get_prompt(self, npc_name):
        return self.npc.get(npc_name).get("prompt_hint", "Unknown avatar")

    # Method to return npc's hint.
    def get_hint(self, npc_name):
        return self.npc.get(npc_name).get("hint", "No hint found.") 
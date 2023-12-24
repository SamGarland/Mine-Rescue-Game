"""
This is the Avatar class

"""
class Avatar:
    def __init__(self):
        # Dictionary to hold speech for each character
        self.characters = {
            # Avatar for puzzle_one
            "railwayman": {
                "intro": "Tm st ymj fwj fqq ytwwid!"
            },
            # Avatar for puzzle_two
            "railwayman_two": {
                "intro": (
                    "The heat of the mining equipment has caused the 100-metre rails to expand! "
                    "They've expanded by a whole metre, creating a bit of a predicament. "
                    "The rails have formed an arch, buckling upward right at the center. "
                    "You gotta figure out just how high this arch is at the midpoint (mp), "
                    "if it ain't that high you might just make it."),
                "prompt_hint": "I might be able to give you a hand, Y'all got a hammer?",
                "hint": "I reckon old Pythagoras would know the answer, A square plus B square or something I think", },
            #TODO make and insert image for puzzles
            
            # Avatar for puzzle_three
            "miner_one": {
                "intro": (
                    "I can pull ya through with this here chain, but my good riddens, it's in 5 pieces! "
                    "Each piece has 4 links. I can only mend it by breakin' each links and then joinin' 'em back together."
                    "How many links do I gotta break to fix this chain up? "),    
                "prompt_hint": "I might have some old tricks up me sleves, y'all got a lasso?",
                "hint": "Don't one chain got 4 links? dunno if you gotta break em all", },
            #TODO make and insert image for puzzles
            
            # Avatar for puzzle_four
            "miner_two": {
                "intro": (
                    "Boy am I glad to see you! Just a warning 'bout that dynamite, some scary stuff."
                    "Keep that sneaky lil rat's got a taste for trouble. Can't leave it alone with that stuff or it's a heap of trouble"
                    "And don't ya dare leave it wit me, I tend to get a bit shaky and before we know it... kaboom"),
                "prompt_hint": "I might have some old wisdom in here somewhere, y'all got a mask?",                 
                "hint": "I'd get going wit that dynamite first, shouldn't take more than 7 trips I reckon ", },

            # Avatar for puzzle_five
            "AVATAR_NAME": {
                "intro": "INSERT SPEECH",
                "prompt_hint": "INSERT PROMPT",   
                "hint": "INSERT HINT",
            },
            }

    #Method for retreiving avatar's introductory speech /if not found prints default
    def get_intro(self, avatar_name):
        return self.characters.get(avatar_name).get("intro", "Unknown avatar")

    #Get avatar to prompt for a hint, asking for equipment
    def get_prompt(self, avatar_name):
        return self.characters.get(avatar_name).get("prompt_hint", "Unknown avatar")

    #Returns the avatar's hint 
    def get_hint(self, avatar_name):
        return self.characters.get(avatar_name).get("hint", "No hint found.") 
# TODO Make method for retreiving text-image
"""
This is the Avatar class

"""
class Avatar:
    def __init__(self):
        # Dictionary to hold speech for each character
        self.characters = {
            # Character for puzzle_one
            "railwayman": {
                "intro": "Tm st ymj fwj fqq ytwwid!"
            },
            # Character for puzzle_two
            "railwayman_two": {
                "intro": (
                    "The heat of the mining equipment has caused the 100-metre rails to expand! "
                    "They've expanded by a whole metre, creating a bit of a predicament. "
                    "The rails have formed an arch, buckling upward right at the center. "
                    "You gotta figure out just how high this arch is at the midpoint (mp), "
                    "if it ain't that high you might just make it."
                ),
                "hint": "I reckon old Pythagoras would know the answer, A square with B square or something i think",

                #TODO make and insert image for puzzle
            },
            # Character for puzzle_three
            "miner": {
                "intro": "intro text",
                "hint": "Don't one chain got 4 links? dunno if you gotta break em all",

            },
            # Character for puzzle_four
            "miner_two": {
                "intro": "intro text",
                "hint": "Dynamite kinda sound scary, id start with that one",

            },
            }

    #Method for retreiving avatar's introductory speech /if not found prints default
    def get_intro(self, avatar_name):
        return self.characters.get(avatar_name, {}).get("intro", "Unknown avatar") #

    #Returns the avatar's hint 
    def get_hint(self, avatar_name, has_item):
        character = self.characters.get(avatar_name, {})
        return character.get("hint", "No hint found.")

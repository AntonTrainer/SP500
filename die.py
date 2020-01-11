from random import randint

# create a class that represents one die

class Die():

    # make the die 6 sided
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        # rolling the die is just picking a random number within the number of sides
        return randint(1, self.num_sides)


# molecular motion
from random import choice
import matplotlib.pyplot as plt

# ------------------------ Create a class that will fill define the walk points ---------------------------------------------------------

# create a call to create random walks


class RandomWalk():

    def __init__(self, num_points=5000):
        self.num_points = num_points

        # start all walks at (0,0), these lists will then be appended as the fill_walk function makes decisions
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):

        # keep taking steps until walk reaches desired len
        while len(self.x_values) < self.num_points:
            # chose the direction of the step in the walk left or right
            x_direction = choice([-1, 1])
            # chose the distance left or right for the step
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance  # combine the direction and distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # ignore moves that go no where
            if x_step == 0 and y_step == 0:
                continue

            # generate the next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

    # implement the step
            self.x_values.append(next_x)
            self.y_values.append(next_y)


# -------------------------------- Run and display the walk ----------------------------------------------------------


while True:
    steps = int(input("Type a number of desired steps (max 50000): "))
    if steps > 50000:
        break
    rw = RandomWalk(steps)
    rw.fill_walk()

    plt.figure(figsize=(15, 8))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, color = 'Red', linewidth=1)

    plt.show()

    keep_running = input('Run another plot? (y/n): ')
    if keep_running != 'y':
        break

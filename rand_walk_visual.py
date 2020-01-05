import matplotlib.pyplot as plt
from random_walk import RandomWalk

# run the random walk and plot the points while the program is active

while True:
    # make a random walk
    rw = RandomWalk(500000)
    rw.fill_walk()

    # Set the size of the plot window to fit the walk side to side
    plt.figure(figsize=(10, 8))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens,
                edgecolor='none', s=1)  # create a scatterplot of the random walk

    # show the first and last point in a different color
    plt.scatter(0, 0, c="green", edgecolors='none', s=75)
    plt.scatter(rw.x_values[-1], rw.y_values[-1],
                c="red", edgecolors='none', s=75)

    # remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another? (y/n): ")
    if keep_running != 'y':
        break

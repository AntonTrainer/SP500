from die import Die
import pygal

die = Die()  # create a die using the Die Class

# try to make it take an imputted number of rolls
#number_rolls = int(input("How many rolls would you like (must be a number)? "))

# ------------------ Roll die and update the result list for each roll ------------------
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# ------------------ Result Analysis ------------------
frequencies = []

# recall that the list will start at 0 so we have to push it up one
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# ------------------ Visualize the results ------------------
hist = pygal.Bar() # Bar graph created with pygal

hist.title = "Results of rolling 6 sided die 1000 times"
hist.x_labels = list(range(1, die.num_sides+1))
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('one_D6_visual.svg')
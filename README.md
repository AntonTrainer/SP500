# Practice
## small practice scripts doing all kinds of random things


*sp500.py* downloads and graphs SP500 data using pandas_datareader.get_data_yahoo

*rw_practice.py* generates a random walk using a line plot theoretically could simulate molecular motion

*rand_walk_visual.py* produces gradient random walk displays using a scatter plow with the start/end points in green/red 
    *random_walk.py* is a module that builds the random walk that *rand_walk_visual.py* displays

*die.py* creates a a 6 sided die with a class  
*die_visual.py* calls Die from *die.py* and generates a list of frequencies of the results of 1000 rolls and graphs them in a .svg file   
   *one_D6_visual.svg* is the histogram that is created in *die_visual.py* 

*multi_die_visul.py* same as *die.py* but rolls 2 dice and adds their scores and outputs a histogram in *two_D6_visual.svg* as you can see, the histogram of one million rolls is a nearly perfect normal distribution with a median of about 7


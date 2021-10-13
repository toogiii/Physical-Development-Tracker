r"""
Filename: PDTAlpha.py
File Path on Garv's Computer: <C:\Users\garv.gaur\GHP\PDTAlpha.py>
Author: Garv Gaur
Last Modified: 7/12/2020 6:18 PM

###################
###################
###################

This program is not for reproduction or distribution.

###################
###################
###################

This program, the Physical Development Tracker, is a way to track someone's 
physical development and to set reasonable goals for them based on the 
sigmoidal curve of development. There is some research that has shown that
safe physical development happens in the shape of a sigmoidal curve. This 
program takes that sigmoidal curve and fits it to the user's data, as well as 
the expected data taken from the archetypal sigmoidal curve of development,
so as to keep a steady rate of progress going which is tailored to the user
while mitigating risk of injury from too rapid a rate of attempted development. 

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3177954/

This paper describes that the "dose-response curve in gene induction obeys a 
sigmoidal curve," and it says that the correlation between potency and maximum 
activity describe "the expression of the regulated gene in response to ligand 
concentration." This correlation manifests itself in a sigmoid curve. Since 
many developmental activities take place due to ligand-protein interactions, we 
can infer that these developmental activities will follow the same sigmoidal 
curve. However, these curves can vary. So, this curve-fitting algorithm 
(sigmoidal/logistic regression implementation) will serve to account for these 
sigmoid inconsistencies and correct them as data comes in. 
"""

# Librariez

# Matlab Plotting Library for plotting graphs

import matplotlib.pyplot as plt

# NumPy for advanced mathematical uses

import numpy as np

# Scipy.optimize.curve_fit for the least squares regression optimization

from scipy import optimize

# Math for some mathematical operations

import math as m

# Fraction class for easy conversion of numerator, denominator to decimal in exact form

from fractions import Fraction

# Storages for Predicted Curve points

x = []
y = [1, 25, 96]

# Storages for points for x and y for the scatterplot - additional points will be added by the user.

xdata = []
ydata = []

# Original Curve:

def sigmoidalcurve(x, b, x0, y0):
    return 101 * (np.exp(np.float64(b * x - x0)) / (1 + np.exp(np.float64(b * x - x0)))) + y0

# Grab the x value at y = 100:

def ymax(b, x0, y0):
    
    # Storage for result
    
    res = 0
    f = 0
    
    # For every whole x value until it is found
    
    while True:
        f += 1
        try:
            
            # If this works then the number is where y ~ 100
            
            res = ((m.log((100 - f) / (101 - (100 - f))) + x0) / b) - y0
            break
        except:
            continue
    return res

# 1st iteration shown

def arch_curve(x):
    sigmoidal = plt.figure(1)
    
    # The sigmoidal curve represents every kind of physical development for all ages. 
    # We will factor developmental speed in later. 
    # We use 100 + 1 to show that we don't desire an asymptote at 100, but we do want to use 100 as a sort of max for this graph as 100%.
    
    plt.plot(x, sigmoidalcurve(x, 1 / 10, 5.4, 0))
    
    # Labeling and graphing
    
    plt.title(label = "Archetypal Physical Development Curve", loc = "center")
    plt.xlabel("Time (in percent)")
    plt.ylabel("Percentage of goal")
    plt.show(sigmoidal)

# Finding the closest number in an array

def closest(lst, K):
    
    # NumPy Array
    
    lst = np.asarray(lst) 
    
    # Index of the minimum of the distance of each each number away from K
    
    idx = (np.abs(lst - K)).argmin() 
    return idx

# Grab the x values from any function

def getnums():
    
    # Existing graph scrubbed for x values and y values with an increment of 2 * 10^-8
    
    line = plt.gca().get_lines()
    
    # X values from graph
    
    x_data = line[0].get_data()[0]
    
    # Y values from graph
    
    y_data = line[0].get_data()[1]
    
    # For all expected y values
    
    for i in range(len(y)):
        
        # Find the closest y value's index in the y_data array 
        
        index = closest(y_data, y[i])
        
        # Use that index to find the closest x value and add it to the array of expected x values
        
        x.append(x_data[index])
    return x

# This adds the point to the scatterplot in progress

def add_pt_to_scatter(datapt):
    
    # Get Point
    
    for i in range(len(datapt)):
        
        # Process datapoint
        
        datapt[i] = datapt[i].replace(")", "")
        datapt[i] = datapt[i].replace("(", "")
        datapt[i] = int(datapt[i])
        
        # If it is the first piece, add it to the xdata
        
        if i == 0:
            xdata.insert(1, datapt[i])
            
        # Otherwise add it to the ydata    
            
        else:
            ydata.insert(1, datapt[i])

# Once again, we plot the scatterplot
      
def scattergraph(xvals, yvals, label, color):
    plt.scatter(xvals, yvals, label = label, color = color)
    plt.show()

# Now, we compile the data, graph it, and figure out the curve of best fit.

def scat_pred(p0):
    
    # Create a new figure
    
    plt.figure()
    
    # Consolidate expected/observed data into 1 list for x and 1 list for y data
    
    for i in range(len(y)):
        xdata.append(int(x[i]))
        ydata.append(int(y[i]))
    
    # Add Observed Data to the scatterplot with the curve
    
    scattergraph(xdata[:len(xdata) - len(x)], ydata[:len(ydata) - len(y)], "Data Input", "orange")
    
    # Add Expected Data to the scatterplot with the curve
    
    scattergraph(xdata[len(xdata) - len(x):], ydata[len(ydata) - len(y):], "Expected Data", "blue")
    
    # Get parameters for function from the optimize.curve_fit(function, x, y, guess at parameters) command
    # Parcov is irrelevant for our purposes, we just need it so that the function 
    # doesn't return an error and the separation of the two (par and parcov) is painless
    
    par, parcov = optimize.curve_fit(sigmoidalcurve, xdata, ydata, p0=p0)
    
    # Figure out the x where the graph's y = 100, AKA where the user's goal is expected to be reached
    
    hundred = ymax(Fraction(par[0]), Fraction(par[1]), Fraction(par[2]))
    
    # Graph the curve with the new parameters from the curvefitting function
    
    s = np.arange(0., hundred, 0.02)
    plt.plot(s, sigmoidalcurve(s, Fraction(par[0]), Fraction(par[1]), Fraction(par[2])), label = "Curve of Best Fit", color = "red")
    plt.xlabel("Time (in percent)")
    plt.ylabel("Percentage of goal")    
    plt.legend()
    
    # Delete expected data from compiled arrays
    
    del xdata[len(xdata) - 3:]
    del ydata[len(ydata) - 3:]
    
    # Delete x data from expected array for regeneration in the next iteration
    
    del x[0:len(x)]
    
    # Return the parameters in order to provide a guess for the next iteration (anchoring)
    # Return the percentage of time that was originally expected for the user to reach their goal for the user's knowledge
    
    return par, hundred

# Here, we plot the data and grab the numerical data from the function.

# Archetypal Curve

s = np.arange(0., 100., 0.02)
arch_curve(s)

# We need these pars to use as p0 for the first iteration of the curve (they come from the default curve)

pars = [1/10, 5.4, 0]

# The user's goal and time

goal = input("What is your goal at 100%?\n")
time = int(input("How many days do you think it will take you?\n"))

# Easier to create an infinite loop because we need to check if the user reached their goal right after datapoints have been collected and before everything else

while True:
    
    # Datapoint collection
    
    datapt = input("Please input your datapoint in this format: percentage of time elapsed, percentage of goal reached \n").split(",")
    
    # If the goal has been completed, then exit the loop
    
    check_num = int(datapt[1])
    if check_num >= 100:
        break
    
    # Otherwise, add the point to the scatterplot and the data array
    
    add_pt_to_scatter(datapt)
    
    # Grab the estimated points from the previous graph
    
    x = getnums()
    
    # Convert it to integers

    x = [int(i) for i in x]

    # Collect previous parameters as a guess and store the percentage of time it is anticipated that you will reach the goal in

    pars, end = scat_pred(pars)
    end = round(end)
    
    # Output this data to the user
    
    print("You will reach your goal in an estimated " + str(end) + " percent of the time originally anticipated, which was " + str(time) + ". It will take approximately an estimated " + str(end * 0.01 * time) + ". Your goal is " + goal + ".")
print("You reached your goal!")
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize
import math as m
from fractions import Fraction

# Original Curve:

def sigmoidalcurve(x, b, x0):
    return 101 * (np.exp(np.float64(b * x - x0)) / (1 + np.exp(np.float64(b * x - x0))))

# Grab the x value at y = 100:

def ymax(b, x0):
    res = 0
    for i in range(100):
        try:
            res = (m.log((100 - i) / (101 - (100 - i))) + x0) / b
            break
        except:
            continue
    return res

# 1st iteration shown

def arch_curve(x):
    sigmoidal = plt.figure(1)
    
    # The sigmoidal curve represents every kind of physical development for all ages. We will factor developmental speed in later. We use 100 + 1 to show that we don't desire an asymptote at 100, but we do want to use 100 as a sort of max for this graph as 100%.
    
    plt.plot(x, sigmoidalcurve(x, 1 / 10, 5))
    plt.title(label = "Archetypal Physical Development Curve", loc = "center")
    plt.xlabel("Time (in percent)")
    plt.ylabel("Percentage of goal")
    plt.show(sigmoidal)


# Grab the y values from any function

def getnums():
    line = plt.gca().get_lines()
    x_data = line[0].get_data()[0]
    y_data = line[0].get_data()[1]
    for i in range(len(x)):
        index = np.where(x_data == float(x[i]))
        y.append(y_data[index])
    return y

# This adds the point to the scatterplot in progress

def add_pt_to_scatter(datapt):
    
    # Get Point
    
    for i in range(len(datapt)):
        datapt[i] = datapt[i].replace(")", "")
        datapt[i] = datapt[i].replace("(", "")
        datapt[i] = int(datapt[i])
        if (i + 2) % 2 == 0:
            xdata.insert(1, datapt[i])
        else:
            ydata.insert(1, datapt[i])

# Once again, we plot the scatterplot
      
def scattergraph(xvals, yvals, label, color): 
    plt.scatter(xvals, yvals, label = label, color = color)
    plt.show()

# Now, we compile the data, graph it, and figure out the curve of best fit.

def scat_pred():
    plt.figure()
    for i in range(len(x)):
        xdata.append(int(x[i]))
        ydata.append(int(y[i]))
    scattergraph(xdata[:len(xdata) - len(x)], ydata[:len(ydata) - len(y)], "Data Input", "orange")
    scattergraph(xdata[len(xdata) - len(x):], ydata[len(ydata) - len(y):], "Expected Data", "blue")
    par, parcov = optimize.curve_fit(sigmoidalcurve, xdata, ydata)
    hundred = ymax(Fraction(par[0]), Fraction(par[1]))
    s = np.arange(0., hundred, 0.02)
    plt.plot(s, sigmoidalcurve(s, Fraction(par[0]), Fraction(par[1])), label = "Curve of Best Fit", color = "red")
    plt.xlabel("Time (in percent)")
    plt.ylabel("Percentage of goal")    
    plt.legend()
    del xdata[len(xdata) - 10:]
    del ydata[len(ydata) - 10:]
    del y[0:len(y)]
    return hundred
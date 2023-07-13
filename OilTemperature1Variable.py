import matplotlib.pyplot as plt
import numpy as np

#  Below I define a bunch of variables
######################################################################################################################

t = 5
q = 0 # initial value for heat released
mC = 100 #specific heat capacity of water 2 j/g/c * 50 grams of water = mc
tP = 80 #temperature of pipe
tI = 10 # initial temperature of water
k1 = (2*3.14159*0.0017*2)/(np.log(0.16/0.08)) #constant = (2pikL)/(ln(r0/ri))
tempGradient = tP - 25 #temp gradient from reference point of water is the difference between the pipe temp and wter temp
#print(k1*tempGradient) #k1*tempGradient is equal to dQ/dt
x = np.arange(0, 10000, t) # set x values and bounds
y = [] # create a list for the y axis plot

# the expression (k1*tempGradient) is equal to the derivative of Q / dQ/dt / Q'(t)

########################################################################################################################

# Here the main calculation is performed. For each x value, a corresponding rate of heat exchange is calculated.
# The rate of heat exchange is accummalated into a reimmann sum integral, and said integral is used to calculate the next 
# rate of heat exchange and subsequently the next addition to the reimmann sum. 

for i in range (len(x)):
    tW = tI + q/mC # finds the current temperature of the water by adding (initaial temp + heat transfer induced change in temp)
    tempGradient = tP - tW # uses the new temp, tw, in the temperature gradient function (temp pipe - temp water)
    q = q + k1*tempGradient*t # finds Q'(t), k1*tempGradient, and multiplies Q' by time interval t. --
                                     #-- then sums all Q' to find the reimmann sum
    y.append(tI + q/mC) # adds the current value of Q(t) to the list of y axis plot points
    print(tI + q/mC)

########################################################################################################################
  
# Below the values are plotted

# plot the points 
plt.plot(x, y)
  
# name the x axis
plt.xlabel('time (seconds)')
# name the y axis
plt.ylabel('heat (joules)')
  
# title the graph
plt.title('Approximation of Heat Transfer')
  
# show the plot
plt.show()
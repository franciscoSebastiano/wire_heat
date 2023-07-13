import matplotlib.pyplot as plt
import numpy as np

#       Below I define a bunch of variables
######################################################################################################################

t = 5 # time interval width of the reimmann sum
eQ = 1.1 # heating rate from electric energy = 10 watts = 10 joules/sec
q = 0 # initial value for heat released
mC = 100 #specific heat capacity of water 4.2 j/g/c * 100grams of water = mc
mC2 = 3 # specific heat of copper wire 1 j/g/c * 10grams of wire = mc
k1 = (2*3.14159*.002*5)/(np.log(1/0.5)) #constant = (2pikL)/(ln(r0/ri))
tempGradient = 0  #temp gradient  = 0 because the water and pipe start at same temp.
tI = 10

# the expression (k1*tempGradient) is equal to the derivative of Q / dQ/dt / Q'(t)

########################################################################################################################

# Here I set up my arrays for the ordered pair (x,y)

x = np.arange(0, 7500, t) # set x values and bounds by creating a list of values from 1 to 1000 with interval step t
y = [] # create a list for the y axis plot

########################################################################################################################

# Here the main calculation is performed. For each x value, a corresponding rate of heat exchange is calculated.
# The rate of heat exchange is accummalated into a reimmann sum integral, and said integral is used to calculate the next 
# rate of heat exchange and subsequently the next addition to the reimmann sum. 

for i in range (len(x)):
    tempGradient = (eQ*i*t)/mC2 - (q/mC2) - (q/mC) # the difference in energy is equal to (electrical energy in) - (electrical energy out).--
                                               #-- Similarly, the difference in temperature is (energy in/mc) - (energy out/mc)
    q = q + k1*tempGradient*t # this calculates the accumalation of energy as a reimmann sum with Q'(t)* t seconds
    y.append(q/mC) # this plots the current accummalated energy in the water to the y-axis.
    #print(tempGradient)
    print(tI+q/mC)

    tP = (eQ*i*t)/mC2 - q/mC2 # this is an expression for the temperature of the pipe. It's not used in the primary calculation, but It's useful for checking program functionality.
    tW = q/mC # this is an expression for the temperature of the temperature of the water. It's not used in the primary calculation either.

##########################################################################################################################

# Below the values are plotted

print(tP*mC2)
print(tW*mC)
#print(q)

  
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
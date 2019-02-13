# =============================================================================
# UserID: ChartreuseRabbit
# Date: 4/20/18
# Challenge: 5
# 
# Sources:
#         
#         Title: How to return dictionary keys as a list in Python?
#         URL: https://stackoverflow.com/questions/16819222/how-to-return-dictionary-keys-as-a-list-in-python/16819250#16819250
#         
#         Title: numpy.absolute
#         URL: https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.absolute.html
# =============================================================================

# imports======================================================================
from __future__ import division
import numpy
import matplotlib.pyplot as mplot
# =============================================================================


# variables=====================================================================
data = None #data read from signals.csv
transmissions = {} #dictionary where the signal is the key and a list of transmissions with that signal are the values
scatterColors = ["black","orange","green","brown","purple"] #used for the 5 different scatter plots
# =============================================================================


# reads signals.csv and saves it into data=====================================
data = open("signals.csv", "r")
data = data.read()
data = data.split("\n")

while (data[-1] == ""):
    data.pop()
# =============================================================================
   
#loops through data    
for i in range(0, len(data)):
    
    #splits each string of data on commmas
    data[i] = data[i].split(",")
    
    
    #checks if the list at the given key value has been initilized
    if (not transmissions.has_key(data[i][1])):
        transmissions[data[i][1]] = []
            
    #appends the list given at the specified signal with the time and intensity
    transmissions[data[i][1]].append([numpy.float32(data[i][0]),numpy.float32(data[i][2])])
    
    #loops through transmissions
for i in transmissions.keys():
    
    xVals = [] #values for the x-axis of the given transmission (the time)
    yVals = [] #values for the y-axis of the given transmission (the intensity)
    correlation = None #correlation coefficient for xVals and yVals
    
    #loops through each element in the list at the specified transmission key
    for j in range(0,len(transmissions[i])):
        
        #adds transmission time and intensity to xVals and yVals respectively
        xVals.append(transmissions[i][j][0])
        yVals.append(transmissions[i][j][1])

    #plots the scatter plots for all transmissions
    mplot.scatter(xVals,yVals,color=scatterColors.pop())
    
    #if the absolute value of the correlation coefficient is greater than .5
    correlation = numpy.corrcoef(xVals,yVals)[1][0]
    if(numpy.absolute(correlation) > 0.5):
        
        xLine = range(0,101) #list of values 0-100
        yLine = [] #linear regression y values
        
        slope = numpy.corrcoef(xVals,yVals)[1][0] * numpy.std(yVals) / numpy.std(xVals) #slope for linear regression
        intercept = numpy.mean(yVals) - slope * numpy.mean(xVals) #intercept for linear regression
        
        #loop that adds the y values for each point into the yLine list
        for k in xLine:
            yLine.append(slope * k + intercept)
        
        #plots the linear regression line
        mplot.plot(xLine,yLine,color="red")
        
        
# code for plotting the polynomial regression curve============================
        if (numpy.absolute(correlation) > 0.95):
            polyParams = numpy.polyfit(xVals,yVals,2)
            predictedY = numpy.polyval(polyParams,xLine)
            mplot.plot(xLine,predictedY,color="blue")
        else:
            polyParams = numpy.polyfit(xVals,yVals,3)
            predictedY = numpy.polyval(polyParams,xLine)
            mplot.plot(xLine,predictedY,color="blue")
# =============================================================================
            

# details for the entire graph=================================================
mplot.title("Challenge 5")
mplot.xlabel("Time(ms)")
mplot.ylabel("Signal Intensity")
mplot.show
# =============================================================================

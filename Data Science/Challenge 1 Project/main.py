# =============================================================================
# UserID: ChartreuseRabbit
# Date: 2/6/18
# Challenge: 1
# 
# Sources:
#     
#    Title: Python - Dictionary
#    URL: https://www.tutorialspoint.com/python/python_dictionary.htm
#    
#    Title: Python - Lists
#    URL: https://www.tutorialspoint.com/python/python_lists.htm
# =============================================================================


#imports
from __future__ import division
import matplotlib.pyplot as mplot


#Declaring lists and dictionaries
xScatter = []
yScatter = []
xLine = []
yLine = []
signalsList = []
keyIndex = []
signalsDict = {}

#opening file, reading it, and splitting on new line
data = open("transmissionData.csv", "r")
data = data.read()
data = data.split("\n")

#removes the last empty line if there is one
if (data[-1] == ""):
    data.pop()

#fills x and y vals for scatter plot, and fills signalsList
for i in range(0,len(data)):
        
    line = data[i].split(",")        
    
    if(float(line[2]) == 31.071373):
        
        xScatter.append(float(line[0]))
        yScatter.append(float(line[1]))
        
        signalsList.append(line)

#Fills SignalsDict: keys are the time, values are lists of amplitudes
for i in range(0,len(signalsList)):
    
    if(not signalsDict.has_key(signalsList[i][0])):
        signalsDict[signalsList[i][0]] = []
        keyIndex.append(signalsList[i][0])
         
    signalsDict[signalsList[i][0]].append(signalsList[i][1])
    
#averages amplitudes for each time unit, and fills x and y vals for line plot
for i in range(0,len(signalsDict)):
    
    total = 0
    count = 0
    
    for j in range(0,len(signalsDict[keyIndex[i]])):
        total += float(signalsDict[keyIndex[i]][j])
        count += 1
    
    yLine.append(total/count)
    xLine.append(float(keyIndex[i]))
    
#creates the scatter and line plot
mplot.xlabel("Transmission Time (Milliseconds)")
mplot.ylabel("Amplitude")
mplot.title("Transmission Time and Amplitude of Signals from the Working Relay")
mplot.scatter(xScatter, yScatter, color="red")
mplot.plot(xLine, yLine, color = "blue")
mplot.show
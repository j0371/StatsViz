# =============================================================================
# UserID: ChartreuseRabbit
# Date: 3/29/18
# Challenge: 4
# 
# Sources:  
# =============================================================================

#Imports
from __future__ import division
import matplotlib.pyplot as mplot
import numpy

#Variables
outline = None #data for the outline of the US
dataRaw= None  #unaltered data from data.csv
kVal = 0       #K Value that the user specifies
xOutline = []  #x Values for the outline
yOutline = []  #y Values for the outline
xScatter = []  #x Values for the reconstructed data
yScatter = []  #y Values for the reconctructed data
vVals = []     #color values for the recontructed data

#gets user input for k value
kVal = numpy.int32(raw_input("Enter your K Value: "))

#===Creates US Outline==================================
outline = open("us_outline.csv", "r")
outline = outline.read()
outline = outline.split("\n")

for i in range(0, len(outline)):
   outline[i] = outline[i].split(",")

while (outline[-1] == ""):
    outline.pop()

for i in range(0,len(outline)):
    xOutline.append(numpy.float32(outline[i][0]))
    yOutline.append(numpy.float32(outline[i][1]))
    
#mplot.plot(xOutline,yOutline, color = "black")
#=======================================================

#===Reads in the data from data.csv and stores it into dataRaw===
dataRaw = open("data.csv", "r")
dataRaw = dataRaw.read()
dataRaw = dataRaw.split("\n")

for i in range(0, len(dataRaw)):
   dataRaw[i] = dataRaw[i].split(",")

while (dataRaw[-1] == ""):
    dataRaw.pop()
#===============================================================
    
    #code for constructing the k-value approximations for each grid point
for i in range(0,121):
    for j in range(0,195):
        
        distances = [] # list of distance lists
        average = 0 #average of all of the kth terms of the sorted distances color values
        
        #fills the distances list
        for k in range (0,len(dataRaw)):
            distance = [] #[Distance from this grid point to raw data point, Color value of raw data point]
            distance.append(numpy.sqrt(numpy.power(numpy.float32(dataRaw[k][0])-j,2)+numpy.power(numpy.float32(dataRaw[k][1])-i,2)))
            distance.append(numpy.float32(dataRaw[k][2]))
            
            distances.append(distance)
            
        #Sorts distances and slices it at the kth index
        distances=sorted(distances, key=lambda val:val[0])
        distances=distances[0:kVal]
        
        #averages all the color values in the sliced distances list
        for k in range(0,len(distances)):
            average += distances[k][1]
        average /= len(distances)
        
        
        #Fills the parameters for the reconstructed data
        xScatter.append(j)
        yScatter.append(i)
        vVals.append(average)
            
#creates the plot for the reconstructed data and shows the graph
mplot.scatter(xScatter,yScatter, c=vVals, cmap="gist_ncar")
mplot.axis("off")
mplot.show

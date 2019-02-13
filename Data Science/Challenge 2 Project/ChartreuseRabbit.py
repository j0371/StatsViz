# =============================================================================
# UserID: ChartreuseRabbit
# Date: 2/19/18
# Challenge: 2
# 
# Sources:
#     
#     Title: Replace all non-alphanumeric characters in a string
#       URL: https://stackoverflow.com/questions/12985456/replace-all-non-alphanumeric-characters-in-a-string
#     
#     Title: Python 2.7 getting user input and manipulating as string without quotations
#       URL: https://stackoverflow.com/questions/4960208/python-2-7-getting-user-input-and-manipulating-as-string-without-quotations
# 
#     Title: Doing math to a list in python
#       URL: https://stackoverflow.com/questions/6645357/doing-math-to-a-list-in-python        
# =============================================================================

#imports
from __future__ import division
import matplotlib.pyplot as mplot
import re
import numpy

#Variables
seriesA = [] #all words in series A
seriesBG = [] #all words in series BG
lexicon = [] #list that holds each word and its sentiment in the lexicon
yAxis = [] # holds all the counts for each bin in the bar graph
xAxis = (range(0,5))
ticks = ["Neg", "W. Neg", "Neu" , "W. pos" , "Pos"]

lexDict = {} #lexicon dictionary where the word is the key and the sentiment val is the element

#counts for all the words in each sentiment range
neg = 0
negW = 0
neutral = 0
posW = 0
pos = 0

series = None #Used for the title to say if its series A or BG

#saves data from the sentiment lexicon csv into the lexicon list and splits on new line
lexicon = open("sentiment_lex.csv", "r")
lexicon = lexicon.read()
lexicon = lexicon.split("\n")

#removes empty strings at the end of the lexicon list
while (lexicon[-1] == ""):
    lexicon.pop()

#fills lexDict with data from lexicon
for i in range(0, len(lexicon)):
   lexicon[i] = lexicon[i].split(",")
   lexDict[lexicon[i][0]] = lexicon[i][1]

seriesPick = raw_input("Which series do you choose to display?(A or BG): ") #Input on which series to display

#Conditional Code for when series a is picked
if(seriesPick.lower() == "a"):
    
    series = "A" 
    
    #saves all series a text into the list seriesA
    for i in range(0, 22):
    
        seriesA.append(open("a" + str(i+101) + "script.txt", "r"))
        seriesA[i] = seriesA[i].read().lower()
        seriesA[i] = re.sub("[']+", "",seriesA[i])
        seriesA[i] = re.sub("[^0-9a-zA-Z]+", " ",seriesA[i])
        seriesA[i] = seriesA[i].split()

    #for each word in script a, determines which sentiment range it should go in
    for i in range(0, len(seriesA)):
        for j in range(0,len(seriesA[i])):
            if(lexDict.has_key(seriesA[i][j])):
            
                if(numpy.float32(lexDict[seriesA[i][j]]) < -0.6):
                    neg += 1
                elif((numpy.float32(lexDict[seriesA[i][j]]) >= -0.6) and (numpy.float32(lexDict[seriesA[i][j]]) < -0.2)):
                    negW += 1
                elif((numpy.float32(lexDict[seriesA[i][j]]) >= -0.2) and (numpy.float32(lexDict[seriesA[i][j]]) <= 0.2)):
                    neutral += 1
                elif((numpy.float32(lexDict[seriesA[i][j]]) > 0.2) and (numpy.float32(lexDict[seriesA[i][j]]) <= 0.6)):
                    posW += 1
                else:
                    pos += 1
            
#Conditional code for when series bg is picked  instead of series a   
elif(seriesPick.lower() == "bg" or seriesPick.lower() == "b"):
    
    series = "BG"
    
    #saves all series bg text into the list seriesBG
    for i in range(0, 13):
    
        seriesBG.append(open("bg" + str(i+101) + "script.txt", "r"))
        seriesBG[i] = seriesBG[i].read().lower()
        seriesBG[i] = re.sub("[']+", "",seriesBG[i])
        seriesBG[i] = re.sub("[^0-9a-zA-Z]+", " ",seriesBG[i])
        seriesBG[i] = seriesBG[i].split()
        
    #for each word in script bg, determines which sentiment range it should go in
    for i in range(0, len(seriesBG)):
        for j in range(0,len(seriesBG[i])):
            if(lexDict.has_key(seriesBG[i][j])):
            
                if(numpy.float32(lexDict[seriesBG[i][j]]) < -0.6):
                    neg += 1
                elif((numpy.float32(lexDict[seriesBG[i][j]]) >= -0.6) and (numpy.float32(lexDict[seriesBG[i][j]]) < -0.2)):
                    negW += 1
                elif((numpy.float32(lexDict[seriesBG[i][j]]) >= -0.2) and (numpy.float32(lexDict[seriesBG[i][j]]) <= 0.2)):
                    neutral += 1
                elif((numpy.float32(lexDict[seriesBG[i][j]]) > 0.2) and (numpy.float32(lexDict[seriesBG[i][j]]) <= 0.6)):
                    posW += 1
                else:
                    pos += 1
  
#else for invalid input given that neither series A or series BG is chosen       
else:
    print("Invalid Input")
    
yAxis =numpy.log10([neg,negW,neutral,posW,pos])

#Creates the graph
mplot.bar(xAxis, yAxis)
mplot.xticks(xAxis,ticks)
mplot.title("Sentiment Analysis for Series " + series)
mplot.ylabel("Log(10) Word Count")
mplot.xlabel("Sentiment")
mplot.show
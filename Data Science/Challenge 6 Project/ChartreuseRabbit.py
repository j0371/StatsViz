# =============================================================================
# UserID: ChartreuseRabbit
# Date: 5/2/2018
# Challenge: 6
# 
# Sources: 
#     
#         Title: Generate random integers between 0 and 9
#         URL: https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
#         
#         Title: Python - Functions
#         URL: https://www.tutorialspoint.com/python/python_functions.htm
#         
#         Title: Global and Local Variables in Python
#         URL: https://www.geeksforgeeks.org/global-local-variables-python/
#         
#         Title: How to check whether a file exists?
#         URL: https://stackoverflow.com/questions/82831/how-to-check-whether-a-file-exists?rq=1
#
#         Title: Getting user input from the keyboard
#         URL: http://www.pythonforbeginners.com/basics/getting-user-input-from-the-keyboard
# =============================================================================
    
#imports
from __future__ import division
import mazeGenerator as mg
import neuro
import os
import time

#function for giving the network test cases
def test(network):  
    
    testInput = mg.generate(10000) #generates test case mazes
    correct = 0 #number of mazes the network gets correct
    
    #loops for each generated maze
    for i in range(0,len(testInput)):
        
        mazeBool = mg.isMaze(testInput[i],0,[0]) #checks whether the maze is valid or not
        
        pred = neuro.predict(network,testInput[i]) #gives the network's prediction
        
        #rounds the prediction
        pred = round(pred)
        
        #if the networks prediction matches what the algorithm (isMaze) determined, correct is incremented
        if((mazeBool and pred == 1) or (not mazeBool and pred == 0)):
            correct+=1         
            
    #prints the percentage that the network got correct
    print "Percent the network got correct: ",correct/len(testInput)*100

#asks user to determine how many mazes to generate
mazeNum = input("How many mazes?: ")

#ask user to determine how many reps to do
reps = input("How many Reps?: ")

mazes = [] #holds all of the generated mazes
inputs = [] #holds the positions for each maze (excludes maze validity)
targets = [] #targets for the network
network = [] #variable for the network
    
start = time.time() #start time for determining how long the training took

#generates the specified number of mazes
mazes = mg.generate(mazeNum)

#appends inputs and targets with the appropriate information from mazes
for i in mazes:
    inputs.append(i[0:25])
    targets.append([i[-1]])

#if there's already a network saved, then it will load that, otherwise it will create a new one
if(os.path.isfile("neuroFile.net")):
    network = neuro.readNetworkFromFile("neuroFile.net")
else:
    network = neuro.setup_network(inputs)
    
#trains the network
neuro.train(network,inputs,targets,reps)

#writes the network to a file
neuro.writeNetworkToFile("neuroFile.net",network)

#prints the time taken to train the network
print "time taken to train: ",time.time() - start

#test(network)


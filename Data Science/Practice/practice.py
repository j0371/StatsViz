from __future__ import division
import random
import numpy

def main():
    
    samples = 4
    mazes = generate(samples)
    gridPrint(mazes[0])
    
    print "\n",isMaze(mazes[0])
            
        
            
    
        
        


#print function that gives a more intuitive view of what a given maze looks like
def gridPrint(maze):
    
    for i in range(0,5):
        print maze[0+5*i],maze[1+5*i],maze[2+5*i],maze[3+5*i],maze[4+5*i]
        
def isMaze (maze,position,prevPositions):
    
    #prevPoistions keeps up with where the algorithm has already been so it doesn't recurse infinitely
    prevPositions.append(position)
    
    rVal = False #boolean for if it's a valid maze
    usedPos = {"pos+1":False,"pos+5":False,"pos-1":False,"pos-5":False} #restricts certain movement options if that postion has been used
    
    #conditional code for movement restriction based on previously visited positions
    for i in range(0,len(prevPositions)):
        if(position+1 == prevPositions[i]):
            usedPos["pos+1"] = True
        if(position+5 == prevPositions[i]):
            usedPos["pos+5"] = True
        if(position-1 == prevPositions[i]):
            usedPos["pos-1"] = True
        if(position-5 == prevPositions[i]):
            usedPos["pos-5"] = True
    
    #this is only important for determining if the initial(top left most) position is a 0
    if(maze[position] == 0):
    
        #base case for when the algorithm has reached the end of the maze (if it's valid)
        if(position == 24):
            return True
        
        #recursive cases
        if((((position+1) % 5) != 0) and (not usedPos["pos+1"]) and (maze[position+1] == 0)):
           rVal = isMaze(maze,position+1,prevPositions)
           if(rVal == True):
               return rVal
        if((position+5 < 25) and (not usedPos["pos+5"]) and (maze[position+5] == 0)):
           rVal = isMaze(maze,position+5,prevPositions)
           if(rVal == True):
               return rVal
        if((position-1 > -1) and (((position-1) % 5) != 4) and (not usedPos["pos-1"]) and (maze[position-1] == 0)):
            rVal = isMaze(maze,position-1,prevPositions)
            if(rVal == True):
               return rVal
        if((position-5 > -1) and (not usedPos["pos-5"]) and (maze[position-5] == 0)):
            rVal = isMaze(maze,position-5,prevPositions)
            if(rVal == True):
               return rVal
            
    return rVal

def generate(mazeNum):
    
    while(mazeNum % 4 != 0):
        mazeNum+=1
    
    nonmazes = []
    positionCount = [0] * 25
    
    while((len(nonmazes) < mazeNum)):
           
        maze = []
        mazeBool = None            
        
        for i in range(0,25):
        
            maze.append(float(random.randint(0,1)))

        
        mazeBool = (isMaze(maze,0,[]))        
        
        if((not mazeBool)):
            
            for i in range(0,25):
                if(maze[i] == 1):
                    positionCount[i]+=1
            
            maze.append(0.0)
            nonmazes.append(maze)
    
    return positionCount

main()
#Imports
from __future__ import division
import random

#Function to generate random mazes, generates as many mazes as it does nonmazes
def generate(mazeNum):
    
    #Makes sure the mazes can be split evenly
    while(mazeNum % 2 != 0):
        mazeNum+=1
    
    mazes = [] #contains all valid mazes, then is extended with nonmazes
    nonmazes = [] #contains all nonmazes
    
    #loop while mazes and nonmazes isnt full
    while((len(mazes) < mazeNum*.5) or (len(nonmazes) < mazeNum*.5)):
           
        maze = [] #contains all the data for the maze
        mazeBool = None #boolean for if the maze is valid or not         
        
        #loops for each position in the maze
        for i in range(0,25):
        
            #randomly picks a 1 or 0 for the given maze position
            maze.append(float(random.randint(0,1)))            
        
        #determines if the maze is valid or not
        mazeBool = (isMaze(maze,0,[]))        
        
        #conditional code for determining if it should be put in mazes or nonmazes
        if((mazeBool) and (len(mazes) < mazeNum*.5)):
            maze.append(1.0)
            mazes.append(maze)
        if((not mazeBool) and (len(nonmazes) < mazeNum*.5)):
            maze.append(0.0)
            nonmazes.append(maze)      
        
    #extends mazes with all the nonmazes aswell
    mazes.extend(nonmazes)
    
    return mazes


# ==========Failed attempt at improving the maze generator===================================================================
# def generateTricky(mazeNum):
#   
#     while(mazeNum % 4 != 0):
#         mazeNum+=1
#     
#     mazes = []
#     nonmazes = []
#     nonmazesT = []
#     
#     while((len(mazes) < mazeNum*.5) or (len(nonmazes) < mazeNum*.25) or (len(nonmazesT) < mazeNum*.25)):
#            
#         maze = []
#         mazeBool = None            
#         
#         for i in range(0,25):
#         
#             maze.append(float(random.randint(0,1)))            
#         
#         mazeBool = (isMaze(maze,0,[]))  
#         
#         if((mazeBool) and (len(mazes) < mazeNum*.5)):
#             maze.append(1.0)
#             mazes.append(maze)
#             
#             
#             
#         elif(mazeBool and (len(nonmazesT) < mazeNum*.25)):
#             
#             while(isMaze(maze,0,[])):
#                
#                 randPos = random.randint(0,24)
#                
#                 if(maze[randPos] == 0.0):
#                     maze[randPos] = 1.0
#                    
#             maze.append(0.0)
#             nonmazesT.append(maze)
#             
#             
#             
#         elif((not mazeBool) and (len(nonmazes) < mazeNum*.25)):
#             maze.append(0.0)
#             nonmazes.append(maze)
#             
#             
#         
#     mazes.extend(nonmazes)
#     mazes.extend(nonmazesT)
#     
#     return mazes
# =============================================================================

#print function that gives a more intuitive view of what a given maze looks like
def gridPrint(maze):
    for i in range(0,5):
        print(int(maze[0+5*i]),int(maze[1+5*i]),int(maze[2+5*i]),int(maze[3+5*i]),int(maze[4+5*i]))
    print "\n"
   
#Recursive function that determines whether or not the maze is a valid maze  
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
    
# =============================================================================
# mazes = generate(20)
# for i in mazes:
#     gridPrint(i)
#     print i[-1],"\n\n"
# =============================================================================

    
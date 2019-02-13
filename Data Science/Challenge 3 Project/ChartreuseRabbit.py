# =============================================================================
# UserID: ChartreuseRabbit
# Date: 2/27/18
# Challenge: 3
# 
# Sources:
#     
#     Title: How to check whether a file exists?
#       URL: https://stackoverflow.com/questions/82831/how-to-check-whether-a-file-exists?rq=1
#     
#     Title: Python - Basic Operators
#       URL: https://www.tutorialspoint.com/python/python_basic_operators.htm      
# =============================================================================

#imports
from __future__ import division
from PIL import Image
import numpy
import matplotlib.pyplot as mplot

#Variables
imgs = []
avgImg = []
stdDevImg = []

threshold = None

#gets user input for the threshold value
threshold = raw_input("Enter your change threshold: ")

#convert threshold to float32 as long as it's numerical
try:
    threshold = numpy.float32(threshold)

    #if the threshold value is valid
    if(0 <= threshold <= 255):
        
        #turns threshold into a list so it can check if any of the 3 rgb values are > threshold
        threshold = [threshold,threshold,threshold]
        
        #Loads image data and saves each image in the imgs list
        for i in range(0,200):     
            try:
                imgs.append(Image.open("rebelmrkt_" + str(i) + ".jpg")) 
            except:
                continue
            
        #converts images into float32 values
        for i in range(0,len(imgs)):
            imgs[i]=numpy.float32(imgs[i])
        
        #calulates average image
        avgImg = imgs[0]
        for i in range(1,len(imgs)):
            avgImg += imgs[i]
        avgImg /= len(imgs)
        
        #calculates standard deviation image
        stdDevImg = (imgs[0] - avgImg)**2
        for i in range(1,len(imgs)):
            stdDevImg += (imgs[i] - avgImg)**2
        stdDevImg = numpy.sqrt(stdDevImg / (len(imgs)-1))
        
        #for each pixel in avgImg, if the stdDevImg pixel is more than the threshold, it will make the pixel red
        for i in range(0, len(avgImg)):
            for j in range(0, len(avgImg[i])):
                
                if( stdDevImg[i][j] > threshold).any():
                    avgImg[i][j] = [255, 0, 0]
                else:
                    continue
                
        #clips avgImg and turns it into an unsigned 8 bit integer
        avgImg = numpy.clip(avgImg, 0, 255)
        avgImg = numpy.uint8(avgImg)
        
        #shows avgImg
        mplot.imshow(avgImg)
        mplot.show()
      
    #if threshold is not between 0 and 255
    else:
        print("Invalid input")

#if threshold is not numerical        
except:
    print("invalid input")
from __future__ import division
import random
import numpy

def main():
    
    samples = 10000000
    
    amounts = genWithBias(samples)
    
    print amounts,"\n"
    print "Mean: ",numpy.mean(amounts)
    print "Standard Deviation: ",numpy.std(amounts)
    print "Number of samples: ",samples
    
    
    
def genWithBias(genNum):
    
    onesCount = [0] * 5
    generated = 0
    
    while(generated < genNum):
           
        for i in range(0,5):
            
            weight = random.randint(0,7)
            
            if i in (0,4):
                
                counterWeight = random.randint(1,10000000)
                
                if(weight == 7):
                   
                    if(counterWeight >= 1247801):
                        onesCount[i]+=1
                else:
                    if(counterWeight <= 1247801):
                        onesCount[i]+=1
                    
            if i in (1,3):
                if weight in (6,7):
                    onesCount[i]+=1                  
            if (i == 2):
                if weight in(4,5,6,7):
                    onesCount[i]+=1
                    
        generated+=1
            
    return onesCount
    
    
    
    
main()
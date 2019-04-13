from collections import defaultdict
from scipy import stats
import numpy as np

#gets the columns from the data that's specified by the input
def getColumns(*, data: [], xCol: int = None, yCol: int = None, groups: list = None):

    xs = [] #values in the specified x axis column
    ys = [] #values in the specified y axis column
    groupData = [] #list of columns used for grouping/categorization

#appends empty lists for each group
    if(groups != None):
        for i in range(0,len(groups)):
            groupData.append([])
    
#appends all the x and y data to xs and ys and groupData
    for i in range(0, len(data)):
        if(xCol != None):
            xs.append(data[i][xCol])
        if(yCol != None):
            ys.append(data[i][yCol])

        if(groups != None):
            for j in range(0, len(groups)):
                groupData[j].append(data[i][groups[j]])

#if there is no x axis (eg when using interval plot) and if there is no groupData
#There values will be set to None
    if(xCol == None):
        xs = None
    if(yCol == None):
        ys = None
    if(groups == None):
        groupData = None

    return (xs, ys, groupData)

#function that removes the first row of the csv, and returns there values as a list
def popLabels(*, data: []):
    return data.pop(0)

#function that calculates the necessary intervals as well as the mean for the interval plot
def getIntervals(*, type: str, ys: list, groups: list = None):

    calculatedData = {} #dict with all categories concatenated as key, and (+interval,mean,-interval) as value

#if there was at least one column specified for grouping
    if groups != None:
        groupConcat = []
        groupVals = defaultdict(list)
        
#creates key values for calculatedData
        for i in range(len(groups[0])):
            string = []
            for j in range(len(groups)):
                if(j != len(groups)-1):
                    string.append(str(groups[j][i])+"\n")
                else:
                    string.append(str(groups[j][i]))

            groupConcat.append("".join(string))

        groupSet = list(set(groupConcat)) #the set of all key combos that appear in the data

#calculates the values for each key in calculatedData
        for i in range(len(groupSet)):
            for j in range(len(ys)):
                if groupConcat[j] == groupSet[i]:
                    groupVals[groupSet[i]].append(ys[j])

            mean = np.mean(groupVals[groupSet[i]])
            interval = 0

        #determines what interval to calculate based on the type of interval specified
        #there must be more than one value at the group column combo for there to be an interval
            if len(groupVals[groupSet[i]]) > 1:
                if type == "se":  
                    interval = stats.sem(groupVals[groupSet[i]])
                elif type == "sd":
                    interval = np.std(groupVals[groupSet[i]])
                elif type == "ci":
                    interval = stats.sem(groupVals[groupSet[i]]) * stats.t.ppf((1.95) / 2, len(groupVals[groupSet[i]])-1)
                calculatedData[groupSet[i]] = (mean+interval, mean, mean-interval)
            else:
                calculatedData[groupSet[i]] = (None, mean, None)

#when there is no category specified for the interval plot (there will just be one mean and interval plotted)
    else:
        mean = np.mean(ys)
        interval = 0

        #determines what interval to calculate based on the type of interval specified
        #there must be more than one value at the group column combo for there to be an interval
        if len(ys) > 1:
            if type == "se":  
                interval = stats.sem(ys)
            elif type == "sd":
                interval = np.std(ys)
            elif type == "ci":
                interval = stats.sem(ys) * stats.t.ppf((1.95) / 2, len(ys)-1)
            calculatedData["interval"] = (mean+interval, mean, mean-interval)
        else:
            calculatedData["interval"] = (None, mean, None)

    return calculatedData
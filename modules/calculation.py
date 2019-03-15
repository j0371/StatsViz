from collections import defaultdict
from scipy import stats
import numpy as np

def getColumns(*, data: [], xCol: int = None, yCol: int, groups: list = None):

    xs = []
    ys = []
    groupData = []

    if(groups != None):
        for i in range(0,len(groups)):
            groupData.append([])
    
    for i in range(0, len(data)):
        if(xCol != None):
            xs.append(data[i][xCol])
        ys.append(data[i][yCol])

        if(groups != [-1]):
            for j in range(0, len(groups)):
                groupData[j].append(data[i][groups[j]])

    if(xCol == None):
        return (None, ys, groupData)
    elif(groups != [-1]):
        return (xs, ys, groupData)
    else:
        return (xs, ys, None)



def popLabels(*, data: []):
    return data.pop(0)

def getIntervals(*, type: str, ys: list, groups: list):

    groupConcat = []
    groupVals = defaultdict(list)
    calculatedData = {}

    for i in range(len(groups[0])):
        string = []
        for j in range(len(groups)):
            if(j != len(groups)-1):
                string.append(str(groups[j][i])+",")
            else:
                string.append(str(groups[j][i]))

        groupConcat.append("".join(string))

    groupSet = list(set(groupConcat))

    for i in range(len(groupSet)):
        for j in range(len(ys)):
            if groupConcat[j] == groupSet[i]:
                groupVals[groupSet[i]].append(ys[j])

        mean = np.mean(groupVals[groupSet[i]])

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

    return calculatedData
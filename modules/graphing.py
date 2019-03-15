import matplotlib.pyplot as plt
import itertools
from collections import defaultdict

def graphScatter(*, xs: list, ys: list, groups: list = None, title: str = None,
                  xLabel: str = None, yLabel: str = None, gridLines: str = ""):
    
    if(groups != None):
        xPoints = defaultdict(list)
        yPoints = defaultdict(list)
        groupSet = list(set(groups[0]))

        for i in range(0,len(groups[0])):
            xPoints[groups[0][i]].append(xs[i])
            yPoints[groups[0][i]].append(ys[i])

        for i in range(0, len(groupSet)):
            plt.scatter(xPoints[groupSet[i]], yPoints[groupSet[i]], label=groupSet[i])
    else:
        plt.scatter(xs, ys)

    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)

    if(groups != None):
        plt.legend(loc="best")

    if len(gridLines)==1:
        plt.grid(which="major", axis=gridLines)
    elif gridLines == "xy":
        plt.grid(which="major", axis="both")

    plt.tight_layout()

    plt.show()

def graphInterval(*,data: dict, title: str = None, xLabel: str = None,
                  yLabel: str = None, gridLines: str = ""):

    xticks = []

    sortedData = sorted(data.items())
 
    for i in range(len(sortedData[0][0].split(","))):
        xticks.append([])
    
    for key, _ in sortedData:

        keyList = key.split(",")

        for i in range(len(keyList)):
            xticks[i].append(keyList[i])

    tickRange = 1

    for i in range(len(xticks)):
        xticks[i] = sorted(list(set(xticks[i])))

        tickRange *= len(xticks[i])

    allKeys = []

    for crossProduct in itertools.product(*xticks):

        key = ""
        for i in range(len(crossProduct)-1):
            key += crossProduct[i]+","
        key += crossProduct[-1]

        allKeys.append(key)

        labels = []

        for key in allKeys:
            labels.append(key.split(",")[-1])

        if key in data:

            if data[key][0] != None:
                plt.scatter(key, data[key][0], color="blue", marker="_")
            plt.scatter(key, data[key][1], color="blue", marker=".")
            if data[key][2] != None:
                plt.scatter(key, data[key][2], color="blue", marker="_")
            if data[key][0] != None and data[key][2] != None:
                plt.plot([key]*3, [data[key][0], data[key][1], data[key][2]], color="blue", linewidth=.85)

        else:
            plt.scatter(key, None)

    plt.xticks(labels=labels, ticks=(range(tickRange)))

    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel) 

    if len(gridLines)==1:
        plt.grid(which="major", axis=gridLines)
    elif gridLines == "xy":
        plt.grid(which="major", axis="both")

    plt.tight_layout()

    plt.show()

    
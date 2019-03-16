import matplotlib.pyplot as plt
import itertools
from collections import defaultdict

def graphScatter(*, xs: list, ys: list, groups: list = None, title: str = None,
                  xLabel: str = None, yLabel: str = None, gridLines: str = ""):

    _, _ = plt.subplots()
    
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

    _, ax = plt.subplots()

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

    # for i in range(len(xticks)-1):
    #     for j in range(len(xticks[i])):
    #         plt.text((j/len(xticks[i]))+(1/tickRange)+(25/540), -.1, xticks[i][j], horizontalalignment='center', transform=ax.transAxes)

    if len(xticks) == 2:
        for i in range(len(xticks[0])):
            xPlacement = (i/len(xticks[0]))+(1/tickRange)+(25/540)
            plt.text(xPlacement, -.1, xticks[0][i], horizontalalignment="center", transform=ax.transAxes) #-(.1+len(xticks)/100)
            #categoryPlacement(xticks, xPlacement, 1, ax)

    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel) 

    if len(gridLines)==1:
        plt.grid(which="major", axis=gridLines)
    elif gridLines == "xy":
        plt.grid(which="major", axis="both")

    #plt.tight_layout()

    plt.show()

# def categoryPlacement(categories, higherCatPlace, index, ax):

#     if index != len(categories)-1:

#         print("yes")

#         i = 0
#         for j in range(-(int(len(categories[index])/2)), int(len(categories[index])/2)+1):

#             if j != 0:
#                 xPlacement = higherCatPlace/(j/len(categories[index][i]))
#             else:
#                 xPlacement = higherCatPlace

#             plt.text(xPlacement, -.11, categories[index][i], horizontalalignment="center", transform=ax.transAxes) #-(.1+len(categories)-index)/100

#             categoryPlacement(categories, xPlacement, index+1, ax)

#             i += 1

#     else:
#         pass
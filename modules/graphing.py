
import matplotlib.pyplot as plt
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
    
    for key, value in sorted(data.items()):

        keyList = key.split(",")

        for i in range(len(keyList)):
            xticks[i].append(keyList[i])



        if value[0] != None:
            plt.scatter(key, value[0], color="blue", marker="_")
        plt.scatter(key, value[1], color="blue", marker=".")
        if value[2] != None:
            plt.scatter(key, value[2], color="blue", marker="_")
        if value[0] != None and value[2] != None:
            plt.plot([key]*3, [value[0], value[1], value[2]], color="blue", linewidth=.85)

    tickRange = 1

    for i in range(len(xticks)):
        xticks[i] = list(set(xticks[i]))

        tickRange *= xticks[i]

    for i in range(len(xtick))

    plt.xticks(labels=labels, ticks=(range(tickRange-1)))

    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel) 

    if len(gridLines)==1:
        plt.grid(which="major", axis=gridLines)
    elif gridLines == "xy":
        plt.grid(which="major", axis="both")

    plt.tight_layout()

    plt.show()

    
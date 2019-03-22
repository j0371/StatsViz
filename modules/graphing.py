import matplotlib.pyplot as plt
import itertools
from collections import defaultdict

#function that creates and shows the scatterplot
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

    if(groups != None):
        plt.legend(loc="best")   

    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)

    if len(gridLines)==1:
        plt.grid(which="major", axis=gridLines)
    elif gridLines == "xy":
        plt.grid(which="major", axis="both")

    plt.tight_layout()

    plt.show()

#function that creates and shows the interval plot
def graphInterval(*,data: dict, title: str = None, xLabel: str = None,
                  yLabel: str = None, gridLines: str = "", groupNames: tuple=()):

    _, ax = plt.subplots()

    if len(groupNames) > 1:
        groupNames = (":\n".join(reversed(groupNames)))+":"
        plt.text(-.015,-.02, s=groupNames, horizontalalignment="right", verticalalignment="top", transform=ax.transAxes)

    sortedData = sorted(data.items())

    for key, value in sortedData:

        inverseKey = "\n".join(reversed(key.split("\n")))

        if key in data:

            if value[0] != None:
                plt.scatter(inverseKey, value[0], color="blue", marker="_")
            plt.scatter(inverseKey, value[1], color="blue", marker=".")
            if value[2] != None:
                plt.scatter(inverseKey, value[2], color="blue", marker="_")
            if value[0] != None and value[2] != None:
                plt.plot([inverseKey]*3, [value[0], value[1], value[2]], color="blue", linewidth=.85)

        #else:
            #plt.scatter(inverseKey, None)

    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)

    if len(gridLines)==1:
        plt.grid(which="major", axis=gridLines)
    elif gridLines == "xy":
        plt.grid(which="major", axis="both")

    plt.tight_layout()

    plt.show()
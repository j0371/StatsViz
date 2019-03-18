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
                  yLabel: str = None, gridLines: str = "", groupNames: tuple=()):

    _, ax = plt.subplots()

    if len(groupNames) > 1:
        groupNames = (":\n".join(reversed(groupNames)))+":"
        plt.text(-.015,-.02, s=groupNames, horizontalalignment="right", verticalalignment="top", transform=ax.transAxes)

    sortedData = sorted(data.items())

    labels = []

    l3Last = ""
    l2Last = ""

    for key, value in sortedData:

        keySplit = key.split("\n")

        label = keySplit[2]+"\n"

        if keySplit[1] != l2Last:
            label += keySplit[2]+"\n"
        if keySplit[0] != l3Last:
            label += keySplit[0]

        labels.append(label)

        l2Last = keySplit[1]
        l3Last = keySplit[0]

        if value[0] != None:
            plt.scatter(key, value[0], color="blue", marker="_")
        plt.scatter(key, value[1], color="blue", marker=".")
        if value[2] != None:
            plt.scatter(key, value[2], color="blue", marker="_")
        if value[0] != None and value[2] != None:
            plt.plot([key]*3, [value[0], value[1], value[2]], color="blue", linewidth=.85)


    # index = 0
    # for i in range(len(xticks[0])):
    #     for j in range(len(xticks[1])):
    #         for k in range(len(xticks[2])):
    #             if key in data:
    #                 if k == 0:
    #                     labels[index] += "\n"+xticks[1].pop(0)
    #                 if j == 0:
    #                     labels[index] += "\n"+xticks[0].pop(0)
    #                 index += 1


    plt.xticks(labels=labels, ticks=range(len(sortedData)))

    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)

    if len(gridLines)==1:
        plt.grid(which="major", axis=gridLines)
    elif gridLines == "xy":
        plt.grid(which="major", axis="both")

    plt.tight_layout()

    plt.show() 
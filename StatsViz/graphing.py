
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import itertools
from collections import defaultdict
import natsort

from . import rw

#function that creates and shows the scatterplot
def graphScatter(*, xs: list, ys: list, groups: list = None, title: str = None,
                  xLabel: str = None, yLabel: str = None, gridLines: str = "", show: bool = False):

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
        plt.legend(loc="best").set_draggable(True)

    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)

    if len(gridLines)==1:
        pass
        plt.grid(which="major", axis=gridLines)
    elif gridLines == "xy":
        pass
        plt.grid(which="major", axis="both")

    plt.tight_layout()

    if show:
        plt.show()
    else:
        return plt.gcf()

#function that creates and shows the interval plot
def graphInterval(*,data: dict, title: str = None, xLabel: str = None,
                  yLabel: str = None, gridLines: str = "", groupNames: tuple=(), colorIndex: int = None, show: bool=False):

    _, ax = plt.subplots()

    if len(groupNames) > 1:
        groupNames = (":\n".join(reversed(groupNames)))+":"
        plt.text(-.015,-.02, s=groupNames, horizontalalignment="right", verticalalignment="top", transform=ax.transAxes)

    sortedData = natsort.realsorted(data.items(), key = lambda t: t[0])

    colorCatX = defaultdict(list)
    colorCatY = defaultdict(list)

    for key, value in sortedData:

        inverseKey = "\n".join(reversed(key.split("\n")))

        if colorIndex != None:
            colorCatX[key.split("\n")[colorIndex]].append(inverseKey)
            colorCatY[key.split("\n")[colorIndex]].append(value[1])
        else:
            colorCatX[key.split("\n")[0]].append(inverseKey)
            colorCatY[key.split("\n")[0]].append(value[1])

        if key in data:

            if value[0] != None:
                plt.scatter(inverseKey, value[0], marker="_", color="black")
            if value[2] != None:
                plt.scatter(inverseKey, value[2], marker="_", color="black")
            if value[0] != None and value[2] != None:
                plt.plot([inverseKey]*3, [value[0], value[1], value[2]], linewidth=.85, color="black")

    if colorIndex != None:
        for key, _ in colorCatX.items():
            plt.scatter(colorCatX[key], colorCatY[key], label=key)
            plt.legend(loc="best").set_draggable(True)
    else:
        for key, _ in colorCatX.items():
            plt.scatter(colorCatX[key], colorCatY[key], color="blue")

    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)

    if len(gridLines)==1:
        plt.grid(which="major", axis=gridLines)
    elif gridLines == "xy":
        plt.grid(which="major", axis="both")

    plt.tight_layout()

    if show:
        plt.show()
    else:
        return plt.gcf()

def graphHist(*, xs: list,bins: int = None, title: str = None, xLabel: str = None,
                  yLabel: str = None, gridLines: str = "", show: bool=False):

    _, _ = plt.subplots()

    if(bins != None):
        plt.hist(xs, edgecolor="black", bins=bins)
    else:
        plt.hist(xs, edgecolor="black")

    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)

    if len(gridLines)==1:
        pass
        plt.grid(which="major", axis=gridLines)
    elif gridLines == "xy":
        pass
        plt.grid(which="major", axis="both")

    plt.tight_layout()

    if show:
        plt.show()
    else:
        return plt.gcf()

def figureFromFile(fileName, show: bool=False):

    figType = rw.getFigType(fileName)

    if figType == "scatter":
        xs,ys,groups,title,xLabel,yLabel,gridLines = rw.loadFigure(fileName)
        return graphScatter(xs=xs, ys=ys, groups=groups, title=title, xLabel=xLabel, yLabel=yLabel, gridLines=gridLines, show=show)
    elif figType == "interval":
        data,title,xLabel,yLabel,gridLines, groupNames, colorIndex = rw.loadFigure(fileName)
        return graphInterval(data=data, title=title, xLabel=xLabel, yLabel=yLabel, gridLines=gridLines, groupNames=groupNames, colorIndex=colorIndex, show=show)
    elif figType == "histogram":
        xs, bins, title, xLabel, yLabel, gridLines = rw.loadFigure(fileName)
        return graphHist(xs=xs, bins=bins, title=title, xLabel=xLabel, yLabel=yLabel, gridLines=gridLines, show=show)



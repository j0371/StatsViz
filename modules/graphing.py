
import matplotlib.pyplot as mplot
from collections import defaultdict

def graphScatter( *, xs: int, ys: int, groups: list = None, title: str = None,
                  xLabel: str = None, yLabel: str = None, gridLines: str = ""):
    
    if(groups != None):
        xPoints = defaultdict(list)
        yPoints = defaultdict(list)
        groupSet = list(set(groups[0]))

        for i in range(0,len(groups[0])):
            xPoints[groups[0][i]].append(xs[i])
            yPoints[groups[0][i]].append(ys[i])

        for i in range(0, len(groupSet)):
            mplot.scatter(xPoints[groupSet[i]], yPoints[groupSet[i]], label=groupSet[i])
    else:
        mplot.scatter(xs, ys)

    mplot.title(title)
    mplot.xlabel(xLabel)
    mplot.ylabel(yLabel)
    mplot.legend(loc="best")

    if len(gridLines)==1:
        mplot.grid(which="major", axis=gridLines)
    elif gridLines == "xy":
        mplot.grid(which="major", axis="both")


    mplot.show()
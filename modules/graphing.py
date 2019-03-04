
import matplotlib.pyplot as mplot

def graphScatter( *, xs: int, ys: int, groups: list, title: str, xLabel: str, yLabel: str):
    
    if(groups != None):
        xPoints = {}
        yPoints = {}
        groupSet = list(set(groups[0]))

        for i in range(0,len(groups[0])):
            xPoints[groups[0][i]].append(xs[i])
            yPoints[groups[0][i]].append(ys[i])

        for i in range(0, len(groupSet)):
            mplot.scatter(xPoints[groupSet[i]], yPoints[groupSet[i]])
    else:
        mplot.scatter(xs, ys)

    mplot.show()
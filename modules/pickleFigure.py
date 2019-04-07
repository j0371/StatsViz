import matplotlib.pyplot as plt
import pickle
from collections import defaultdict

# fr = open("temp2.txt", "r")

# lines = fr.readlines()

# xs = lines[0].split()

# for x in xs:
#     try:
#         x = int(x)
#     except:
#         try:
#             x = float(x)
#         except:
#             pass

# ys = lines[1].split()

# for y in ys:
#     try:
#         y = int(y)
#     except:
#         try:
#             y = float(y)
#         except:
#             pass

# groups = []
# groups.append([])
# groups[0] = lines[2].split()

# title = lines[3]
# xLabel = lines[4]
# yLabel = lines[5]

# if(len(lines) > 6):
#     gridLines = lines[6]
# else:
#     gridLines = ""

xs = [1,2,3]
ys = [1,2,3]
groups = [["sin", "cos", "tan"]]
title = "test"
xLabel = "test"
yLabel = "test"
gridLines = ""

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

pickle.dump(plt.gcf(), open("figure.pickle", "wb"))
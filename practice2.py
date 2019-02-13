import matplotlib.pyplot as mplot

xs = []
ys = []

data = open("signals.csv", "r")
data = data.read()
data = data.split("\n")

while (data[-1] == ""):
    data.pop()

for i in range(0,len(data)):
    row = data[i].split(",")
    print(row[1])
    xs.append(row[1])
    ys.append(row[2])

mplot.scatter(ys,xs,color="red")
mplot.show()
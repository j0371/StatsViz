import matplotlib.pyplot as mplot
import numpy
import scipy.stats as stats

xs = []
ys = []

data = open("signals.csv", "r")
data = data.read()
data = data.split("\n")

while (data[-1] == ""):
    data.pop()

row2 = []

for i in range(0,len(data)):
    row = data[i].split(",")

    row2.append(float(row[2]))    


print(stats.t.interval(0.95, len(row2)-1, loc=numpy.mean(row2), scale=stats.sem(row2)))

stuff = [10,20,30,40,50]

print(stats.t.interval(0.95, len(stuff)-1, loc=numpy.mean(stuff), scale=stats.sem(stuff)))

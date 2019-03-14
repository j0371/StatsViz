import calculation
import rw

data = rw.read("..\sampleData\PaintHardness.csv")

labels = calculation.popLabels(data=data)

data = calculation.getColumns(data=data, yCol=2, groups=[0,3,1])

concat = calculation.concatGroup(ys=data[1], groups=data[2])

print(concat)


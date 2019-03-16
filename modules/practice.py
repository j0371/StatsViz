import calculation
import rw
import numpy as np


data = rw.read("../sampleData/sample.csv")

calculation.popLabels(data=data)

_,ys,_ = calculation.getColumns(data=data, yCol=1)

print(np.std(ys))
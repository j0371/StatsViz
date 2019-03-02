
def getColumns(*, data: [[]], xCol: int, yCol: int, groups: [int]) -> ([],[],[[]]):

    xs = []
    ys = []
    groupData = [[]]
    
    for i in range(0, len(data)):
        xs.append(data[i][xCol])
        ys.append(data[i][yCol])

        for j in range(0, len(groups)):
            groupData.append([])
            groupData[j].append(data[i][groups[j]])

    return (xs,ys,groupData)

def shaveLabels():
    pass
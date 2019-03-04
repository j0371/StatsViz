
def getColumns(*, data: [], xCol: int, yCol: int, groups: list):

    xs = []
    ys = []
    groupData = []

    if(groups != [-1]):
        for i in range(0,len(groups)):
            groupData.append([])
    
    for i in range(0, len(data)):
        xs.append(data[i][xCol])
        ys.append(data[i][yCol])

        if(groups != [-1]):
            for j in range(0, len(groups)):
                groupData[j].append(data[i][groups[j]])

    if(groups != [-1]):
        return (xs,ys,groupData)
    else:
        return (xs, ys, None)

def shaveLabels(*, data: []):
    return data.pop(0)

def getColumns(*, data: [], xCol: int = None, yCol: int, groups: list):

    xs = []
    ys = []
    groupData = []

    if(groups != [-1]):
        for i in range(0,len(groups)):
            groupData.append([])
    
    for i in range(0, len(data)):
        if(xCol != None):
            xs.append(data[i][xCol])
        ys.append(data[i][yCol])

        if(groups != [-1]):
            for j in range(0, len(groups)):
                groupData[j].append(data[i][groups[j]])

    if(groups != [-1]):
        return (xs,ys,groupData)
    else:
        return (xs, ys, None)

def concatGroup(*, ys: list, groups: list):

    strings = []
    groupVal = {}

    for i in range(len(groups[0])):
        string = []
        for j in range(len(groups)):
            if(j != len(groups)-1):
                string.append(str(groups[j][i])+"\n")
            else:
                string.append(str(groups[j][i]))

        strings.append("".join(string))
        groupVal["".join(string)] = ys[i]


    return groupVal



def popLabels(*, data: []):
    return data.pop(0)
#function that reads data from a csv file and formats it in a way that the rest of the
#program can interpret
def read(fileName: str):

#reads data from a file
    data = open(fileName, "r")

    data = data.read()
    data = data.split("\n")

    while (data[-1] == ""):
        data.pop()

    dataType = [] #variable that saves datatype of first row in each column

    inconsistentCell = None #last cell that has inconsistent data in the column (if exists)

#loops through each row of the csv (i is the row index)
    for i in range(0,len(data)):
        data[i] = data[i].split(",")

#loops through each column at row i (j is the column index)
        for j in range(0,len(data[i])):

            data[i][j] = data[i][j].strip("\"")

#if the data can be converted to int it will be, otherwise it'll be converted to
#float, and if it can't convert to float it will stay as a string
            try:
                data[i][j] = int(data[i][j])
            except:
                try:
                    data[i][j] = float(data[i][j])
                except:
                    pass

            if i == 1:
                dataType.append(type(data[i][j]))
            elif i > 1 and type(data[i][j]) != dataType[j]:
                inconsistentCell = (i+1,j+1)
                
    return (data, inconsistentCell)

def saveScatter(*, xs: list, ys: list, groups: list = None, title: str = None,
                  xLabel: str = None, yLabel: str = None, gridLines: str = "", fileName: str):
    
    fw = open(fileName, "w")
    fw.write("scatter\n")
    for x in xs:
        x = str(x).replace(" ", "**SPACE**")
        fw.write(x+" ")
    fw.write("\n")
    for y in ys:
        y = str(y).replace(" ", "**SPACE**")
        fw.write(y+" ")
    fw.write("\n")

    if groups != None:
        for group in groups[0]:
            group = str(group).replace(" ","**SPACE**")
            fw.write(group+" ")
    else:
        fw.write(" ")

    fw.write("\n")

    if title != None or title != "":
        fw.write(title+"\n")
    else:
        fw.write(" \n")

    if xLabel != None or xLabel != "":
        fw.write(xLabel+"\n")
    else:
        fw.write(" \n")

    if yLabel != None or yLabel !=  "":
        fw.write(yLabel+"\n")
    else:
        fw.write(" \n")

    fw.write(gridLines)
    fw.close()

def saveInterval(*,data: dict, title: str = None, xLabel: str = None,
                  yLabel: str = None, gridLines: str = "", groupNames: tuple=(), colorIndex: int = None, fileName: str):
    
    fw = open(fileName, "w")
    fw.write("interval\n")

    dataKeys = []
    dataUppers = []
    dataMeans = []
    dataLowers = []

    for key,value in data.items():

        key = key.replace("\n", "\\n")
        key = key.replace(" ", "**SPACE**")

        dataKeys.append(key)
        dataUppers.append(value[0])
        dataMeans.append(value[1])
        dataLowers.append(value[2])

    for key in dataKeys:
        fw.write(str(key)+" ")
    fw.write("\n")

    for upper in dataUppers:
        fw.write(str(upper)+" ")
    fw.write("\n")

    for mean in dataMeans:
        fw.write(str(mean)+" ")
    fw.write("\n")

    for lower in dataLowers:
        fw.write(str(lower)+" ")
    fw.write("\n")

    if title != None or title != "":
        fw.write(title+"\n")
    else:
        fw.write(" \n")

    if xLabel != None or xLabel != "":
        fw.write(xLabel+"\n")
    else:
        fw.write(" \n")

    if yLabel != None or yLabel !=  "":
        fw.write(yLabel+"\n")
    else:
        fw.write(" \n")

    for name in groupNames:
        name = name.replace(" ", "**SPACE**")
        fw.write(name+" ")
    fw.write("\n")

    if  colorIndex != None:
        fw.write(str(colorIndex)+"\n")
    else:
        fw.write(" \n")

    fw.write(gridLines)
    fw.close()

def saveHist(*, xs: list, bins: int = None, title: str = None, xLabel: str = None,
                  yLabel: str = None, gridLines: str = "", fileName: str):

    fw = open(fileName, "w")

    fw.write("histogram\n")

    for x in xs:
        x = str(x).replace(" ", "**SPACE**")
        fw.write(str(x)+" ")
    fw.write("\n")

    if bins != None:
        fw.write(str(bins) + "\n")
    else:
        fw.write(" \n")

    if title != None or title != "":
        fw.write(title+"\n")
    else:
        fw.write(" \n")

    if xLabel != None or xLabel != "":
        fw.write(xLabel+"\n")
    else:
        fw.write(" \n")

    if yLabel != None or yLabel !=  "":
        fw.write(yLabel+"\n")
    else:
        fw.write(" \n")

    fw.write(gridLines)
    fw.close()
    

def loadFigure(fileName):
    
    fr = open(fileName, "r")

    lines = fr.read().splitlines()

    figType = lines[0]

    if figType == "scatter":

        xs = lines[1].split()
        ys = lines[2].split()

        groups = []
        groups.append([])
        groups[0] = lines[3].split()

        data = (xs, ys)

        for i in range(len(data)):
            for j in range(len(data[i])):

                data[i][j] = data[i][j].replace("**SPACE**", " ")

                try:
                    data[i][j] = int(data[i][j])
                except:
                    try:
                        data[i][j] = float(data[i][j])
                    except:
                        pass

        for i in range(len(groups[0])):
            groups[0][i] = groups[0][i].replace("**SPACE**", " ")
            try:
                groups[0][i] = int(groups[0][i])
            except:
                try:
                    groups[0][i] = float(groups[0][i])
                except:
                    pass

        if len(groups[0]) < 2:
            groups = None

        title = lines[4]
        xLabel = lines[5]
        yLabel = lines[6]

        if(len(lines) > 7):
            gridLines = lines[7]
        else:
            gridLines = ""

        return (xs, ys, groups, title, xLabel, yLabel, gridLines)

    elif figType == "interval":
        
        keys = lines[1].split()
        uppers = lines[2].split()
        means = lines[3].split()
        lowers = lines[4].split()

        for i in range(len(keys)):
            keys[i] = keys[i].replace("\\n", "\n")
            keys[i] = keys[i].replace("**SPACE**", " ")

        for i in range(len(uppers)):
            if uppers[i] == "None":
                uppers[i] = None
            if lowers[i] == "None":
                lowers[i] = None

        data = (uppers, means, lowers)

        for i in range(len(data)):
            for j in range(len(data[i])):
                try:
                    data[i][j] = int(data[i][j])
                except:
                    try:
                        data[i][j] = float(data[i][j])
                    except:
                        pass

        dataDict = {}

        for i in range(len(keys)):
            dataDict[keys[i]] = (uppers[i], means[i], lowers[i])

        title = lines[5]
        xLabel = lines[6]
        yLabel = lines[7]

        groupNames = []

        groupNamesLoad = lines[8].split()

        for name in groupNamesLoad:
            name = name.replace("**SPACE**", " ")
            groupNames.append(name)
        groupNames = tuple(groupNames)

        if lines[9] == " ":
            colorIndex = None
        else:
            colorIndex = int(lines[9])

        if(len(lines) > 10):
            gridLines = lines[10]
        else:
            gridLines = ""

        return (dataDict, title, xLabel, yLabel, gridLines, groupNames, colorIndex)

    elif figType == "histogram":
        
        xs = lines[1].split()

        for i in range(len(xs)):

            xs[i] = xs[i].replace("**SPACE**", " ")

            try:
                xs[i] = int(xs[i])
            except:
                try:
                    xs[i] = float(xs[i])
                except:
                    pass

        if lines[2] == " ":
            bins = None
        else:
            bins = int(lines[2])

        title = lines[3]
        xLabel = lines[4]
        yLabel = lines[5]

        if(len(lines) > 6):
            gridLines = lines[6]
        else:
            gridLines = ""

        return (xs, bins, title, xLabel, yLabel, gridLines)
        
        
        


def getFigType(fileName):
    fr = open(fileName, "r")
    lines = fr.read().splitlines()
    return lines[0]
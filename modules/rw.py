import pickle

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

#iff the data can be converted to int it will be, otherwise it'll be converted to
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
        fw.write(str(x)+" ")
    fw.write("\n")
    for y in ys:
        fw.write(str(y)+" ")
    fw.write("\n")

    if groups != None:
        for group in groups[0]:
            fw.write(str(group)+" ")
    else:
        fw.write(" ")

    fw.write("\n")
    fw.write(title+"\n")
    fw.write(xLabel+"\n")
    fw.write(yLabel+"\n")
    fw.write(gridLines)
    fw.close()

def loadFigure(fileName):
    
    fr = open(fileName, "r")

    lines = fr.readlines()

    figType = lines[0]

    if figType == "scatter":
        xs = lines[1].split()

        for x in xs:
            try:
                x = int(x)
            except:
                try:
                    x = float(x)
                except:
                    pass

        ys = lines[2].split()

        for y in ys:
            try:
                y = int(y)
            except:
                try:
                    y = float(y)
                except:
                    pass

        groups = []
        groups.append([])
        groups[0] = lines[3].split()

        if (groups[0]) < 2:
            groups = None

        title = lines[4]
        xLabel = lines[5]
        yLabel = lines[6]

        if(len(lines) > 7):
            gridLines = lines[7]
        else:
            gridLines = ""

        return (figType, xs, ys, groups, title, xLabel, yLabel, gridLines)

    elif figType == "interval":
        pass
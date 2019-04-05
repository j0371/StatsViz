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

def readPickle(fileName: str):
    return pickle.load(open(fileName,'rb'))

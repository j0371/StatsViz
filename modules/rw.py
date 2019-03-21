def read(fileName: str) -> []:

    data = open(fileName, "r")

    data = data.read()
    data = data.split("\n")

    while (data[-1] == ""):
        data.pop()

    dataType = []

    inconsistentCell = None

    for i in range(0,len(data)):
        data[i] = data[i].split(",")

        for j in range(0,len(data[i])):

            data[i][j] = data[i][j].strip("\"")

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

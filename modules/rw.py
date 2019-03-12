def read(fileName: str) -> []:
    
    data = open(fileName, "r")
    data = data.read()
    data = data.split("\n")

    while (data[-1] == ""):
        data.pop()

    for i in range(0,len(data)):
        data[i] = data[i].split(",")

        for j in range(0,len(data[i])):
            try:
                data[i][j] = float(data[i][j])
            except:
                pass

    return data
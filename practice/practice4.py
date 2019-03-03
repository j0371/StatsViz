

lst = []

lst2 = []

for i in range(0,100):
    lst.append(i)

for i in range(0,10):
    lst2.append([])
    for j in range(0,10):
        lst2[i].append(j)

print (lst2)
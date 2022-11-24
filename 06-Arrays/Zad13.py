array=[[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
parzyste=0
nieparzyste=0
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j]%2==0:
            parzyste+=array[i][j]
        else:nieparzyste+=array[i][j]
print(parzyste, nieparzyste)

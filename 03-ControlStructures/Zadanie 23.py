wys = int(input("podaj wysokość piramidy: "))
for i in range(1,wys+1,1):
    j=0
    while j<i:
        print(i, end=" ")
        j=j+1
    print()
    i=i+1    
wys = int(input("podaj wysokość strzałki: "))
for i in range(1,wys+1,1):
    j=0
    while j<i:
        print("*", end=" ")
        j=j+1
    print()
    i=i+1 

for k in range(wys-1,0,-1):
    j=0
    while j<k:
        print("*", end=" ")
        j=j+1
    print()
    k=k-1    
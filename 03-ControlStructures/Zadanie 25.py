a = int(input("podaj wymiar a: "))
b = int(input("podaj wymiar b: "))
for i in range(1, a+1, 1):
    print("*",end="")
print()
for i in range(1,b-1,1):
    print("*",end="")
    for j in range(1,a-1,1): 
        print(" ",end="")
        j=j+1
    print("*")
    i=i+1
for i in range(1, a+1, 1):
    print("*",end="")
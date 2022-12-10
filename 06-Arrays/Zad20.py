array=[12,6,4,9,10]

def star(n):
    for i in range(0,n):
        print("*",end="")

for i in range(0,len(array)):
    print(star(array[i]))
    
star(10)
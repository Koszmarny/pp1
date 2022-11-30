array=[12,6,4,9,10]

def star(n):
    for i in range(0,n):
        print("*",end="")

for i in array:
    print( star(i))
    
star(10)
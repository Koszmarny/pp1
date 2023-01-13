def f(dictionary,x,y):
    suma=0
    for i in dictionary:
        for j in dictionary[i]:
            if j in range(x,y+1):
                suma+=int(j)

    return suma

print(f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6))
print(f({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}, 5, 10) )
def f(array2D):
    array1D=[sum([i[b] for i in array2D])for b in range(len(array2D[0]))]
    return array1D
    
print(f([ [3,6,2,7], [9,5,4,0], [2,8,0,9] ]) )
array=[15,8,31,47,2,19]
length = len(array)
suma = 0
for i in range(0,length):
    suma+=array[i]

print(f"array:", array," , arithmetic mean: ", round(suma/length,2) )
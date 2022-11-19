array = [-15,8,-31,47,-2,19]
maks = array[0]
mini = array[0]
for i in range(len(array)):
    if array[i] > maks:
        maks = array[i]
    elif array[i] < mini:
        mini = array[i]

print(maks, mini)
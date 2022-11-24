array = ["Genowefa","Onufry","Celestyna","Alojzy","Pankracy"]
maks = len(array[0])
ktory = array[0]
for i in range(len(array)):
    if len(array[i]) > maks:
        maks = len(array[i])
        ktory=array[i]

print(ktory)

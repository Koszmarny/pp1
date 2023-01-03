import random

with open("rand50.txt",'w') as file:
    for i in range (51):
        randl=random.randint(100,999)
        file.writelines(str(randl)+'\n')
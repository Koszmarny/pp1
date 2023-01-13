import re

with open("leastsix.txt",'r') as file:
    lines=str(file.readlines())
    for word in lines.split():
        if len(word)>=6:
            print(word)
        else: pass
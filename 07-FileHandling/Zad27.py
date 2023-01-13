import re

with open("grades.txt",'r') as file:
    suma, ilosc = 0,0
    znaki = file.read()
    #for znak in znaki:
    for znak in re.findall(r"\d.\d",znaki):
        if str.isnumeric(znak):
            print(znak)
            suma+= int(znak)
            ilosc+=1
        else: pass
        
print(f"srednia ocen to : {suma/ilosc}")

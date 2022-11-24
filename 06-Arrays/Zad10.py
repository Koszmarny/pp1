array = [12,53,2,8,17,9,101,]
i=0
parzyste=0
nieparzyste=0
while i<len(array):
    if array[i]%2==0:
        parzyste+=1
    else: nieparzyste+=1
    
    i+=1
print(f"parzyste: ", parzyste, "nieparzyste: " , nieparzyste)
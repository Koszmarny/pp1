with open("1to50.txt",'w') as file:
    for i in range (51):
        file.writelines(str(i)+'\n')
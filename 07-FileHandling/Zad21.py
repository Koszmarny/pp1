with open("10power.txt",'w') as file:
    for i in range (1,11):
        file.writelines(str(i)+", "+str(i*i)+", "+str(i*i*i)+'\n')
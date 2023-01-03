with open("co5.txt",'r') as file:
    i=0
    line = file.readlines()
    while i< len(line):
        for j in range(5):
            print(line[i+j])
            j+=1
        input("pres enter to continue")
        i+=5
        

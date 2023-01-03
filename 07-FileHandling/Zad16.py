with open("co5.txt",'r') as file1:
    file2= open("copy.txt",'w')
    line=file1.readlines()
    file2.writelines(line)
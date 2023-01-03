with open("shoppinglist.txt",'a') as list:
    MF = open("MeatAndFish.txt",'r')
    list.writelines(MF)
    MF.close()
    GB = open("GrainsANdBread.txt",'r')
    list.writelines(GB)
    GB.close()
    
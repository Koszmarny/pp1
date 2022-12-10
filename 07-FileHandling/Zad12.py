file = open('07-FileHandling/shopping.txt','a')
while True:
    choice = input('\nco kupic?: ')
    file.write('\n'+choice)
    if choice=="":break
file.close
import random

PCroll = random.randrange(1,7)
UserRoll = int(input("zgadnij rzut, podaj liczbe od 1 do 6: "))
print (UserRoll==PCroll)
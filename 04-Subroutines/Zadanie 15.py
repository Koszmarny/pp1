from mymath import read_number
from mymath import generate_number

print("Let's play a game")
print("enter one digit number")

liczbaKompa = generate_number()
liczbaGracza = read_number()
print(liczbaGracza, liczbaKompa)
if liczbaGracza==liczbaKompa:
    print("wygrana")
else: print("przegrana")    

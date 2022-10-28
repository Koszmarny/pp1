PIN = "0805"

for i in range(1,4,1):
    x = input("Enter PIN code: ")
    if x==PIN: 
        print("poprawne haslo") 
        break
    else: 
        print("Niepoprawne...")
        i=i+1
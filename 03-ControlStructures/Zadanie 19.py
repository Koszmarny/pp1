DogAgeH = int(input("Enter dog's age in human years: "))
DogAgeD = 0
if DogAgeH <=2: DogAgeD=DogAgeH*10.5
else: DogAgeD = 21+(DogAgeH-2)*4
print(f"Dog's age in dog's years is {DogAgeD} years")
import math


SideA = int(input("podaj bok A: "))
SideB = int(input("podaj bok B: "))
SideC = int(input("Podaj bok C: "))

S = (SideA+SideB+SideC)/2
Area = math.sqrt(S*(S-SideA)*(S-SideB)*(S-SideC))
print(f"Pole trójkąta o bokach: {SideA}, {SideB} i {SideC} wynosi: {Area}")
from math import floor
import math

Total = int(input("Enter the amount in PLN: "))
ile5 = math.floor(Total/5)
ile2 = math.floor(Total%5/2)
ile1 = Total%5%2
print(f"Amount of PLN {Total} in coins: ")
print ("5 zł - ",ile5)
print ("2 zł - ",ile2)
print ("1 zł - ",ile1)
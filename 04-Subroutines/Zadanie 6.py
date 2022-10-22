def klawiaturka():
    for i in range(1, 4): print(i, end=" ")
    print()
    for j in range(4, 7): print(j, end=" ")
    print()
    for k in range(7, 10): print(k, end=" ")

klawiaturka()
print()

for l in range(1, 10): 
    if l%3 == 0: print(l)
    else: print(l, end=" ")
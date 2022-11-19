def f(n1, n2, n3):
    minimum = n3
    maksimum = n1
    if n1 < n2 and n2 > n3:
        maksimum = n2
    elif n2 < n3 and n1 < n3:
     maksimum = n3
    if n1 > n2 and n2 < n3:
        minimum = n2
    elif n2 > n3 and n1 > n3:
     minimum = n3
    return maksimum - minimum

print(f(9,4,7))
     
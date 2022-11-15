def f(number, even):
    lista = [int(i) for i in str(number)]
    print(lista)
    suma=0
    if even:
        for i in lista:
            if i%2==0:
                suma+=i
    else:
        for i in lista:
            if i%2==1:
                suma+=i
    return suma

print(f(2137420,True ))
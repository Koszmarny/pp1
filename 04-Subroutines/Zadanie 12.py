def SUM(n):
    odliczanie = 1
    suma =1
    while odliczanie<n:
        odliczanie+=1
        suma+=odliczanie
    return suma    
       
  
x = 10
print( f"Suma od 1 do {x} = {SUM(x)}" )
#liczba linii w pliku txt
plik=input("podaj ścieżkę pliku")
with open(plik,'r') as file:
    l=len(file.readlines())
print(f"Number of lines ",l)
def f(first_letter,last_letter):
    with open("09-Test2/data.txt",'r',encoding="UTF-8") as file:
        wynik=0
        slowa=file.read().split()
        #print(slowa)
        for slowo in slowa:
            if slowo.startswith(first_letter)& slowo.endswith(last_letter):
                wynik+=1
    return wynik
#f("w","d")    
print(f("w","d"))
import random


def read_number():
    number = input("podaj liczbę: ")
    return(int(number))

def generate_number():
    return(random.randrange(1,10)) 


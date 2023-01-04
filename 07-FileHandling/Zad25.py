import re
expresion = "To be, or not to be, that is the question"
wynik = re.compile(r' ').split(expresion)
print(f"w wyrażeniu jest {len(wynik)} wyrazów")
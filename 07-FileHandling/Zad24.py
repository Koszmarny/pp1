import re
expresion = "To be, or not to be, that is the question"
#vowels = re.search(samogloski,expresion)

vowels = re.findall("[aoeui]", expresion)

number = len(vowels)
print(f"The number of vowels in the text is {number}")
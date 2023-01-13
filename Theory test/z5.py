import re

DD="1.22.333.4444.55555.666666"
print(re.findall(r'\d',DD))
#wszsystkie cyfry osobno
print(re.findall(r'\d+',DD))
#6: 1,22,333...
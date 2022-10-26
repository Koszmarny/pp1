from lib2to3.pgen2.token import PERCENT


Amount = 15.84
Vat = round(Amount*0.23, 2)
print(f"Amount   : {Amount}")
print(f"VAT 23%  : {Vat}")
def f(binary_number):
    bin = list(binary_number) 
    czy = 0 
    for i in bin:
        if i =="0" or i == "1":
            pass
        else:
            czy = 1 
            break
    if czy == 0: return True
    else: return False

print(f("01010010"))
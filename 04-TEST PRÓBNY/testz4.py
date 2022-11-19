def f(expression):
    x = 0
    exception = False
    for i in expression:
        try:
            i = int(i)
            if exception == True:
                i = i * -1
                exception = False
        except ValueError:
            if i == "+":
                continue
            else:
                exception = True

        if exception == True:
            continue
        
        x += i
    return x
    
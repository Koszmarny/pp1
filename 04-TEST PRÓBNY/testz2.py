def f(name):
    y = ""
    x = name.split()
    for i in x:
        y += i[0]
    return y

print(f("Kuba z buczkowic"))


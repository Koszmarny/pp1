#WITH
with open("07-FileHandling/countries.txt") as f:
    for line in f:
        print(line, end="")
f.close()

import csv

with open("students.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line=0
    for row in csv_reader:
        if line==0:
            print(", ".join(row))
            line+=1
        elif int(row[2])<30:
           # print(", ".join(row))
            print(f"{row[0]} {row[1]} {row[4]}")
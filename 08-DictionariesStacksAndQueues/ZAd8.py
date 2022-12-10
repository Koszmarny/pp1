person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }
   #a
for i in person:
    print(i,": ", person[i])
#b
print(person["name"])
#c
for i in range(2):
    print(person["hobby"][i])
#d
person["surname"]="Nowak"
print (person["surname"])
#e
person["married"]=False

#f
person["gender"]="Male"

#g
person["hobby"]+=["bicycle"]
print(person)
#h
person["phone"]["work"]="313131444"


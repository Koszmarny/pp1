def f(human_age):
    dog_age=0
    if int(human_age)>2:
        dog_age+=20
        dog_age+=(human_age-2)*4
        return dog_age
    else:
        dog_age=human_age*10
        return dog_age

print(f(15))
print(f(2))
print(f(1.5))
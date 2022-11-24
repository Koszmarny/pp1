array=["styczen","luty","marzec","kwiecien","maj","czerwiec",
"lipiec","sierpien","wrzesien","pazdziernik","listopad","grudzien"]

def month(n):
    return array[n-1]

print(month(1))
print(month(2))
print(month(11))
print(month(12))
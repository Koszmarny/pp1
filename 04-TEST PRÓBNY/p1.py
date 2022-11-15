def f(card_number):
    cardArray = list(card_number)
    for i in range(2,12):
        cardArray[i] = "*"
    return ''.join(cardArray)

print(f("5290312400019022"))
def f(player1, player2):
    cards = {"A", "K", "Q", "J", "T"}
    sum1 = 0
    sum2 = 0
    for number in player1:
        if number in cards:
            sum1 += 10
        else:
            sum1 += int(number)
    for number in player2:
        if number in cards:
            sum2 += 10
        else:
            sum2 += int(number)
    if sum1 > sum2:
        return True
    else:
        return False


print(f("AJ972", "AQT72"))
print(f("9532", "K8"))
print(f("987", "AT4"))

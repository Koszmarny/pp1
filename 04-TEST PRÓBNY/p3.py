def f(amount_to_pay):
    rest = amount_to_pay%5
    ile5=(amount_to_pay-rest)/5
    ile1=rest%2
    ile2=(rest-ile1)/2
    return (ile5 + ile2 + ile1)

print(int(f(2)))

from functools import reduce


def amount_payment(payment):
    cleared = []
    for i in filter(lambda x: x > 0, payment):
        cleared.append(i)
    return reduce ((lambda x, y: x + y), cleared)

payment = [1, -3, 4]
print (amount_payment(payment))
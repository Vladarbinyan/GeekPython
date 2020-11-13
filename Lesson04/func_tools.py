import functools

user_balances = {'Vasya': 500, 'Petya': 300, 'Nina': 1000}


def my_balance(total, amount):
    return total + amount


# users_total = functools.reduce(my_balance, user_balances.values())

users_total = functools.reduce(
    lambda total, amount: total+amount,
    user_balances.values())

print(users_total)

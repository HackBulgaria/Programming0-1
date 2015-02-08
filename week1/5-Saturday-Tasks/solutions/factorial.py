# Това е същата задача като сумата на числата между 1 и n.
# Само че в този случай търсим тяхното произведение

n = input("Enter a number: ")
n = int(n)

start = 1
# Тук ще пазим резултата
product = 1

while start <= n:
    product = product * start
    start = start + 1

print(product)


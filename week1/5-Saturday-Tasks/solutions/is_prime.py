# Тук използваме трика с "флаговата" променлива
# Нашият флаг се казва is_prime, който има стойност True
# Ако нищо друго не успее да промени стойността на флага в цикъла
# То числото е просто

n = input("Enter a number: ")
n = int(n)

start = 2
is_prime = True

# Специален случай за 1.
if n == 1:
    is_prime = False

while start < n:
    if n % start == 0:
        is_prime = False
        break
    start = start + 1

if is_prime:
    print("It is prime")
else:
    print("It is not prime")

# Проблемът на тази задача е, че не знаем горната граница на интервала
# Например, не знае първите 4 перфектни числа в какъв интервал са
# За това подхождаме по следния начин - while True:
# За всяко число +1 гледаме дали е перфектно
# Aко намерим перфектно, намаляваме търснеата бройка с 1
# Когато търсената бройка стане 0, приключваме

n = input("Enter n: ")
n = int(n)

start = 6

while True:

    divisors_sum = 0
    divisor = 1

    while divisor < start:
        if start % divisor == 0:
            divisors_sum += divisor

        divisor += 1

    if divisors_sum == start:
        print(start)
        n = n - 1
    
    if n == 0:
        break

    start += 1

# Използваме предната задача, като основа на решението
# След като имаме списък с всички делители
# Не ни остава нищо друго, освен да ги сумираме

n = input("Enter n: ")
n = int(n)

divisors = []

start = 1
end = n - 1

while start <= end:
    if n % start == 0:
        divisors = divisors + [start]

    start += 1

divisors_sum = 0

for divisor in divisors:
    divisors_sum += divisor

print(divisors_sum)

# Това решение използва решението на предните 2 задачи за основа
# След като сме сумирали всички делители на n
# Ако получим n, то числото е перфектно

n = input("Enter n: ")
n = int(n)

divisors = []

start = 1
end = n - 1

while start <= end:
    if n % start == 0:
        divisors = divisors + [start]

    start += 1
    #print(start)

divisors_sum = 0

for divisor in divisors:
    divisors_sum += divisor

if divisors_sum == n:
    print("The number is perfect")
else:
    print("The number is not perfect")
















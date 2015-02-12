# Алтернативно решение на задачата
# Вместо да строим списък от делителите и да ги сумираме
# Направо сумираме всеки делител, когато го намерим

n = input("Enter n: ")
n = int(n)

divisors_sum = 0

start = 1
end = n - 1

while start <= end:
    if n % start == 0:
        divisors_sum += start

    start += 1

if divisors_sum == n:
    print("Number is perfect")
else:
    print("Number is not perfect")

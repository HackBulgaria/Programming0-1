# В списъка divisors ще държим всеки делител на n
n = input("Enter n: ")
n = int(n)

divisors = []

start = 1
end = n - 1

while start <= end:
    if n % start == 0:
        divisors = divisors + [start]

    start += 1

print("Divisors are: ")
print(divisors)

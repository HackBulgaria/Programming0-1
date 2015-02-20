def divisors(n):
    result = []

    start = 1
    end = n - 1

    while start <= end:
        if n % start == 0:
            result = result + [start]

        start += 1

    return result


n = input("Enter n: ")
n = int(n)

print(divisors(n))

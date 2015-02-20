def divisors(n):
    result = []

    start = 1
    end = n - 1

    while start <= end:
        if n % start == 0:
            result = result + [start]

        start += 1

    return result

def sum_ints(numbers):
    result = 0

    for number in numbers:
        result += number

    return result


def sum_divisors(n):
    return sum_ints(divisors(n))


def is_perfect(n):
    return sum_divisors(n) == n

n = input("Enter n: ")
n = int(n)

if is_perfect(n):
    print(str(n) + " is perfect!")
else:
    print(str(n) + " is not perfect!")

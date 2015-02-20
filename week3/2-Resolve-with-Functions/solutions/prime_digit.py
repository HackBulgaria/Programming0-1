def is_prime(n):
    if n <= 1:
        return False

    is_prime = True

    start = 2

    while start < n:
        if n % start == 0:
            is_prime = False
            break
        
        start += 1
    
    return is_prime


def to_digits(n):
    result = []
    
    while n != 0:
        digit = n % 10
        
        result = [digit] + result

        n = n // 10

    return result


n = input("Enter n: ")
n = int(n)

digits = to_digits(n)

prime_digit = False

for digit in digits:
    if is_prime(digit):
        prime_digit = True
        break

if prime_digit:
    print("There are prime digits!")
else:
    print("There are no prime digits!")

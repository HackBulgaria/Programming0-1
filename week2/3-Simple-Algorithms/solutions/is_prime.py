def is_prime(n):
    start = 2
    is_prime = True

    while start < n:
        if n % start == 0:
            is_prime = False
            break

        start += 1

    return is_prime

if is_prime(7) and is_prime(11) and is_prime(17):
    print("7, 11 and 17 are primes")

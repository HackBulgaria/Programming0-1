def is_prime(n):
    if n <= 1:
        return False

    start = 2
    is_prime = True

    while start < n:
        if n % start == 0:
            is_prime = False
            break

        start += 1

    return is_prime

p = input("Enter number: ")
p = int(p)

q = p - 2
r = p + 2

is_p_prime = is_prime(p)
is_q_prime = is_prime(q)
is_r_prime = is_prime(r)

if is_p_prime and (not is_q_prime) and (not is_r_prime):
    print(str(p) + " is prime")
    print("But " + str(q) + " and " + str(r) + " are not.")
elif is_p_prime:
    if is_q_prime:
        print(q, p)
    if is_r_prime:
        print(p, r)
else:
    print(str(p) + " is not prime.")

# Тази задача я правим по следния начин:
# Проверяваме дали p, q и q1 са прости числа
# И на базата на това взимаме решение за отговора

p = input("Enter number: ")
p = int(p)

q = p - 2
q1 = p + 2

# Проверяваме за p
is_p_prime = True
start = 2

while start < p:
    if p % start == 0:
        is_p_prime = False
        break
    start += 1

# Проверяваме за q = p - 2
is_q_prime = True
start = 2

while start < q:
    if q % start == 0:
        is_q_prime = False
        break
    start += 1

# Проверяваме за q1 = p + 2
is_q1_prime = True
start = 2

while start < q1:
    if q1 % start == 0:
        is_q1_prime = False
        break
    start += 1

# Правим нужните проверки накрая

if is_p_prime and (not is_q_prime) and (not is_q1_prime):
    print(str(p) + " is prime")
    print("But " + str(q) + " and " + str(q1) + " are not.")
elif is_p_prime:
    if is_q_prime:
        print(q, p)
    if is_q1_prime:
        print(p, q1)
else:
    print(str(p) + " is not prime.")

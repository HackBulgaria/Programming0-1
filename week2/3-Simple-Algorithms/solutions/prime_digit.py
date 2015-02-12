# Тази задача я решаваме по следния начин:
# Превръщаме n в списък от цифри
# Проверяваме за всяка цифра, ако е 2, 3, 5 или 7 - значи е просто цифра
# Използваме похвата с флаговата променлива

n = input("Enter n: ")
n = int(n)

digits = []

while n != 0:
    digit = n % 10

    digits = [digit] + digits 

    n = n // 10

has_prime_digit = False

for digit in digits:
    if digit in [2, 3, 5, 7]:
        has_prime_digit = True
        break

if has_prime_digit:
    print("At least one prime digit found")
else:
    print("No prime digits found")



    

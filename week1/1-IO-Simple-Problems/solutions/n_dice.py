from random import randint

n = input("Enter sides: ")
# Превръщаме string-a в int. Всеки input е string
n = int(n)

result = randint(1, n)

print(result)

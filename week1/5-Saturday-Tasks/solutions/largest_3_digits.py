# Tази задача ще я решим по-егелантно със списъци
# В случая, ни трябват
# x,y,z - трите цифри на въведеното число
# Най-голямото да решем x) и най-малкото (y) от тях
# Тогава числото xzy е най-голямото с тези цифри, а yzx е най-малкото

n = input("Enter a 3-digit number: ")
n = int(n)

# Взимаме трите цифри
z = n % 10
n = n // 10

y = n % 10
n = n // 10

x = n % 10
n = n // 10

# Виждаме дали сме ги взели правилно
print(x, y, z)

# Намираме най-голямата след цифрите
# Приемаме, че е x
# Aко y > x and y > z, то това е y
# Ако z > x and z > y, то това е z

largest = x

if y >= largest and y >= z:
    largest = y

if z >= largest and z >= y:
    largest = z

print("Largets digit: " + str(largest))

# По същата логика взимаме и най-малката

smallest = x

if y <= smallest and y <= z:
    smallest = y

if z <= smallest and z <= y:
    smallest = z

print("Smallest digit: " + str(smallest))

# Остана да определим коя е средната цифра, която не е нито най-голямата нито най-малката

middle = z

if (largest == z and smallest == y) or (smallest == z and largest == y):
    middle = x
elif (largest == z and smallest == x) or (smallest == z and largest == x):
    middle = y

max_number = largest * 100 + middle * 10 + smallest
min_number = smallest * 100 + middle * 10 + largest

print("Max number with those digits is: " + str(max_number))
print("Min number with those digits is: " + str(min_number))

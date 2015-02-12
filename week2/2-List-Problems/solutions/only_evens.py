# Четем числа от входа
# Ако числото е четно, го добавяме в списъка even_numbers
# Броят на четните числа = дължината на списъка even_numbers
# Накрая обхождаме списъка и изкарваме числата на екрана

n = input("Enter count of numbers: ")
n = int(n)

count = 1
even_numbers = []

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    
    if number % 2 == 0:
        even_numbers = even_numbers + [number]

    count += 1

print("Count of evens: " + str(len(even_numbers)))
print("Evens are: ")

for even in even_numbers:
    print(even)


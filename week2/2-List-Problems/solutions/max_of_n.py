# Добавяме всички числа в numbers
# След което търсим най-голямото

n = input("Enter n: ")
n = int(n)

start = 0
numbers = []

while start < n:
    number = input()
    number = int(number)
    
    numbers = numbers + [number]

    start += 1

# Най-голямото ни число е първото число в списъка
# След което обхождаме списъка
# И ако намерим по-голямо от това, което сме взели в началото
# Казваме, че новото current_max е това, което сме намерили
# Накаря, когато обходим списъка ще имаме най-голямото

current_max = numbers[0]

for number in numbers:
    if number > current_max:
        current_max = number

print(current_max)

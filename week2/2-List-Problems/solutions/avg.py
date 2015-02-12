# Четем числа от потребителя и ги слагаме в списъка numbers
# Накрая обхождаме списъка и сумираме всяко едно число
# След което го разделяме на дължината на списъка

n = input("Enter n: ")
n = int(n)

start = 0
numbers = []

while start < n:
    number = input()
    number = int(number)
    
    numbers = numbers + [number]

    start += 1


total_sum = 0
count_numbers = len(numbers)

for number in numbers:
    total_sum += number

avg = total_sum / count_numbers

print("Avg is: " + str(avg))

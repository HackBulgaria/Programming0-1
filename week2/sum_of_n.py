# sum_of_n.py

n = input("Enter number: ")
n = int(n)

numbers = range(1, n + 1)

total_sum = 0

for number in numbers:
    total_sum += number

print(total_sum)

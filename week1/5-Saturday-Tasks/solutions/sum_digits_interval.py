N = input("Enter N: ")
M = input("Enter M: ")

N = int(N)
M = int(M)

lower_bound = 0
upper_bound = 0

# Първото нещо, за което се грижим в тази задача е да видим как са ни дали интервалите
# Дали N > M или обратното
# Пазим правилните граници на интервалите в lower_bound и upper_bound

if N < M:
    lower_bound = N
    upper_bound = M
else:
    lower_bound = M
    upper_bound = N

# Започваме да обхождаме интервала - тази задача сме я решавали

start = lower_bound

while start <= upper_bound:

    n = start
    total_sum  = 0
    
    # Вътре в интервала, за всяко число, решаваме задачата със сумата на цифрите на дадено число
    while n != 0:
        digit = n % 10
        total_sum = total_sum + digit
        n = n // 10

    print("total_sum of digits of " + str(start) + " = " + str(total_sum))
    start += 1


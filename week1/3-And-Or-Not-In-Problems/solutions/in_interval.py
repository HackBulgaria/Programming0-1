a = input("Enter lower bound: ")
b = input("Enter upper bound: ")
x = input("Enter x: ")

a = int(a)
b = int(b)
x = int(x)

# Правим проверките поред на това, което ни питат.

if x == a:
    print("The number is equal to the lower bound of the interval")
elif x == b:
    print("The number is equal to the upper bound of the interval")
elif x > a and x < b:
    print("The number is in the interval")
elif x < a:
    print("The number is outside the interval, x < a")
elif x > b:
    # Покрили сме всички други случаи, остава да е вътре в интервала.
    print("The number is outside the interval, x > b")

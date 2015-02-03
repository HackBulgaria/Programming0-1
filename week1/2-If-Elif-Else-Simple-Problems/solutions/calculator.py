a = input("Enter a: ")
b = input("Enter b: ")
oper = input("Enter operation: ")

a = int(a)
b = int(b)

# Променлива в която ще държим резултата
# Aко променлива след края на сметката не е False
# Значи сме получили валиден символ
# Ако е False, значи не поддържаме тази операция
result = False


if oper == "+":
    result = a + b
elif oper == "-":
    result = a - b
elif oper == "*":
    result = a * b
elif oper == "/":
    result = a / b

# Ако не влезем в нито 1 от горните if / elif-и, result ще остане непроменен.
# Това означава, че ще има стойност False и ние сме получили операция, която не разбираме
if result != False:
    print("Result is:")
    print(result)
else:
    print("We do not support that operation.")

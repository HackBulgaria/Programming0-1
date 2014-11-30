a = input("Enter a:")
b = input("Enter b:")
operation = input("Enter operation:")

a = int(a)
b = int(b)
result = 0

if operation == "+":
    result = a + b
elif operation == "*":
    result = a * b
elif operation == "-":
    result = a - b
elif operation == "/":
    result = a / b
else:
    print("Unknown operation: " + str(operation))

print("The result is: " + str(result))

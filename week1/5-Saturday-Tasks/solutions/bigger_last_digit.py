number1 = input("Enter first number: ")
number2 = input("Enter second number: ")

number1 = int(number1)
number2 = int(number2)

# Взимаме последните 2 цифри и след това гледаме коя от тях е по-голяма

last_digit1 = number1 % 10
last_digit2 = number2 % 10

if last_digit1 > last_digit2:
    print(number1)
elif last_digit1 < last_digit2:
    print(number2)
else:
    if number1 > number2:
        print(number1)
    else:
        print(number2)


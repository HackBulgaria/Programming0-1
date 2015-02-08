# Tук ще използваме следния алгоритъм:
# Ще строим обърнатото число, спазвайки принципа, че ако имаме цифрите а и b
# Получаваме числото от тези цифри така: a * 10 + b
# a ще бъде досега обърнатото число, а b ще е текущата последна цифра на това, което обръщаме

n = input("Enter a number: ")
n = int(n)

reversed_number = 0

while n != 0:
    digit = n % 10

    reversed_number = reversed_number * 10 + digit

    n = n // 10

print("The reversed number is: " + str(reversed_number))

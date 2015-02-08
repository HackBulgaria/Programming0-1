# Четем число от потребителя
# Ако е четно и > 20, значи всичко е наред.

n = input("Enter number: ")
n = int(n)

if n % 2 == 0 and n > 20:
    print("Yes, it is!")
else:
    print("No, it isn't!")

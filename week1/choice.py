# choice.py

from random import randint

print("Enter 1 for a joke")
print("Enter 2 for a random number")
print("Enter 3 for for nothing")

number = input("What do you choose?")
number = int(number)

if number == 1:
    print("Something funny here")
elif number == 2:
    random_number = randint(1,100)
    print("A random number between 1 and 100:")
    print(random_number)
elif number == 3:
    print("Nothing!")

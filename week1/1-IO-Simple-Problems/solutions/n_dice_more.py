from random import randint

n = input("Enter sides: ")
n = int(n)

dice_roll_1 = randint(1, n)
dice_roll_2 = randint(1, n)

print(dice_roll_1 + dice_roll_2)


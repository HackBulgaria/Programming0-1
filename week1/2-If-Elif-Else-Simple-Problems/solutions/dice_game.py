from random import randint

sides = input("Enter dice sides: ")
sides = int(sides)

player1_name = input("Enter player1 name: ")
player2_name = input("Enter player2 name: ")

player1_dice_roll = randint(1, sides)
player2_dice_roll = randint(1, sides)


print(player1_name + " rolled: " + str(player1_dice_roll))
print(player2_name + " rolled: " + str(player2_dice_roll))

if player1_dice_roll == player2_dice_roll:
    print("Tie!")
elif player1_dice_roll > player2_dice_roll:
    print("The winner is: " + player1_name)
else: 
    print("The winner is: " + player2_name)

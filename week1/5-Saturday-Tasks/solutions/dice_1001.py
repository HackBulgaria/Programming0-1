from random import randint


ivan_score = 1001
maria_score = 1001

while True:

    # Симулираме 6 хвърляния за Мария
    
    counter = 1
    dice_roll_sum = 0

    while counter <= 6:
        dice_roll = randint(1, 6)
        
        dice_roll_sum += dice_roll
        
        counter += 1
        
    if maria_score > 0:
        maria_score -= dice_roll_sum
    elif maria_score < 0:
        maria_score += dice_roll_sum

    print("Maria rolls: " + str(dice_roll_sum) + " and has a score of: " + str(maria_score))
    
    if maria_score == 0:
        # ако сме стигнали точно 0, Мария печели
        break

    # Правим същото и за Иван
    
    counter = 1
    dice_roll_sum = 0
    
    while counter <= 6:
        dice_roll = randint(1, 6)
        
        dice_roll_sum += dice_roll
        
        counter += 1
        
    if ivan_score > 0:
        ivan_score -= dice_roll_sum
    elif ivan_score < 0:
        ivan_score += dice_roll_sum

    print("Ivan rolls: " + str(dice_roll_sum) + " and has a score of: " + str(ivan_score))
    
    if ivan_score == 0:
        # В този случай Иван печели
        break

if ivan_score == 0:
    print("Ivan wins")
elif maria_score == 0:
    print("Maria wins")


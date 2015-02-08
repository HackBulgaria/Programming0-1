score = input("Enter student score: ")
score = int(score)

# Отново, трябва да проверим оценката в какъв интервал е

if score <= 50:
    print("Слаб 2")
elif score >= 51 and score <= 60:
    print("Среден 3")
elif score >= 61 and score <= 70:
    print("Добър 4")
elif score >= 71 and score <= 80:
    print("Много Добър 5")
elif score >= 81 and score <= 99:
    print("Отличен 6")
elif score == 100:
    print("Много Отличен 7")

# Трябва да решим задачата, колко са уникалните имена в activity
# Ще държим уникалните хора в списъка counted_people
# И само ако намерим човек, който не е в списъка, тогава ще го добавим
# Накрая бройката на уникалните хора ще е равна на бройката на елементи в списъка

def get_people_count(activity):
    counted_people = []
    
    for person in activity:
        if person not in counted_people:
            counted_people += [person]

    return len(counted_people)

print(get_people_count(["Rado", "Ivo", "Maria", "Anneta", "Rado", "Rado", "Anneta", "Ivo", "Maria", "Rado"]))


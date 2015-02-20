def square(x):
    return x ** 2


# Това е същата задача като това да намерим произведението на числата от 1 до n
def factorial(n):
    result = 1
    start = 1

    while start <= n:
        result *= start
        start += 1

    return result


# За всеки елемент в списъка, увеличаваме един брояч
def count_elements(items):
    result = 0

    for item in items:
        result += 1

    return result


# Използваме флагова променлива
# В началото казваме, че не сме намерили x
# Освен ако наистина не го намерим, обхождайки xs
def member(x, xs):
    found = False
    
    for memb in xs:
        if x == memb:
            found = True
            break

    return found


# Използваме index-a, за да знаем на кой студент и коя оценка сме
# По условие знаем, че студентът на index i, има оценка в grades[i]
def grades_that_pass(students, grades, limit):
    result = []
    index = 0

    for grade in grades:
        student = students[index]
        
        if grade >= limit:
            result = result + [student]
        
        index += 1

    return result

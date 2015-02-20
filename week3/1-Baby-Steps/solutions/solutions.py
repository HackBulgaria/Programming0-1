def square(x):
    return x ** 2

def factorial(n):
    result = 1
    start = 1

    while start <= n:
        result *= start
        start += 1

    return result

def count_elements(items):
    result = 0

    for item in items:
        result += 1

    return result

def member(x, xs):
    found = False
    
    for memb in xs:
        if x == memb:
            found = True
            break

    return found

def grades_that_pass(students, grades, limit):
    result = []
    index = 0

    for grade in grades:
        student = students[index]
        
        if grade >= limit:
            result = result + [student]
        
        index += 1

    return result

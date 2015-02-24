# Функцията взима списък и връща последния елемент
def last(items):
    return items[len(items) - 1]

# Функцията взима списък и връща предпоследния елемент
def before_last(items):
    return items[len(items) - 2]

# Функцията връща списък с първите n елемента от редицата на Фибоначи
def fib(n):
    if n == 1:
        return [1]

    if n == 2:
        return [1, 1]
    
    result = [1, 1]
    
    while len(result) < n:
        next_fib = last(result) + before_last(result)
        result = result + [next_fib]

    return result


# Функцията взима едно цяло число и връща броя на неговите цифри
def count_digits(n):
    result = 0

    while n != 0:
        result += 1
        n = n // 10

    return result


# Функцията взима списък от цели числа, които може и да са с повече от 1 цифра
# Напришер [1, 12, 18, 5]
# И връща число, което представлява всички цифри събрани заедно: 112185
def to_number(numbers):
    result = 0

    for number in numbers:
        # Умножаваме по 10^на степен = броя на цифрите на числото, с което ще съберем
        # Така си освобождаваме толова на брой места (0ли)
        multiplier = 10 ** count_digits(number)
        result = result * multiplier + number 
    
    return result


def fib_number(n):
    return to_number(fib(n))


















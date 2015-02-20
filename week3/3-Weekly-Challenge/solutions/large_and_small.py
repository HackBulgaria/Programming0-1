def to_digits(n):
    result = []
    
    while n != 0:
        digit = n % 10
        
        result = [digit] + result

        n = n // 10

    return result


# Приемаме, че в digits ще имаме само едноцифрени числа
def to_number(digits):
    result = 0

    for digit in digits:
        result = result * 10 + digit

    return result


# Функията взима число и връща най-голямото число
# Което може да се направи от цифрите на n
# Алгоритъма, който използваме е следния:
# Превръщаме числото в списък от цифри
# Сортираме този списък от най-голямата към най-малката цифра
# Превръщаме списъкът отново в число
def max_number(n):
    digits = to_digits(n)

    # Подреждаме списъка чрез сортиране в обратна посока
    digits = sorted(digits, reverse=True)
    
    return to_number(digits)


# Функията взима число и връща най-малкото число
# Което може да се направи от цифрите на n
# Алгоритъма, който използваме е следния:
# Превръщаме числото в списък от цифри
# Сортираме този списък от най-малката към най-голямата цифра
# Превръщаме списъкът отново в число
def min_number(n):
    digits = to_digits(n)

    digits = sorted(digits)

    return to_number(digits)

n = input("Enter n: ")
n = int(n)

print(max_number(n))
print(min_number(n))

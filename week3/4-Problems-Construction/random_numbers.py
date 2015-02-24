from random import randint

# Тук решението е стандартно.
# Въртим n на брой пъти,
# Като всеки път взимаме случайно число в интервала [start, end]
def generate_random_list(n, start, end):
    result = []
    counter = 0
    while counter < n:
        next_number = randint(start, end)
        result = result + [next_number]

        counter += 1
        
    return result

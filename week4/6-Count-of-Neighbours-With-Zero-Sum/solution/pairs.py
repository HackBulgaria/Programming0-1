def count_zero_neighbours(numbers):
    count = 0
    index = 0

    for number in numbers:
        if index < len(numbers) - 1:
            neighbour = numbers[index + 1]

            if number + neighbour == 0:
                count += 1
        index += 1

    return count


def count_zero_pairs(numbers):
    count = 0
    n = len(numbers)
    
    for x_index in range(0, n):
        for y_index in range(x_index, n):
            x = numbers[x_index]
            y = numbers[y_index]

            if x + y == 0:
                count += 1

    return count


def is_prime(n):
    start = 2
    is_prime = True

    while start < n:
        if n % start == 0:
            is_prime = False
            break

        start += 1

    return is_prime


def prime_pair(numbers):
    for x in numbers:
        for y in numbers:
            if is_prime(x + y):
                return True

    return False


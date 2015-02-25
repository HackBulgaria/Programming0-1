def zero_neighbours(numbers):
    index = 0

    for number in numbers:
        if index < len(numbers) - 1:
            neighbour = numbers[index + 1]

            if number + neighbour == 0:
                return True
        index += 1

    return False

print(zero_neighbours([1, -1, 2, 3]))
print(zero_neighbours([1, 1, 2, 3, -3]))
print(zero_neighbours([1, 1, 2, 3, 3]))

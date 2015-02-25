def zero_pairs(numbers):
    for x in numbers:
        for y in numbers:
            if x + y == 0:
                return True

    return False

print(zero_pairs([1, 2, 3, -1]))
print(zero_pairs([1, 2, 3, 4, 5]))

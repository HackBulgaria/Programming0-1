# Връщаме индекса на най-малкия елемент в списъка
def min_index(arr):
    result = 0
    index = 0

    for x in arr:
        if x < arr[result]:
            result = index
        index += 1

    return result


def selection_sort_that_destroys(numbers):
    result = []
    n = len(numbers)

    while len(result) != n:
        current_min_index = min_index(numbers)
        result.append(numbers[current_min_index])
        del numbers[current_min_index]

    return result


def swap(i, j, items):
    temp = items[i]
    items[i] = items[j]
    items[j] = temp


def min_index_from(start_index, items):
    result = start_index
    n = len(items)

    for index in range(start_index, n):
        if items[index] < items[result]:
            result = index
        index += 1

    return result


def selection_sort_that_mutates(numbers):
    n = len(numbers)

    for i in range(0, n):
        index_of_min_from_i = min_index_from(i, numbers)
        swap(i, index_of_min_from_i, numbers)


def diff(a, b):
    result = []

    for item in a:
        if item not in b:
            result.append(item)

    return result


def min_index_without_used(numbers, used):
    unused_indexes = diff(range(0, len(numbers)), used)

    min_index = unused_indexes[0]

    for index in unused_indexes:
        if numbers[index] < numbers[min_index]:
            min_index = index

    return min_index


def selection_sort(numbers):
    result = []
    n = len(numbers)
    used = []

    while len(result) != n:
        min_index = min_index_without_used(numbers, used)
        used.append(min_index)
        result.append(numbers[min_index])

    return result


a = [100, 0, 0, -10, 5]
b = selection_sort(a)
print(a)
print(b)

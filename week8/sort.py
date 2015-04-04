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
        result.append(arr[current_min_index])
        del arr[current_min_index]
    

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


a = [100, 0, -10, 5]
selection_sort_that_mutates(a)
print(a)












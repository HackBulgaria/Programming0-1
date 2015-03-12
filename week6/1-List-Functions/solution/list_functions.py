def head(items):
    return items[0]


# Брои от 0!
def last(items):
    last_index = len(items) - 1
    return items[last_index]


def tail(items):
    result = []

    for index in range(1, len(items)):
        item = items[index]
        result += [item]

    return result


def equal_lists(l1, l2):
    if len(l1) != len(l2):
        return False

    while len(l1) != 0:
        if head(l1) != head(l2):
            return False

        l1 = tail(l1)
        l2 = tail(l2)

    return True


def eq_lists(l1, l2):
    if len(l1) != len(l2):
        return False

    for index in range(0, len(l1)):
        if l1[index] != l2[index]:
            return False

    return True


def count_item(search, items):
    count = 0

    for item in items:
        if item == search:
            count += 1

    return count


def take2(n, items):
    result = []
    taken = 0

    while taken != n and len(items) != 0:
        item = head(items)
        result += [item]
        taken += 1
        items = tail(items)

    return result


def take(n, items):
    result = []

    for index in range(0, min(n, len(items))):
        result += [items[index]]

    return result


def drop(n, items):
    result = []

    for index in range(n, len(items)):
        result += [items[index]]

    return result


def reverse(items):
    result = []

    last_index = len(items) - 1

    while last_index >= 0:
        result += [items[last_index]]
        last_index -= 1

    return result


def main():
    print("ahahahaha")


if __name__ == '__main__':
    main()
